from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import get_connection
from app.routes import reports, employees, ai


app = FastAPI(
    title="AI-Powered MIS & Business Intelligence Assistant"
)


# Allow frontend (Live Server) to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    reports.router,
    prefix="/api/reports",
    tags=["Reports"]
)

app.include_router(
    employees.router,
    prefix="/api/employees",
    tags=["Employees"]
)

app.include_router(
    ai.router,
    prefix="/api/ai",
    tags=["AI Assistant"]
)


@app.get("/")
def root():
    return {
        "message": "AI MIS Assistant API is running"
    }


@app.get("/health/database")
def database_health():
    with get_connection() as connection:
        result = connection.execute(
            "SELECT current_database() AS database_name"
        ).fetchone()

    return {
        "status": "connected",
        "database": result["database_name"]
    }