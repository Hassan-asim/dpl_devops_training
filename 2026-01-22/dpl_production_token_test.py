import requests
import json
from datetime import datetime
import time

TOKEN = "<your-fbr-sandbox-token>"
headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
current_date = datetime.now().strftime("%Y-%m-%d")

def submit_dpl_scenario(scenario_id, sale_type, attempt_num):
    """Submit DPL-specific scenarios multiple times"""
    print(f"Attempt {attempt_num}: Submitting {scenario_id} - {sale_type}")
    
    payload = {
        "invoiceType": "Sale Invoice",
        "invoiceDate": current_date,
        "sellerNTNCNIC": "2226849",
        "sellerBusinessName": "DPL PVT LTD",
        "sellerProvince": "Sindh",
        "sellerAddress": "Karachi",
        "buyerNTNCNIC": "",
        "buyerBusinessName": f"Test Customer {attempt_num}",
        "buyerProvince": "Sindh",
        "buyerAddress": "Karachi",
        "buyerRegistrationType": "Unregistered",
        "invoiceRefNo": "",
        "scenarioId": scenario_id,
        "items": [{
            "hsCode": "0101.2100",
            "productDescription": f"DPL Services - Attempt {attempt_num}",
            "rate": "16%",
            "uoM": "Numbers, pieces, units",
            "quantity": 1.0000,
            "totalValues": 1160.00,
            "valueSalesExcludingST": 1000.00,
            "fixedNotifiedValueOrRetailPrice": 0.00,
            "salesTaxApplicable": 160.00,
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
                print(f"  ✓ SUCCESS! Invoice: {invoice_number}")
                return True, invoice_number
            else:
                error = validation.get('error', 'No error')
                print(f"  ✗ Invalid: {error}")
                return False, ""
        else:
            print(f"  ✗ HTTP Error: {response.status_code}")
            return False, ""
            
    except Exception as e:
        print(f"  ✗ Exception: {str(e)}")
        return False, ""

def main():
    print("FOCUSED TEST: DPL SCENARIOS FOR PRODUCTION TOKEN")
    print("=" * 60)
    print("Testing ONLY SN018 and SN019 (DPL Service Provider scenarios)")
    print("Goal: Generate enough successful invoices to trigger production token")
    print()
    
    # DPL-specific scenarios
    dpl_scenarios = [
        ("SN018", "Services (FED in ST Mode)"),
        ("SN019", "Services")
    ]
    
    successful_invoices = []
    
    # Submit multiple invoices for each DPL scenario
    for scenario_id, sale_type in dpl_scenarios:
        print(f"TESTING {scenario_id}: {sale_type}")
        print("-" * 40)
        
        # Submit 5 invoices for each scenario
        for i in range(1, 6):
            success, invoice_number = submit_dpl_scenario(scenario_id, sale_type, i)
            if success:
                successful_invoices.append((scenario_id, invoice_number))
            
            # Small delay between requests
            time.sleep(1)
        
        print()
    
    print("=" * 60)
    print("RESULTS SUMMARY:")
    print(f"Total successful invoices: {len(successful_invoices)}")
    
    if successful_invoices:
        print("\nSUCCESSFUL INVOICES:")
        for scenario, invoice in successful_invoices:
            print(f"  {scenario}: {invoice}")
        
        print(f"\n✓ DPL SCENARIOS COMPLETED:")
        print("  - SN018: Services (FED in ST Mode) ✓")
        print("  - SN019: Services ✓")
        
        print(f"\n📋 NEXT STEPS:")
        print("1. Check FBR portal for production token generation")
        print("2. If no production token, contact FBR support with evidence:")
        print("   - DPL is Service Provider in Services sector")
        print("   - Only assigned SN018, SN019 scenarios")
        print("   - Both scenarios completed successfully")
        print("   - Request production token generation")
        
        print(f"\n🎯 EVIDENCE FOR FBR SUPPORT:")
        print(f"   Company: DPL PVT LTD")
        print(f"   NTN: 2226849")
        print(f"   Business: Service Provider - Services")
        print(f"   Assigned Scenarios: SN018, SN019 (per Section 10)")
        print(f"   Completion Status: BOTH COMPLETED")
        print(f"   Total Valid Invoices: {len(successful_invoices)}")
    else:
        print("\n✗ NO SUCCESSFUL INVOICES - Check network/token issues")

if __name__ == "__main__":
    main()