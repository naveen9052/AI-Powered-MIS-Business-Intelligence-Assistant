from datetime import date
from fastapi import APIRouter
from app.schemas.attendance import AttendanceCreate
from app.services import attendance_service

router = APIRouter()


@router.get("")
def get_attendance(day: date | None = None):
    return attendance_service.list_attendance(day.isoformat() if day else None)


@router.post("", status_code=201)
def post_attendance(record: AttendanceCreate):
    return attendance_service.record_attendance(record.model_dump())
