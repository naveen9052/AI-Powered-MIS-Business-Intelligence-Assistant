# 🤖 AI-Powered MIS & Business Intelligence Assistant

An AI-powered Management Information System (MIS) and Business Intelligence application designed to simplify employee management, attendance tracking, business reporting, and data analysis through a centralized dashboard.

## 🚀 Features

* **Dashboard:** View employee statistics, attendance summaries, and monthly sales.
* **Employee Management:** Access and manage employee information.
* **Attendance Tracking:** Monitor employee attendance records.
* **Business Reports:** Review business performance and operational data.
* **AI Assistant:** Designed to help users interact with business information and access insights.
* **REST API:** Backend endpoints for application data and functionality.
* **PostgreSQL Integration:** Store and retrieve structured business data.

## 🛠️ Technologies Used

### Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL

### Frontend

* HTML5
* CSS3
* JavaScript

### Tools

* Git and GitHub
* Visual Studio Code
* Uvicorn

## 📁 Project Structure

```text
ai-mis-assistant/
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   ├── config/
│   │   ├── database/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   └── requirements.txt
├── frontend/
│   ├── css/
│   ├── js/
│   ├── index.html
│   ├── dashboard.html
│   ├── employees.html
│   ├── attendance.html
│   ├── reports.html
│   └── ai-assistant.html
├── data/
├── docs/
├── sql/
├── tests/
├── .env.example
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/naveen9052/AI-Powered-MIS-Business-Intelligence-Assistant.git
```

### 2. Navigate to the project directory

```bash
cd AI-Powered-MIS-Business-Intelligence-Assistant/ai-mis-assistant
```

### 3. Create a Python virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 5. Configure environment variables

Create a `.env` file using `.env.example` as a reference.

Configure the required values, including your PostgreSQL database connection string.

**Security:** Never commit your `.env` file, database password, or API keys to GitHub.

### 6. Set up the database

Create a PostgreSQL database and configure the connection details.

Review the SQL files in the `sql/` directory and the database design documentation in `docs/` before initializing the schema.

### 7. Start the backend

From the `ai-mis-assistant` directory, run:

```bash
uvicorn app.main:app --app-dir backend --reload
```

The API should be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 8. Run the frontend

Open `frontend/index.html` using VS Code Live Server or another local HTTP server.

Ensure the frontend API configuration points to the running backend.

## 🔌 API Endpoints

The project includes API route modules for the following areas:

| Module         | Purpose                          |
| -------------- | -------------------------------- |
| Reports        | Business summaries and reporting |
| Employees      | Employee information             |
| Attendance     | Attendance records               |
| Authentication | Login and authentication         |
| AI Assistant   | AI-related functionality         |

For available endpoints and request formats, run the backend and visit `/docs`.

## 🎯 Project Objectives

* Centralize business and employee information.
* Simplify attendance monitoring and reporting.
* Provide a dashboard for business performance analysis.
* Explore AI-assisted access to business insights.
* Demonstrate full-stack application development and database integration.

## 🔮 Future Enhancements

* Advanced business analytics and interactive visualizations.
* Role-based access control.
* Exportable reports.
* Improved AI-powered natural-language queries.
* Cloud deployment.
* Automated testing and monitoring.

## 👨‍💻 Author

**Naveen Kumar**

B.Tech — Artificial Intelligence and Machine Learning

GitHub: [@naveen9052](https://github.com/naveen9052)

## 📄 License

This project is available for educational and portfolio purposes. Add a specific open-source license if you intend to grant permissions for reuse and distribution.
