@echo off
echo ========================================
echo DPL FBR Digital Invoicing System Setup
echo ========================================

echo.
echo Creating virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Setup completed successfully!
echo.
echo To run the application:
echo 1. Run: venv\Scripts\activate.bat
echo 2. Run: streamlit run app.py
echo.
echo The application will open in your browser at http://localhost:8501
echo.
pause