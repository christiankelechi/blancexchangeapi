from web3 import Web3

# Connect to BSC Mainnet
bsc_mainnet = "https://bsc-dataseed.binance.org/"
w3 = Web3(Web3.HTTPProvider(bsc_mainnet))

# Check if connected successfully
if w3.is_connected():
    print("Connected to BSC Mainnet")

# Example: Get transaction details by hash
tx_hash = '0x24EC9efdAD7E305b41a09C2c9DDaC7aD10D891fa'  # Replace with your transaction hash
tx = w3.eth.get_transaction(tx_hash)
print(tx)
