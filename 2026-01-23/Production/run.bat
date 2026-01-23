@echo off
echo ========================================
echo Starting DPL FBR Digital Invoicing System
echo ========================================

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting Streamlit application...
echo Application will open in your browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

streamlit run app.py --server.port 8501 --server.address localhost