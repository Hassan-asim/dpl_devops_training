import requests
import json
from datetime import datetime
from typing import Dict, Any, Tuple
import os
from dotenv import load_dotenv

load_dotenv()

class FBRClient:
    """Professional FBR API Client for DPL Digital Invoicing"""
    
    def __init__(self):
        self.token = os.getenv('FBR_SANDBOX_TOKEN')
        self.post_url = os.getenv('FBR_SANDBOX_URL')
        self.validate_url = os.getenv('FBR_VALIDATE_URL')
        self.company_ntn = os.getenv('COMPANY_NTN')
        self.company_name = os.getenv('COMPANY_NAME')
        self.company_province = os.getenv('COMPANY_PROVINCE')
        self.company_address = os.getenv('COMPANY_ADDRESS')
        
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
    
    def create_service_invoice(self, invoice_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create FBR compliant service invoice (SN018/SN019)"""
        
        # Determine scenario and sale type
        if invoice_data.get('fed_in_st_mode', False):
            scenario_id = "SN018"
            sale_type = "Services (FED in ST Mode)"
        else:
            scenario_id = "SN019"
            sale_type = "Services"
        
        # Calculate tax (16% for services)
        amount = float(invoice_data['amount'])
        tax_rate = 16.0
        sales_tax = round(amount * (tax_rate / 100), 2)
        total_amount = amount + sales_tax
        
        fbr_invoice = {
            "invoiceType": "Sale Invoice",
            "invoiceDate": invoice_data['invoice_date'],
            "sellerNTNCNIC": self.company_ntn,
            "sellerBusinessName": self.company_name,
            "sellerProvince": self.company_province,
            "sellerAddress": self.company_address,
            "buyerNTNCNIC": invoice_data.get('buyer_ntn', ''),
            "buyerBusinessName": invoice_data['buyer_name'],
            "buyerProvince": invoice_data.get('buyer_province', 'Sindh'),
            "buyerAddress": invoice_data.get('buyer_address', 'Karachi'),
            "buyerRegistrationType": invoice_data.get('buyer_type', 'Unregistered'),
            "invoiceRefNo": "",
            "scenarioId": scenario_id,
            "items": [{
                "hsCode": "9802.0000",  # Services HS Code
                "productDescription": invoice_data['description'],
                "rate": f"{tax_rate}%",
                "uoM": "Numbers, pieces, units",
                "quantity": 1.0000,
                "totalValues": total_amount,
                "valueSalesExcludingST": amount,
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
        
        return fbr_invoice
    
    def submit_invoice(self, invoice_data: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        """Submit invoice to FBR and return success status and response"""
        try:
            fbr_invoice = self.create_service_invoice(invoice_data)
            
            response = requests.post(
                self.post_url,
                headers=self.headers,
                json=fbr_invoice,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                validation = data.get('validationResponse', {})
                status = validation.get('status', 'Unknown')
                
                if status == 'Valid':
                    return True, {
                        'success': True,
                        'invoice_number': data.get('invoiceNumber', ''),
                        'status': status,
                        'message': 'Invoice submitted successfully to FBR',
                        'fbr_response': data
                    }
                else:
                    return False, {
                        'success': False,
                        'status': status,
                        'error': validation.get('error', 'Unknown error'),
                        'message': 'Invoice validation failed',
                        'fbr_response': data
                    }
            else:
                return False, {
                    'success': False,
                    'error': f"HTTP {response.status_code}",
                    'message': 'Failed to connect to FBR API',
                    'response_text': response.text
                }
                
        except Exception as e:
            return False, {
                'success': False,
                'error': str(e),
                'message': 'System error occurred'
            }
    
    def validate_invoice(self, invoice_data: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        """Validate invoice with FBR before submission"""
        try:
            fbr_invoice = self.create_service_invoice(invoice_data)
            
            response = requests.post(
                self.validate_url,
                headers=self.headers,
                json=fbr_invoice,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                validation = data.get('validationResponse', {})
                status = validation.get('status', 'Unknown')
                
                return status == 'Valid', {
                    'status': status,
                    'message': 'Validation completed',
                    'fbr_response': data
                }
            else:
                return False, {
                    'error': f"HTTP {response.status_code}",
                    'message': 'Validation API error'
                }
                
        except Exception as e:
            return False, {
                'error': str(e),
                'message': 'Validation system error'
            }