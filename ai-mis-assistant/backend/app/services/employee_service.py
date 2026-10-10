from fastapi import HTTPException
from psycopg import errors

from app.database.connection import get_connection


def list_employees(search: str = "") -> list[dict]:
    with get_connection() as db:
        pattern = f"%{search}%"

        rows = db.execute(
            """
            SELECT
                e.id,
                e.employee_code,
                e.name,
                e.email,
                d.department_name AS department,
                e.designation,
                e.joining_date,
                e.salary,
                e.status
            FROM employees e
            JOIN departments d
                ON d.id = e.department_id
            WHERE
                e.name ILIKE %s
                OR d.department_name ILIKE %s
                OR e.email ILIKE %s
            ORDER BY e.name
            """,
            (pattern, pattern, pattern)
        ).fetchall()

        return [dict(row) for row in rows]


def create_employee(data: dict) -> dict:
    try:
        with get_connection() as db:
            department = data["department"].strip()

            department_row = db.execute(
                """
                SELECT id
                FROM departments
                WHERE department_name = %s
                """,
                (department,)
            ).fetchone()

            if not department_row:
                raise HTTPException(
                    status_code=400,
                    detail=f"Department '{department}' does not exist"
                )

            cursor = db.execute(
                """
                INSERT INTO employees
                (
                    employee_code,
                    name,
                    email,
                    department_id,
                    designation,
                    joining_date,
                    salary
                )
                VALUES
                (
                    %s, %s, %s, %s, %s, %s, %s
                )
                RETURNING id
                """,
                (
                    data["employee_code"],
                    data["name"],
                    data["email"],
                    department_row["id"],
                    data["designation"],
                    data["joining_date"],
                    data.get("salary")
                )
            )

            employee_id = cursor.fetchone()["id"]

            row = db.execute(
                """
                SELECT
                    e.id,
                    e.employee_code,
                    e.name,
                    e.email,
                    d.department_name AS department,
                    e.designation,
                    e.joining_date,
                    e.salary,
                    e.status
                FROM employees e
                JOIN departments d
                    ON d.id = e.department_id
                WHERE e.id = %s
                """,
                (employee_id,)
            ).fetchone()

            return dict(row)

    except errors.UniqueViolation as error:
        raise HTTPException(
            status_code=409,
            detail="An employee with this email or employee code already exists"
        ) from error


def deactivate_employee(employee_id: int) -> dict:
    with get_connection() as db:
        result = db.execute(
            """
            UPDATE employees
            SET status = 'Inactive'
            WHERE id = %s
            """,
            (employee_id,)
        )

        if result.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        row = db.execute(
            """
            SELECT
                e.id,
                e.employee_code,
                e.name,
                e.email,
                d.department_name AS department,
                e.designation,
                e.joining_date,
                e.salary,
                e.status
            FROM employees e
            JOIN departments d
                ON d.id = e.department_id
            WHERE e.id = %s
            """,
            (employee_id,)
        ).fetchone()

        return dict(row)