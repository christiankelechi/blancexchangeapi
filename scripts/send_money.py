from tronpy import Tron
from tronpy.keys import PrivateKey

# Initialize Tron client
client = Tron()

# Replace with your private key of the sending address
sender_private_key = "your_private_key_here"

# Create a private key object
priv_key = PrivateKey(bytes.fromhex(sender_private_key))

# Define the sending address and recipient address
sender_address = "6664971ece8d97a8157f3a050272a1af"
recipient_address = "TCvWHrMWhnUU9g3Sth6xUDHUFuoWtpeWpD"

# Define the amount of TRX to send (1.7 TRX)
amount_to_send = 1.7

# Convert the amount to sun (smallest unit of TRX)
amount_in_sun = int(amount_to_send * 1_000_000)

# Create a transaction to transfer TRX
txn = (
    client.trx.transfer(sender_address, recipient_address, amount_in_sun)
    .build()
    .sign(priv_key)
)

# Broadcast the transaction
txn_result = txn.broadcast()

# Output the transaction result
print(f"Transaction result: {txn_result}")
