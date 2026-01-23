import requests
import json

# Configuration
TOKEN = "<your-fbr-sandbox-token>"
headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

# All possible FBR API endpoints to test
ALL_ENDPOINTS = [
    # Invoice Operations
    "https://gw.fbr.gov.pk/di_data/v1/di/postinvoicedata_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/validateinvoicedata_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/getinvoicedata_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/invoicedetails_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/getinvoicedetails_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/invoiceinfo_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/searchinvoice_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/listinvoices_sb",
    
    # Status and Scenario Operations
    "https://gw.fbr.gov.pk/di_data/v1/di/scenariostatus_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/getstatus_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/checkstatus_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/status_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/scenarios_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/getscenarios_sb",
    
    # Reference Data
    "https://gw.fbr.gov.pk/di_data/v1/di/reference_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/getreference_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/saletypes_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/getsaletypes_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/hscodes_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/gethscodes_sb",
    
    # Token and Auth
    "https://gw.fbr.gov.pk/di_data/v1/di/token_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/gettoken_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/auth_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/authenticate_sb",
    
    # Reports and Analytics
    "https://gw.fbr.gov.pk/di_data/v1/di/reports_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/getreports_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/analytics_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/dashboard_sb",
    
    # User and Profile
    "https://gw.fbr.gov.pk/di_data/v1/di/profile_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/getprofile_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/userinfo_sb",
    "https://gw.fbr.gov.pk/di_data/v1/di/getuserinfo_sb"
]

def test_endpoint(url):
    """Test an endpoint with different HTTP methods and payloads"""
    print(f"Testing: {url}")
    
    # Test payloads
    payloads = [
        {},  # Empty
        {"sellerNTNCNIC": "2226849"},  # Basic seller info
        {"invoiceNumber": "2226849DIABWORY133287", "sellerNTNCNIC": "2226849"},  # Invoice info
        {"scenarioId": "SN018"},  # Scenario info
        {"token": TOKEN}  # Token info
    ]
    
    methods = ["GET", "POST"]
    
    for method in methods:
        for i, payload in enumerate(payloads):
            try:
                if method == "GET":
                    response = requests.get(url, headers=headers, timeout=10)
                else:
                    response = requests.post(url, headers=headers, json=payload, timeout=10)
                
                if response.status_code == 200:
                    print(f"  SUCCESS - {method} with payload {i}: {response.status_code}")
                    try:
                        data = response.json()
                        print(f"  Response: {json.dumps(data, indent=2)[:300]}...")
                    except:
                        print(f"  Response: {response.text[:200]}")
                    return True
                elif response.status_code not in [404, 405, 401]:
                    print(f"  INTERESTING - {method} with payload {i}: {response.status_code}")
                    print(f"  Response: {response.text[:100]}")
                    
            except Exception as e:
                if "timeout" not in str(e).lower():
                    print(f"  ERROR - {method}: {str(e)[:50]}")
    
    return False

def main():
    print("FBR API ENDPOINT DISCOVERY")
    print("=" * 60)
    print(f"Testing {len(ALL_ENDPOINTS)} possible endpoints")
    print("Looking for working APIs beyond the known ones...")
    print()
    
    working_endpoints = []
    interesting_endpoints = []
    
    for i, endpoint in enumerate(ALL_ENDPOINTS, 1):
        print(f"[{i}/{len(ALL_ENDPOINTS)}] ", end="")
        
        if test_endpoint(endpoint):
            working_endpoints.append(endpoint)
        
        print()
    
    print("=" * 60)
    print("DISCOVERY COMPLETED")
    print()
    
    if working_endpoints:
        print("WORKING ENDPOINTS FOUND:")
        for endpoint in working_endpoints:
            print(f"  ✅ {endpoint}")
    else:
        print("❌ No new working endpoints discovered")
    
    print()
    print("KNOWN WORKING ENDPOINTS:")
    print("  ✅ https://gw.fbr.gov.pk/di_data/v1/di/postinvoicedata_sb")
    print("  ✅ https://gw.fbr.gov.pk/di_data/v1/di/validateinvoicedata_sb")
    
    print()
    print("CONCLUSION:")
    print("FBR sandbox appears to have limited API endpoints available.")
    print("Most detail/status APIs are likely production-only.")

if __name__ == "__main__":
    main()