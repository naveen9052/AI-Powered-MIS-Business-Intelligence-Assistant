@echo off
set "PROJECT=D:\AI-Powered MIS & Business Intelligence Assistant\ai-mis-assistant"

echo Starting Backend...
start "AI MIS Backend" cmd /k "pushd "%PROJECT%\backend" && python -m uvicorn app.main:app --host 127.0.0.1 --port 8001"

echo Starting Frontend...
start "AI MIS Frontend" cmd /k "python -m http.server 5500 --directory "%PROJECT%\frontend""

timeout /t 4 /nobreak >nul

start http://127.0.0.1:5500/index.html

echo.
echo ==================================
echo Website: http://127.0.0.1:5500
echo API    : http://127.0.0.1:8001
echo ==================================

