import requests
import json
from datetime import datetime

TOKEN = "<your-fbr-sandbox-token>"
headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
current_date = datetime.now().strftime("%Y-%m-%d")

def test_scenario(scenario_id, description, sale_type, buyer_type):
    """Test a specific scenario"""
    print(f"Testing {scenario_id}: {description}")
    
    # Determine correct tax rate and buyer setup
    if 'Services' in sale_type:
        tax_rate = "16%"
        sales_tax = 160.00
    elif 'Reduced' in sale_type:
        tax_rate = "5%"
        sales_tax = 50.00
    elif 'zero-rate' in sale_type or 'Exempt' in sale_type:
        tax_rate = "0%"
        sales_tax = 0.00
    else:
        tax_rate = "18%"
        sales_tax = 180.00
    
    buyer_ntn = "" if buyer_type == 'Unregistered' else "1234567"
    
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
            "productDescription": "Product Description",
            "rate": tax_rate,
            "uoM": "Numbers, pieces, units",
            "quantity": 1.0000,
            "totalValues": 0.00,
            "valueSalesExcludingST": 1000.00,
            "fixedNotifiedValueOrRetailPrice": 0.00,
            "salesTaxApplicable": sales_tax,
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
            
            if status == 'Valid':
                print(f"  SUCCESS! Invoice: {invoice_number}")
                return True, invoice_number
            else:
                error = validation.get('error', 'No error message')
                print(f"  Invalid: {error[:60]}...")
                return False, ""
        else:
            print(f"  HTTP Error: {response.status_code}")
            return False, ""
            
    except Exception as e:
        print(f"  Exception: {str(e)[:40]}...")
        return False, ""

def main():
    print("TESTING ALL SCENARIOS TO COMPLETE FBR REQUIREMENTS")
    print("=" * 70)
    
    # Test key scenarios that should work
    key_scenarios = [
        ("SN002", "Goods at standard rate to unregistered buyers", "Goods at standard rate (default)", "Unregistered"),
        ("SN026", "Sale to End Consumer by retailers", "Goods at standard rate (default)", "Unregistered"),
        ("SN027", "Sale to End Consumer by retailers", "3rd Schedule Goods", "Unregistered"),
        ("SN028", "Sale to End Consumer by retailers", "Goods at Reduced Rate", "Unregistered"),
        ("SN018", "Services (FED in ST Mode) - Unregistered", "Services (FED in ST Mode)", "Unregistered"),
        ("SN019", "Services - Unregistered", "Services", "Unregistered")
    ]
    
    successful_scenarios = []
    
    print("TESTING KEY SCENARIOS:")
    print("-" * 50)
    
    for scenario in key_scenarios:
        success, invoice = test_scenario(*scenario)
        if success:
            successful_scenarios.append(scenario[0])
        print()
    
    # Now test a few registered scenarios to confirm they fail
    print("TESTING REGISTERED SCENARIOS (Expected to fail):")
    print("-" * 50)
    
    registered_scenarios = [
        ("SN001", "Goods at standard rate to registered buyers", "Goods at standard rate (default)", "Registered"),
        ("SN003", "Sale of Steel", "Steel Melting and re-rolling", "Registered"),
        ("SN005", "Reduced rate sale", "Goods at Reduced Rate", "Registered")
    ]
    
    for scenario in registered_scenarios:
        success, invoice = test_scenario(*scenario)
        if success:
            successful_scenarios.append(scenario[0])
        print()
    
    print("=" * 70)
    print("FINAL ANALYSIS:")
    print(f"Working scenarios: {len(successful_scenarios)}")
    print(f"Successful scenarios: {successful_scenarios}")
    
    if len(successful_scenarios) > 0:
        print("\nCONCLUSION:")
        print("- Token is configured for UNREGISTERED buyers only")
        print("- FBR expects ALL 28 scenarios to be completed")
        print("- Current token cannot complete registered buyer scenarios")
        print("\nACTION REQUIRED:")
        print("Contact FBR support immediately:")
        print("1. Token works for unregistered scenarios")
        print("2. Request token reconfiguration for all 28 scenarios")
        print("3. Or clarify if only specific scenarios are assigned")
        print("4. Production token generation is blocked until resolved")
    else:
        print("\nISSUE: No scenarios working - check network/token")

if __name__ == "__main__":
    main()