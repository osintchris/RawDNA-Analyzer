@echo off
echo ============================================================
echo DNA Analysis Tool - Starting Application
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

REM Check if dependencies are installed, install if missing
echo Checking dependencies...

pip show customtkinter >nul 2>&1
if errorlevel 1 (
    echo Installing customtkinter...
    pip install customtkinter>=5.2.0
)

pip show pillow >nul 2>&1
if errorlevel 1 (
    echo Installing pillow...
    pip install pillow>=9.0.0
)

pip show pandas >nul 2>&1
if errorlevel 1 (
    echo Installing pandas...
    pip install pandas>=1.5.0
)

pip show numpy >nul 2>&1
if errorlevel 1 (
    echo Installing numpy...
    pip install numpy>=1.23.0
)

echo.
echo Starting DNA Analysis Tool...
echo.
python main.py
