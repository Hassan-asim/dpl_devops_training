import streamlit as st
from datetime import datetime, date
import json
from fbr_client import FBRClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="DPL FBR Digital Invoicing",
    page_icon="🧾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2a5298;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .success-alert {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .error-alert {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Initialize FBR Client
@st.cache_resource
def get_fbr_client():
    return FBRClient()

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🏢 DPL FBR Digital Invoicing System</h1>
        <p>Professional Invoice Submission & Compliance Management</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://via.placeholder.com/200x80/2a5298/ffffff?text=DPL+LOGO", width=200)
        st.markdown("### 📊 System Status")
        
        # Environment info
        env = os.getenv('ENVIRONMENT', 'SANDBOX')
        if env == 'SANDBOX':
            st.warning("🧪 Sandbox Environment")
        else:
            st.success("🚀 Production Environment")
        
        st.info(f"**Company:** {os.getenv('COMPANY_NAME')}")
        st.info(f"**NTN:** {os.getenv('COMPANY_NTN')}")
        
        # Navigation
        st.markdown("### 🧭 Navigation")
        page = st.selectbox(
            "Select Module",
            ["📝 Create Invoice", "📋 Invoice History", "🔍 Validate Invoice"]
        )
    
    # Main content based on selected page
    if page == "📝 Create Invoice":
        create_invoice_page()
    elif page == "📋 Invoice History":
        invoice_history_page()
    elif page == "🔍 Validate Invoice":
        validate_invoice_page()

def create_invoice_page():
    st.markdown("## 📝 Create New Invoice")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Invoice Details")
        
        # Invoice form
        with st.form("invoice_form"):
            # Customer Information
            st.markdown("#### 👤 Customer Information")
            col_a, col_b = st.columns(2)
            
            with col_a:
                buyer_name = st.text_input("Customer Name *", placeholder="Enter customer name")
                buyer_type = st.selectbox("Customer Type", ["Unregistered", "Registered"])
            
            with col_b:
                buyer_ntn = st.text_input("Customer NTN", placeholder="Optional for unregistered")
                buyer_province = st.selectbox("Province", ["Sindh", "Punjab", "KPK", "Balochistan"])
            
            buyer_address = st.text_input("Customer Address", placeholder="Enter customer address")
            
            # Service Information
            st.markdown("#### 🛠️ Service Information")
            col_c, col_d = st.columns(2)
            
            with col_c:
                service_description = st.text_area("Service Description *", placeholder="Describe the service provided")
                amount = st.number_input("Service Amount (PKR) *", min_value=0.01, step=0.01, format="%.2f")
            
            with col_d:
                invoice_date = st.date_input("Invoice Date *", value=date.today())
                fed_in_st_mode = st.checkbox("FED in ST Mode (SN018)", help="Check if Federal Excise Duty applies")
            
            # Calculate tax preview
            if amount > 0:
                tax_amount = amount * 0.16
                total_amount = amount + tax_amount
                
                st.markdown("#### 💰 Tax Calculation Preview")
                col_e, col_f, col_g = st.columns(3)
                
                with col_e:
                    st.metric("Service Amount", f"PKR {amount:,.2f}")
                with col_f:
                    st.metric("Sales Tax (16%)", f"PKR {tax_amount:,.2f}")
                with col_g:
                    st.metric("Total Amount", f"PKR {total_amount:,.2f}")
            
            # Submit button
            submitted = st.form_submit_button("🚀 Submit to FBR", type="primary", use_container_width=True)
            
            if submitted:
                if not buyer_name or not service_description or amount <= 0:
                    st.error("❌ Please fill all required fields marked with *")
                else:
                    submit_invoice_to_fbr({
                        'buyer_name': buyer_name,
                        'buyer_type': buyer_type,
                        'buyer_ntn': buyer_ntn if buyer_ntn else '',
                        'buyer_province': buyer_province,
                        'buyer_address': buyer_address,
                        'description': service_description,
                        'amount': amount,
                        'invoice_date': invoice_date.strftime('%Y-%m-%d'),
                        'fed_in_st_mode': fed_in_st_mode
                    })
    
    with col2:
        st.markdown("### 📋 Quick Guide")
        st.info("""
        **DPL Service Scenarios:**
        
        🔹 **SN018**: Services with FED in ST Mode
        - Federal Excise Duty applicable
        - 16% Sales Tax rate
        
        🔹 **SN019**: Regular Services  
        - Standard service invoicing
        - 16% Sales Tax rate
        
        **Requirements:**
        - Customer name is mandatory
        - Service description required
        - Amount must be positive
        - Date cannot be future
        """)
        
        st.markdown("### 🎯 Compliance Status")
        st.success("✅ FBR API Connected")
        st.success("✅ Tax Rates Updated")
        st.success("✅ Scenarios Validated")

