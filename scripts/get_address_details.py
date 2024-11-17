import requests

def fetch_tron_address_details(address):
    url = f"https://apilist.tronscan.org/api/account?address={address}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch details. Status Code: {response.status_code}")
        return None
# {'base58check_address': 'TCvWHrMWhnUU9g3Sth6xUDHUFuoWtpeWpD', 'hex_address': '4120658fe1c6c0c6d14a7f00efdf0250353aa09bb5', 'private_key': '9594b56c4a038d9201e2a4515fbb193dc5010db99ba607f0d79d118ff3e85558', 'public_key': '212bde68fcd7f0ca65bfab9aad9c2a4e2ecb71b74ed2436aae7916ae0e8028d316b5c8f6e3b761b7875199460553c188155f5fcf20667f4b0f4f03be20065172'}
# Example usage:
tron_address = "TCvWHrMWhnUU9g3Sth6xUDHUFuoWtpeWpD"
details = fetch_tron_address_details(tron_address)

if details:
    print(details)
