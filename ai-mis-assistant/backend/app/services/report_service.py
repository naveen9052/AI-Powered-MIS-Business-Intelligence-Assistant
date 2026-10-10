from datetime import date

from app.database.connection import get_connection


def get_summary() -> dict:
    today = date.today()
    month_start = today.replace(day=1)

    if month_start.month == 12:
        next_month = month_start.replace(
            year=month_start.year + 1,
            month=1
        )
    else:
        next_month = month_start.replace(
            month=month_start.month + 1
        )

    with get_connection() as db:

        # 1. Active employees
        employees = db.execute(
            """
            SELECT COUNT(*) AS count
            FROM employees
            WHERE status = 'Active'
            """
        ).fetchone()["count"]

        # 2. Find the latest attendance date available
        latest_date = db.execute(
            """
            SELECT MAX(date) AS latest_date
            FROM attendance
            """
        ).fetchone()["latest_date"]

        # 3. Present employees on latest available date
        present = 0
        recorded = 0

        if latest_date:
            present = db.execute(
                """
                SELECT COUNT(*) AS count
                FROM attendance
                WHERE date = %s
                  AND status = 'Present'
                """,
                (latest_date,)
            ).fetchone()["count"]

            recorded = db.execute(
                """
                SELECT COUNT(*) AS count
                FROM attendance
                WHERE date = %s
                """,
                (latest_date,)
            ).fetchone()["count"]

        # 4. Monthly sales
        sales = db.execute(
            """
            SELECT COALESCE(SUM(achieved), 0) AS total_sales
            FROM sales
            WHERE month = (
                SELECT MAX(month)
                FROM sales
            )
            """
        ).fetchone()["total_sales"]

        # 5. Attendance percentage
        attendance_rate = (
            (present / recorded) * 100
            if recorded
            else 0
        )

        return {
            "employees": employees,
            "present_today": present,
            "sales_month": float(sales),
            "attendance_rate": round(attendance_rate, 1)
        }


def sales_by_department() -> list[dict]:
    with get_connection() as db:

        rows = db.execute(
            """
            SELECT
                d.department_name AS department,
                SUM(s.achieved) AS amount
            FROM sales s
            JOIN employees e
                ON e.id = s.employee_id
            JOIN departments d
                ON d.id = e.department_id
            GROUP BY d.id, d.department_name
            ORDER BY amount DESC
            """
        ).fetchall()

        return [
            {
                "department": row["department"],
                "amount": float(row["amount"])
            }
            for row in rows
        ]