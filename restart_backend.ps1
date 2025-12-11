# PowerShell script to restart the backend server
Write-Host "Restarting Radiology Assistant Backend..." -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# Step 1: Find and stop the existing backend process
Write-Host "`nStep 1: Stopping existing backend..." -ForegroundColor Yellow

# Find process using port 8000
$process = Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess -First 1

if ($process) {
    Write-Host "  Found process on port 8000 (PID: $process)" -ForegroundColor Gray
    Stop-Process -Id $process -Force
    Write-Host "  ✓ Stopped old backend" -ForegroundColor Green
    Start-Sleep -Seconds 2
} else {
    Write-Host "  No process found on port 8000" -ForegroundColor Gray
}

# Step 2: Start the new backend
Write-Host "`nStep 2: Starting new backend..." -ForegroundColor Yellow
Write-Host "  Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""

# Start the backend in this window
python -m backend.main
