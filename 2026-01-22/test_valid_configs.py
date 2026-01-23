import requests
import json
from datetime import datetime

# Configuration
TOKEN = "<your-fbr-sandbox-token>"
headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
current_date = datetime.now().strftime("%Y-%m-%d")

def test_invoice_generation(scenario_id, buyer_type, rate, sale_type):
    """Test invoice generation with different parameters"""
    print(f"Testing {scenario_id} - {buyer_type} - {rate} - {sale_type}")
    
    payload = {
        "invoiceType": "Sale Invoice",
        "invoiceDate": current_date,
        "sellerNTNCNIC": "2226849",
        "sellerBusinessName": "DPL PVT LTD",
        "sellerProvince": "Sindh",
        "sellerAddress": "Karachi",
        "buyerNTNCNIC": "" if buyer_type == "Unregistered" else "1234567",
        "buyerBusinessName": "Test Customer",
        "buyerProvince": "Sindh",
        "buyerAddress": "Karachi",
        "buyerRegistrationType": buyer_type,
        "invoiceRefNo": "",
        "scenarioId": scenario_id,
        "items": [{
            "hsCode": "0101.2100",
            "productDescription": "Services Description",
            "rate": rate,
            "uoM": "Numbers, pieces, units",
            "quantity": 1.0000,
            "totalValues": 0.00,
            "valueSalesExcludingST": 1000.00,
            "fixedNotifiedValueOrRetailPrice": 0.00,
            "salesTaxApplicable": 160.00 if rate == "16%" else 0.00,
            "salesTaxWithheldAtSource": 0.00,
            "extraTax": 0.00,
            "furtherTax": 0.00,
            "sroScheduleNo": "",
            "fedPayable": 0.00,
            "discount": 0.00,
            "saleType": sale_type,
            "sroItemSerialNo": ""
        }]
    }
    
    try:
        url = "https://gw.fbr.gov.pk/di_data/v1/di/postinvoicedata_sb"
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            validation = data.get('validationResponse', {})
            status = validation.get('status', 'Unknown')
            invoice_number = data.get('invoiceNumber', '')
            
            print(f"  Status: {status}")
            if status == 'Valid':
                print(f"  SUCCESS! Invoice: {invoice_number}")
                return invoice_number
            else:
                error = validation.get('error', 'No error message')
                print(f"  Error: {error[:100]}...")
        else:
            print(f"  HTTP Error: {response.status_code}")
            
    except Exception as e:
        print(f"  Exception: {str(e)[:50]}...")
    
    return None

def main():
    print("TESTING DIFFERENT CONFIGURATIONS FOR VALID INVOICE")
    print("=" * 60)
    
    # Test different combinations
    test_configs = [
        # (scenario_id, buyer_type, rate, sale_type)
        ("SN018", "Unregistered", "16%", "Services (FED in ST Mode)"),
        ("SN019", "Unregistered", "16%", "Services"),
        ("SN018", "Registered", "16%", "Services (FED in ST Mode)"),
        ("SN019", "Registered", "16%", "Services"),
        ("SN001", "Unregistered", "18%", "Goods at standard rate (default)"),
        ("SN002", "Unregistered", "18%", "Goods at standard rate (default)"),
        ("SN018", "Unregistered", "0%", "Services (FED in ST Mode)"),
        ("SN019", "Unregistered", "0%", "Services"),
    ]
    
    valid_invoices = []
    
    for config in test_configs:
        invoice_number = test_invoice_generation(*config)
        if invoice_number:
            valid_invoices.append((config, invoice_number))
        print()
    
    print("=" * 60)
    print("RESULTS:")
    
    if valid_invoices:
        print("VALID INVOICES GENERATED:")
        for config, invoice_number in valid_invoices:
            scenario, buyer, rate, sale_type = config
            print(f"  {scenario} ({buyer}, {rate}): {invoice_number}")
    else:
        print("No valid invoices generated with current token configuration")
        print("Token appears to be restricted to specific business scenarios only")

if __name__ == "__main__":
    main()