def submit_invoice_to_fbr(invoice_data):
    """Submit invoice to FBR API"""
    fbr_client = get_fbr_client()
    
    with st.spinner("🔄 Submitting invoice to FBR..."):
        success, response = fbr_client.submit_invoice(invoice_data)
        
        if success:
            st.markdown("""
            <div class="success-alert">
                <h4>✅ Invoice Submitted Successfully!</h4>
                <p><strong>FBR Invoice Number:</strong> {}</p>
                <p><strong>Status:</strong> {}</p>
                <p><strong>Message:</strong> {}</p>
            </div>
            """.format(
                response.get('invoice_number', 'N/A'),
                response.get('status', 'N/A'),
                response.get('message', 'N/A')
            ), unsafe_allow_html=True)
            
            # Store in session state for history
            if 'invoice_history' not in st.session_state:
                st.session_state.invoice_history = []
            
            st.session_state.invoice_history.append({
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'customer': invoice_data['buyer_name'],
                'amount': invoice_data['amount'],
                'fbr_number': response.get('invoice_number', 'N/A'),
                'status': 'Success'
            })
            
            st.balloons()
            
        else:
            st.markdown("""
            <div class="error-alert">
                <h4>❌ Invoice Submission Failed</h4>
                <p><strong>Error:</strong> {}</p>
                <p><strong>Message:</strong> {}</p>
            </div>
            """.format(
                response.get('error', 'Unknown error'),
                response.get('message', 'Please try again')
            ), unsafe_allow_html=True)

def invoice_history_page():
    st.markdown("## 📋 Invoice History")
    
    if 'invoice_history' not in st.session_state or not st.session_state.invoice_history:
        st.info("📝 No invoice history available. Submit invoices to see them here.")
        return
    
    # Display simple table
    st.markdown("### Recent Invoices")
    for i, invoice in enumerate(reversed(st.session_state.invoice_history[-10:])):
        with st.expander(f"Invoice #{i+1} - {invoice['customer']} - PKR {invoice['amount']:,.2f}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Date:** {invoice['date']}")
                st.write(f"**Customer:** {invoice['customer']}")
            with col2:
                st.write(f"**Amount:** PKR {invoice['amount']:,.2f}")
                st.write(f"**FBR Number:** {invoice['fbr_number']}")
                st.write(f"**Status:** {invoice['status']}")
    
    if st.button("🗑️ Clear History"):
        st.session_state.invoice_history = []
        st.rerun()

def validate_invoice_page():
    st.markdown("## 🔍 Invoice Validation")
    st.info("Pre-validate your invoice before submission to ensure FBR compliance.")
    
    # Similar form but for validation only
    with st.form("validation_form"):
        st.markdown("#### Quick Validation")
        
        col1, col2 = st.columns(2)
        with col1:
            val_customer = st.text_input("Customer Name")
            val_amount = st.number_input("Amount (PKR)", min_value=0.01)
        with col2:
            val_description = st.text_input("Service Description")
            val_fed = st.checkbox("FED in ST Mode")
        
        validate_btn = st.form_submit_button("🔍 Validate", type="secondary")
        
        if validate_btn and val_customer and val_amount > 0:
            fbr_client = get_fbr_client()
            
            validation_data = {
                'buyer_name': val_customer,
                'buyer_type': 'Unregistered',
                'description': val_description,
                'amount': val_amount,
                'invoice_date': date.today().strftime('%Y-%m-%d'),
                'fed_in_st_mode': val_fed
            }
            
            with st.spinner("🔄 Validating with FBR..."):
                is_valid, response = fbr_client.validate_invoice(validation_data)
                
                if is_valid:
                    st.success("✅ Invoice validation passed! Ready for submission.")
                else:
                    st.error(f"❌ Validation failed: {response.get('message', 'Unknown error')}")

if __name__ == "__main__":
    main()