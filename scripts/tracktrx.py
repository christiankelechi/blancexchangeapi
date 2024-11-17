import requests

# Example response data (assuming this is what you've got)
response_data = {
    'trc20token_balances': [{
        'tokenId': 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t', 
        'balance': '1700979', 
        'tokenName': 'Tether USD', 
        'tokenAbbr': 'USDT', 
        'tokenDecimal': 6, 
        'tokenCanShow': 1, 
        'tokenType': 'trc20', 
        'tokenLogo': 'https://static.tronscan.org/production/logo/usdtlogo.png', 
        'vip': True, 
        'tokenPriceInTrx': 6.24280854884764, 
        'amount': 10.61888624261031, 
        'nrOfTokenHolders': 53769912, 
        'transferCount': 2044334976
    }],
    'transactions_in': 1,
    'transactions_out': 0,
    'address': 'TW7zoR4rau8NcbFWRMujJRZdGWvdj3iL3a',
    'transactions': 1,
}

# Function to fetch transaction details
def fetch_transaction_details(transaction_id):
    TRON_API_URL = "https://apilist.tronscan.org/api/"
    # Assuming the transaction endpoint is /transaction/{transaction_id}
    tx_url = f"{TRON_API_URL}transaction/{transaction_id}"
    response = requests.get(tx_url)

    if response.status_code == 200:
        transaction_data = response.json()
        return transaction_data
    else:
        print(f"Failed to fetch transaction details. Status Code: {response.status_code}")
        return None

# Function to get the latest transaction ID for the given address
def get_latest_transaction_id(address):
    TRON_API_URL = "https://apilist.tronscan.org/api/"
    # Fetch transactions for the address
    transactions_url = f"{TRON_API_URL}transaction?address={address}&limit=1"
    response = requests.get(transactions_url)

    if response.status_code == 200:
        transactions_data = response.json()
        if transactions_data['data']:  # Check if there are any transactions
            return transactions_data['data'][0]['txID']  # Adjust this if the structure is different
        else:
            print("No transactions found for this address.")
            return None
    else:
        print(f"Failed to fetch transactions. Status Code: {response.status_code}")
        return None

# Get the latest transaction ID for the specified address
first_transaction_id = get_latest_transaction_id(response_data['address'])

# Fetching transaction details if a transaction ID was found
if first_transaction_id:
    transaction_details = fetch_transaction_details(first_transaction_id)

    # Print the transaction details
    if transaction_details:
        print(transaction_details)
    else:
        print("No transaction details found.")
else:
    print("No transaction ID found.")
