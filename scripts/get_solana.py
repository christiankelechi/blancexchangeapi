import requests

def fetch_solana_fm_tokens(address):
    # Define the Solana FM API endpoint for fetching tokens
    url = f"https://solana.fm/api/v1/address/{address}/tokens?cluster=mainnet-alpha"
    
    # Make a GET request to the API
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")
        return None

# Example usage
address = "4z97Dk9wwsDekxb7cCHQUP5iM5dqU1NJdyxSX6SwPVhu"
tokens_data = fetch_solana_fm_tokens(address)

if tokens_data:
    print(tokens_data)
