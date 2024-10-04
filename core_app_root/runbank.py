import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()

# Fetch the secret key from environment variables
secret_key = os.getenv('PRIVATE_PAYSTACK_KEY')
# Fetch the secret key from environment variables


# Define your base URL
base_url = 'https://api.paystack.co'

# Dummy data for serializer.validated_data to simulate request data
# In a real application, replace this with actual data
serializer = {
    'validated_data': {
        'account_number': '0754024784',
        'bank_code': '058'
    }
}

# Define endpoint and parameters
endpoint = '/bank/resolve'
params = {
    'account_number': str(serializer['validated_data']['account_number']),
    'bank_code': str(serializer['validated_data']['bank_code'])
}

# Define headers
headers = {
    'Authorization': f'Bearer {secret_key}'
}

# Make GET request
response = requests.get(f'{base_url}{endpoint}', params=params, headers=headers)

# Check for successful request
if response.status_code == 200:
    data = response.json()
    account_name = data['data']['account_name']
    print(f'Account Name: {account_name}')
else:
    print(f'Failed to resolve bank account: {response.status_code}')
    print(response.text)
