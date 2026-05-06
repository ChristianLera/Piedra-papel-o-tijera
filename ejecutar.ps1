# Piedra, Papel o Tijera - Script de ejecución para PowerShell
# Autor: Christian Lera

# Configurar la consola
$Host.UI.RawUI.WindowTitle = "Piedra, Papel o Tijera - Christian Lera"
# Colores para mejor experiencia
$Host.UI.RawUI.ForegroundColor = "Green"

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "   Iniciando el juego Piedra, Papel o Tijera" -ForegroundColor Yellow
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python detectado:" -ForegroundColor Green
    Write-Host $pythonVersion -ForegroundColor White
    Write-Host ""
}
catch {
    Write-Host "[ERROR] No se encontró Python instalado en el sistema." -ForegroundColor Red
    Write-Host ""
    Write-Host "Por favor, instala Python desde https://python.org" -ForegroundColor Yellow
    Write-Host "Asegúrate de marcar 'Add Python to PATH' durante la instalación." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Presiona cualquier tecla para salir..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}

# Verificar que el archivo del juego existe
if (-not (Test-Path "PiedraPapelTijera.py")) {
    Write-Host "[ERROR] No se encontró el archivo PiedraPapelTijera.py" -ForegroundColor Red
    Write-Host "Asegúrate de que el archivo está en la misma carpeta que este script." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Presiona cualquier tecla para salir..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}

# Ejecutar el juego
Write-Host "Iniciando juego..." -ForegroundColor Magenta
Write-Host ""
Start-Process -NoNewWindow -Wait python -ArgumentList "PiedraPapelTijera.py"

Write-Host ""
Write-Host "Gracias por jugar!" -ForegroundColor Green
Start-Sleep -Seconds 3