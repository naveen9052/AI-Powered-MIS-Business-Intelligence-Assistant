from fastapi import APIRouter, Query
from app.schemas.employee import EmployeeCreate
from app.services import employee_service

router = APIRouter()


@router.get("")
def get_employees(search: str = Query(default="", max_length=120)):
    return employee_service.list_employees(search)


@router.post("", status_code=201)
def post_employee(employee: EmployeeCreate):
    return employee_service.create_employee(employee.model_dump())


@router.patch("/{employee_id}/deactivate")
def patch_deactivate(employee_id: int):
    return employee_service.deactivate_employee(employee_id)
