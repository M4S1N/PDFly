param (
    [int]$port = 8000
)

Write-Host "`nSelected port: $port" -ForegroundColor Cyan

Write-Host "`nBuilding Docker image..." -ForegroundColor Cyan
docker build -t fastapi .
if (-not $?) {
    Write-Host "`nDocker build failed. Aborting..." -ForegroundColor Red
    exit 1
}

Write-Host "`nStopping previous container (if any)..." -ForegroundColor Yellow
docker stop fastapi-container 2>$null

Write-Host "`nRemoving previous container (if any)..." -ForegroundColor Yellow
docker rm fastapi-container 2>$null

Write-Host "`nStarting new container..." -ForegroundColor Green
docker run -d -p "${port}:8000" --name fastapi-container fastapi
if (-not $?) {
    Write-Host "`nFailed to start Docker container." -ForegroundColor Red
    exit 1
}

Write-Host "`nFastAPI is running at: http://localhost:$port" -ForegroundColor Green
Start-Process "http://localhost:$port/docs"
