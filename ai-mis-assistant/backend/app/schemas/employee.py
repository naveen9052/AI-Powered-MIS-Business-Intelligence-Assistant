from datetime import date

from pydantic import BaseModel, Field


class EmployeeCreate(BaseModel):
    employee_code: str = Field(min_length=1, max_length=20)
    name: str = Field(min_length=1, max_length=100)
    email: str = Field(
        pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
        max_length=150
    )
    department: str = Field(min_length=1, max_length=100)
    designation: str = Field(min_length=1, max_length=100)
    joining_date: date
    salary: float | None = None


class Employee(EmployeeCreate):
    id: int
    status: str

    class Config:
        from_attributes = True