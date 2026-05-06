@echo off
title Piedra, Papel o Tijera - Christian Lera
color 0A

echo ================================================
echo    Iniciando el juego Piedra, Papel o Tijera
echo ================================================
echo.

:: Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] No se encontro Python instalado en el sistema.
    echo.
    echo Por favor, instala Python desde https://python.org
    echo Asegurate de marcar "Add Python to PATH" durante la instalacion.
    echo.
    pause
    exit /b 1
)

:: Mostrar versión de Python
echo Python detectado:
python --version
echo.

:: Ejecutar el juego
echo Iniciando juego...
echo.
python PiedraPapelTijera.py

:: Si el archivo no existe
if errorlevel 1 (
    echo.
    echo [ERROR] No se encontro el archivo PiedraPapelTijera.py
    echo Asegurate de que el archivo esta en la misma carpeta que este script.
)

echo.
echo Gracias por jugar!
timeout /t 3 >nul