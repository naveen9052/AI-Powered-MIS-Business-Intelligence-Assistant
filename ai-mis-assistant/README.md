# AI MIS Assistant

A starter internal dashboard for employee records, attendance, sales summaries, and business questions. The backend uses FastAPI and PostgreSQL; the frontend is plain HTML, CSS, and JavaScript.

## PostgreSQL setup

The starter expects a local PostgreSQL server and a database/login. If you used the earlier setup instructions, the defaults below match `mis_user` and `ai_mis_assistant`.

1. From this directory, create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

2. Install the backend dependencies:

   ```powershell
   py -m pip install -r requirements.txt
   ```

3. Create a local environment file and enter the password you set for the PostgreSQL login:

   ```powershell
   Copy-Item .env.example .env
   notepad .env
   ```

   The default connection setting is:

   ```env
   DATABASE_URL=postgresql://mis_user:YOUR_PASSWORD@localhost:5432/ai_mis_assistant
   ```

   If your database, user, host, or port differs, update the URL. URL-encode reserved characters in the password (for example, `@` becomes `%40`). Keep `.env` private; it is ignored by Git.

4. Start the API from this directory:

   ```powershell
   cd backend
   py -m uvicorn app.main:app --reload
   ```

   On first startup, the app creates the tables/indexes and inserts sample employees and sales if the employee table is empty. No manual schema command is needed. Open the dashboard from `frontend/index.html`; API docs are at `http://127.0.0.1:8000/docs`.

## Database and existing data

`sql/schema.sql` is the PostgreSQL schema; `sql/sample_data.sql` contains optional sample inserts. CSV files under `data/` are import templates and are not loaded automatically. The app now connects to PostgreSQL and does not automatically import any previous SQLite file. If you have SQLite records to retain, export and import them separately before using PostgreSQL.

See [`docs/database-design.md`](docs/database-design.md) for the ER diagram, constraints, and data model.

## API overview

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | `/api/health` | Health check |
| GET, POST | `/api/employees` | List or add employees |
| PATCH | `/api/employees/{id}/deactivate` | Deactivate employee |
| GET, POST | `/api/attendance` | List by optional `day` or record attendance |
| GET | `/api/reports/summary` | Workforce and monthly sales snapshot |
| GET | `/api/reports/sales-by-department` | Sales totals by department |
| POST | `/api/ai/ask` | Ask the assistant (`{"question":"..."}`) |

## Current limits

This is a local development starter, not a production deployment. Authentication/authorization, audit logging, input governance, real LLM integration, PDF/vector RAG, and write-action approvals still need to be designed before company data or permitted AI actions are enabled. The assistant does not execute business actions. For policy search, add approved `.txt` files to `documents/`; PDFs are not indexed yet.
