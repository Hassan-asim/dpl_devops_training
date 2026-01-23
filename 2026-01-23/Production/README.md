# DPL FBR Digital Invoicing System
## Professional Invoice Submission & Compliance Management

### 🏢 Overview
Professional desktop application for DPL Finance team to submit service invoices to FBR Digital Invoicing system. Supports SN018 (Services with FED in ST Mode) and SN019 (Regular Services) scenarios.

### ✨ Features
- **Professional UI**: Clean, corporate-grade interface
- **Real-time FBR Integration**: Direct API connection to FBR sandbox/production
- **Service Invoice Support**: SN018 and SN019 scenarios
- **Automatic Tax Calculation**: 16% sales tax for services
- **Invoice Validation**: Pre-validate before submission
- **Dashboard & Analytics**: Track submission history and metrics
- **Compliance Ready**: Follows FBR technical specifications

### 🚀 Quick Start

#### Option 1: Automated Setup
1. Double-click `setup.bat` to install dependencies
2. Double-click `run.bat` to start the application
3. Application opens at http://localhost:8501

#### Option 2: Manual Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

### 📋 System Requirements
- Python 3.8 or higher
- Windows 10/11 (for .bat files)
- Internet connection for FBR API
- Modern web browser

### 🔧 Configuration
Edit `.env` file to configure:
- FBR API tokens (sandbox/production)
- Company details (NTN, name, address)
- Environment settings

### 📊 Supported Invoice Types
- **SN018**: Services with Federal Excise Duty in Sales Tax Mode
- **SN019**: Regular Services
- **Tax Rate**: 16% for all services
- **Customer Types**: Registered and Unregistered

### 🛡️ Security Features
- Environment-based configuration
- Secure API token handling
- Input validation and sanitization
- Error handling and logging

### 📱 User Interface
- **Create Invoice**: Submit new service invoices
- **Dashboard**: View analytics and metrics
- **Validate Invoice**: Pre-validate before submission
- **Invoice History**: Track all submissions

### 🔄 Deployment Options
1. **Standalone Desktop**: Run locally on each user's machine
2. **Network Shared**: Install on shared network drive
3. **Web Deployment**: Deploy to internal server for team access

### 📞 Support
- Technical Documentation: `docs details.txt`
- FBR Support: https://dicrm.pral.com.pk/
- Internal Support: Contact IT Department

### 🏷️ Version Information
- **Version**: 1.0.0 MVP
- **Environment**: Sandbox (for testing)
- **Last Updated**: 2026-01-23
- **Status**: Production Ready

### 📄 License
Internal use only - DPL PVT LTD Finance Department