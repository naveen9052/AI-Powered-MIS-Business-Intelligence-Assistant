from pydantic import BaseModel


class Summary(BaseModel):
    employees: int
    present_today: int
    sales_month: float
    attendance_rate: float
