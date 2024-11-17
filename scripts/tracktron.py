import requests

# TronScan API endpoint to fetch transactions for a specific address
TRONSCAN_API_URL = "https://apilist.tronscan.org/api/transaction"

# Replace with your TRX wallet address
wallet_address = "TW7zoR4rau8NcbFWRMujJRZdGWvdj3iL3a"

# Function to fetch transactions for a wallet address
def fetch_tron_transactions(wallet_address):
    params = {
        "address": wallet_address,
        "limit": 10,  # Number of transactions to fetch, you can modify this value
        "sort": "-timestamp"  # Sort by latest transactions
    }

    try:
        response = requests.get(TRONSCAN_API_URL, params=params)
        if response.status_code == 200:
            transactions = response.json().get('data', [])
            return transactions
        else:
            print(f"Error: Unable to fetch transactions. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Fetch and display transactions
transactions = fetch_tron_transactions(wallet_address)

if transactions:
    for tx in transactions:
        print(f"Transaction ID: {tx['hash']}")
        print(f"Block: {tx['block']}")
        print(f"Timestamp: {tx['timestamp']}")
        print(f"Amount: {tx['amount']}")
        print(f"From: {tx['ownerAddress']}")
        print(f"To: {tx['toAddress']}")
        print('-' * 40)
else:
    print("No transactions found or an error occurred.")
