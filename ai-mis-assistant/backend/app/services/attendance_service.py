from fastapi import HTTPException
from psycopg import errors
from app.database.connection import get_connection


def list_attendance(day: str | None = None) -> list[dict]:
    with get_connection() as db:
        rows = db.execute("""SELECT a.*, e.name AS employee_name, d.name AS department
            FROM attendance a JOIN employees e ON e.id=a.employee_id JOIN departments d ON d.id=e.department_id
            WHERE (%s::date IS NULL OR a.attendance_date=%s::date) ORDER BY a.attendance_date DESC, e.name""", (day, day)).fetchall()
        return [dict(row) for row in rows]


def record_attendance(data: dict) -> dict:
    try:
        with get_connection() as db:
            cursor = db.execute("""INSERT INTO attendance(employee_id,attendance_date,check_in,check_out,status)
                VALUES(%s,%s,%s,%s,%s) RETURNING id""", (data["employee_id"],data["attendance_date"],data["check_in"],data["check_out"],data["status"]))
            attendance_id = cursor.fetchone()["id"]
            row = db.execute("""SELECT a.*,e.name AS employee_name,d.name AS department FROM attendance a
                JOIN employees e ON e.id=a.employee_id JOIN departments d ON d.id=e.department_id WHERE a.id=%s""", (attendance_id,)).fetchone()
            return dict(row)
    except errors.ForeignKeyViolation as error:
        raise HTTPException(status_code=404, detail="Employee not found") from error
    except errors.UniqueViolation as error:
        if error.diag.constraint_name == "attendance_employee_id_attendance_date_key":
            raise HTTPException(status_code=409, detail="Attendance already recorded for this employee and date") from error
        raise
