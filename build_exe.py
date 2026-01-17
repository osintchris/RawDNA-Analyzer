#!/usr/bin/env python3
"""
Build script to create executable using PyInstaller
Cross-platform alternative to BUILD.bat
"""

import subprocess
import sys
import os
import shutil

def build_exe():
    """Build the executable"""

    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print("=" * 60)
    print("DNA Analysis Tool - Executable Builder")
    print("=" * 60)

    # Install/upgrade requirements first
    print("\n[1/4] Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

    # Clean previous builds
    print("\n[2/4] Cleaning previous builds...")
    for folder in ["build", "dist"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
    for f in os.listdir("."):
        if f.endswith(".spec"):
            os.remove(f)

    # Build the executable with all hidden imports
    print("\n[3/4] Building executable...")

    hidden_imports = [
        # Core dependencies
        "customtkinter", "pandas", "numpy",
        "PIL", "PIL.Image", "PIL.ImageTk",
        "tkinter", "tkinter.filedialog", "tkinter.messagebox",
        # Core modules
        "dna_parser", "traits_data", "expanded_traits",
        "reference_populations", "real_ancestry_data",
        "calibrated_ancestry_engine", "comprehensive_analysis",
        # Ancestry markers
        "ancestry_markers_real", "ancestry_markers_expanded", "ancestry_markers_merged",
        # Databases
        "ancestry_deep_database", "ancient_dna_database", "ancient_dna_history_database",
        "behavioral_genetics_database", "sleep_genetics_database",
        "physical_traits_expanded_database", "pharmacogenomics_database",
        "carrier_status_database", "sports_genetics_database",
        "immune_deep_genetics_database", "longevity_genetics_database",
        "mental_health_database", "cancer_risk_database",
        "cardiovascular_database", "skin_dermatology_database",
        "sensory_genetics_database", "nutrition_metabolism_database",
        "reproduction_genetics_database", "unique_features_database",
        "expanded_genetics_database", "advanced_traits_database",
        "unique_features_analysis",
        # UI modules
        "carrier_ui", "behavioral_ui", "sleep_ui",
        "physical_traits_expanded_ui", "sports_ui",
        "immune_deep_ui", "longevity_ui", "pharmacogenomics_ui",
        "mental_health_ui", "cancer_risk_ui", "cardiovascular_ui",
        "skin_dermatology_ui", "ancestry_deep_ui", "ancestry_ethnicity_ui",
        "sensory_ui", "nutrition_metabolism_ui", "reproduction_ui",
        "ancient_dna_history_ui", "unique_features_ui",
    ]

    pyinstaller_args = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--name=DNAAnalysisTool",
    ]

    # Add all hidden imports
    for imp in hidden_imports:
        pyinstaller_args.extend(["--hidden-import", imp])

    pyinstaller_args.extend([
        "--collect-data=customtkinter",
        "--noconfirm",
        "main.py"
    ])

    subprocess.run(pyinstaller_args, check=True)

    # Verify build
    print("\n[4/4] Build verification...")
    exe_path = os.path.join(script_dir, "dist", "DNAAnalysisTool.exe")
    if os.path.exists(exe_path):
        print(f"SUCCESS: Executable created!")
        print(f"\nExecutable location: {exe_path}")
        print("\nYou can now run the application by double-clicking the .exe file.")
    else:
        print("ERROR: Build failed - executable not found")
        sys.exit(1)

if __name__ == "__main__":
    build_exe()
