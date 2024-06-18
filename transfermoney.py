import requests
import json

# Set the necessary variables
base_api_url = "https://api.flutterwave.com/v3"  # Replace with your actual base API URL if different
endpoint = "/transfers"
url = f"{base_api_url}{endpoint}"
api_key = "FLWSECK-f51de43c83b002fcdf43c831c06e08f8-1902546945avt-X"  # Replace with your actual API key


# Define the transfer data
transfer_data = {
    "account_bank": "058",
    "account_number": "0754024784",
    "amount": 100,
    "narration": "good",
    "currency": "NGN",
    "debit_currency": "NGN"
}

# Define the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(transfer_data))

# Handle the response
if response.status_code == 200:
    print("Transfer initiated successfully!")
    print(response.json())
else:
    print(f"Failed to initiate transfer: {response.status_code}")
    print(response.json())
