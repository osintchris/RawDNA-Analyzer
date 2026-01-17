@echo off
echo ============================================================
echo DNA Analysis Tool - Build Executable
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

echo [1/4] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo [2/4] Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.spec del /q *.spec

echo.
echo [3/4] Building executable...
pyinstaller --onefile --windowed --name=DNAAnalysisTool ^
    --hidden-import=customtkinter ^
    --hidden-import=pandas ^
    --hidden-import=numpy ^
    --hidden-import=PIL ^
    --hidden-import=PIL.Image ^
    --hidden-import=PIL.ImageTk ^
    --hidden-import=tkinter ^
    --hidden-import=tkinter.filedialog ^
    --hidden-import=tkinter.messagebox ^
    --hidden-import=dna_parser ^
    --hidden-import=traits_data ^
    --hidden-import=expanded_traits ^
    --hidden-import=reference_populations ^
    --hidden-import=real_ancestry_data ^
    --hidden-import=calibrated_ancestry_engine ^
    --hidden-import=comprehensive_analysis ^
    --hidden-import=ancestry_markers_real ^
    --hidden-import=ancestry_markers_expanded ^
    --hidden-import=ancestry_markers_merged ^
    --hidden-import=ancestry_deep_database ^
    --hidden-import=ancient_dna_database ^
    --hidden-import=ancient_dna_history_database ^
    --hidden-import=behavioral_genetics_database ^
    --hidden-import=sleep_genetics_database ^
    --hidden-import=physical_traits_expanded_database ^
    --hidden-import=pharmacogenomics_database ^
    --hidden-import=carrier_status_database ^
    --hidden-import=sports_genetics_database ^
    --hidden-import=immune_deep_genetics_database ^
    --hidden-import=longevity_genetics_database ^
    --hidden-import=mental_health_database ^
    --hidden-import=cancer_risk_database ^
    --hidden-import=cardiovascular_database ^
    --hidden-import=skin_dermatology_database ^
    --hidden-import=sensory_genetics_database ^
    --hidden-import=nutrition_metabolism_database ^
    --hidden-import=reproduction_genetics_database ^
    --hidden-import=unique_features_database ^
    --hidden-import=expanded_genetics_database ^
    --hidden-import=advanced_traits_database ^
    --hidden-import=unique_features_analysis ^
    --hidden-import=carrier_ui ^
    --hidden-import=behavioral_ui ^
    --hidden-import=sleep_ui ^
    --hidden-import=physical_traits_expanded_ui ^
    --hidden-import=sports_ui ^
    --hidden-import=immune_deep_ui ^
    --hidden-import=longevity_ui ^
    --hidden-import=pharmacogenomics_ui ^
    --hidden-import=mental_health_ui ^
    --hidden-import=cancer_risk_ui ^
    --hidden-import=cardiovascular_ui ^
    --hidden-import=skin_dermatology_ui ^
    --hidden-import=ancestry_deep_ui ^
    --hidden-import=ancestry_ethnicity_ui ^
    --hidden-import=sensory_ui ^
    --hidden-import=nutrition_metabolism_ui ^
    --hidden-import=reproduction_ui ^
    --hidden-import=ancient_dna_history_ui ^
    --hidden-import=unique_features_ui ^
    --collect-data=customtkinter ^
    --noconfirm ^
    main.py

echo.
echo [4/4] Build verification...
if exist dist\DNAAnalysisTool.exe (
    echo SUCCESS: Executable created!
) else (
    echo ERROR: Build failed - executable not found
    pause
    exit /b 1
)

echo.
echo ============================================================
echo BUILD COMPLETE!
echo.
echo Your executable is at: dist\DNAAnalysisTool.exe
echo.
echo To run the application:
echo   1. Navigate to the 'dist' folder
echo   2. Double-click DNAAnalysisTool.exe
echo ============================================================
pause
