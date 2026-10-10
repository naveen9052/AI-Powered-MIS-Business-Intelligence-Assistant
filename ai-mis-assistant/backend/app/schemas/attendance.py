from datetime import date, time
from typing import Literal
from pydantic import BaseModel


class AttendanceCreate(BaseModel):
    employee_id: int
    attendance_date: date
    check_in: time | None = None
    check_out: time | None = None
    status: Literal["Present", "Absent", "Leave", "Remote"] = "Present"


class Attendance(AttendanceCreate):
    id: int
    employee_name: str
