import psycopg
from psycopg.rows import dict_row

from app.config.settings import DATABASE_URL


def get_connection():
    if not DATABASE_URL:
        raise RuntimeError(
            "DATABASE_URL is missing. Check the .env file."
        )

    return psycopg.connect(
        DATABASE_URL,
        row_factory=dict_row
    )