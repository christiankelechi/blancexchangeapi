# from web3 import Web3
# from eth_account import Account
# # Connect to BNB Chain Mainnet
# bsc_mainnet = "https://bsc-dataseed.binance.org/"
# w3 = Web3(Web3.HTTPProvider(bsc_mainnet))

# # Check if connected successfully
# print("Connected to BNB Chain:", w3.is_connected())
# # Generate a new Ethereum account (BEP-20 is compatible with Ethereum addresses)
# account = Account.create()

# # Display the address and private key
# print(f"New wallet address: {account.address}")
# print(f"Private key: {account._private_key.hex()}")
from web3 import Web3
from eth_account import Account

# Connect to BNB Chain Mainnet
bsc_mainnet = "https://bsc-dataseed.binance.org/"
w3 = Web3(Web3.HTTPProvider(bsc_mainnet))

# Check if connected successfully
print("Connected to BNB Chain:", w3.is_connected())

# Generate a new Ethereum-compatible account (BEP-20 uses the same format)
account = Account.create()

# Extract the private key and address
private_key = account._private_key.hex()
address = account.address

# Generate the public key from the private key
public_key = Account.from_key(private_key).key.hex()

# Display the wallet information
print(f"New Wallet Address: {address}")
print(f"Private Key: {private_key}")
print(f"Public Key: {public_key}")
