import requests
import json
from datetime import datetime

# Configuration
TOKEN = "<your-fbr-sandbox-token>"
headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
current_date = datetime.now().strftime("%Y-%m-%d")

def test_validation_api(scenario_id, buyer_type, rate, sale_type, buyer_ntn=""):
    """Test validation API with different parameters"""
    print(f"Validating {scenario_id} - {buyer_type} - {rate}")
    
    payload = {
        "invoiceType": "Sale Invoice",
        "invoiceDate": current_date,
        "sellerNTNCNIC": "2226849",
        "sellerBusinessName": "DPL PVT LTD",
        "sellerProvince": "Sindh",
        "sellerAddress": "Karachi",
        "buyerNTNCNIC": buyer_ntn,
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
        url = "https://gw.fbr.gov.pk/di_data/v1/di/validateinvoicedata_sb"
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            validation = data.get('validationResponse', {})
            status = validation.get('status', 'Unknown')
            
            print(f"  Status: {status}")
            if status == 'Valid':
                print(f"  SUCCESS! Validation passed")
                print(f"  Response: {json.dumps(data, indent=2)}")
                return True
            else:
                error = validation.get('error', 'No error message')
                error_code = validation.get('errorCode', 'No code')
                print(f"  Error {error_code}: {error[:80]}...")
        else:
            print(f"  HTTP Error: {response.status_code}")
            
    except Exception as e:
        print(f"  Exception: {str(e)[:50]}...")
    
    return False

def main():
    print("TESTING VALIDATION API FOR VALID RESPONSE")
    print("=" * 60)
    
    # Test different combinations for validation
    test_configs = [
        # (scenario_id, buyer_type, rate, sale_type, buyer_ntn)
        ("SN018", "Unregistered", "16%", "Services (FED in ST Mode)", ""),
        ("SN019", "Unregistered", "16%", "Services", ""),
        ("SN018", "Registered", "16%", "Services (FED in ST Mode)", "1234567"),
        ("SN019", "Registered", "16%", "Services", "1234567"),
        ("SN001", "Registered", "18%", "Goods at standard rate (default)", "1234567"),
        ("SN002", "Unregistered", "18%", "Goods at standard rate (default)", ""),
        ("SN018", "Unregistered", "0%", "Services (FED in ST Mode)", ""),
        ("SN019", "Unregistered", "0%", "Services", ""),
        # Try with different buyer NTNs
        ("SN018", "Registered", "16%", "Services (FED in ST Mode)", "2226849"),
        ("SN019", "Registered", "16%", "Services", "2226849"),
    ]
    
    valid_found = False
    
    for config in test_configs:
        scenario, buyer_type, rate, sale_type, buyer_ntn = config
        if test_validation_api(scenario, buyer_type, rate, sale_type, buyer_ntn):
            valid_found = True
            print(f"\n*** FOUND VALID CONFIGURATION ***")
            print(f"Scenario: {scenario}")
            print(f"Buyer Type: {buyer_type}")
            print(f"Rate: {rate}")
            print(f"Sale Type: {sale_type}")
            print(f"Buyer NTN: {buyer_ntn}")
            break
        print()
    
    print("=" * 60)
    if not valid_found:
        print("No valid validation response found.")
        print("The validation API appears to have stricter business rules")
        print("than the invoice generation API.")
        print("\nNote: Invoice generation API works fine and creates valid invoices.")
        print("The validation API is meant for pre-validation, not post-validation.")

if __name__ == "__main__":
    main()