from fastapi import APIRouter
from app.services import report_service

router = APIRouter()


@router.get("/summary")
def summary():
    return report_service.get_summary()


@router.get("/sales-by-department")
def sales_by_department():
    return report_service.sales_by_department()
