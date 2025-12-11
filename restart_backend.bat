@echo off
echo Restarting Radiology Assistant Backend...
echo ==========================================
echo.

echo Step 1: Stopping existing backend...
for /f "tokens=5" %%a in ('netstat -aon ^| find ":8000" ^| find "LISTENING"') do (
    echo   Found process on port 8000 (PID: %%a)
    taskkill /F /PID %%a >nul 2>&1
    echo   √ Stopped old backend
)

timeout /t 2 /nobreak >nul

echo.
echo Step 2: Starting new backend...
echo   Press Ctrl+C to stop the server
echo.

python -m backend.main
