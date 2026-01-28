import brevo_python
from brevo_python.rest import ApiException
import os
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

def get_brevo_client():
    api_key = os.getenv("BREVO_API_KEY")  # Use consistent naming
    
    if not api_key:
        raise HTTPException(500, detail="Brevo API key not configured")
    
    configuration = brevo_python.Configuration()
    configuration.api_key['api-key'] = api_key
    configuration.api_key['partner-key'] = api_key  # Only if needed
    
    # Create client with configuration
    api_client = brevo_python.ApiClient(configuration)
    
    # Test connection with a simple call
    try:
        account_api = brevo_python.AccountApi(api_client)
        account_api.get_account()  # Test API call
        return account_api
    except ApiException as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Brevo connection failed: {e.reason}"
        )
