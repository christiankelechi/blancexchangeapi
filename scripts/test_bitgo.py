import os
from bitgo.v2 import BitGo  # Make sure your script is not named `bitgo.py`

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure BitGo environment and access token
bitgo_detail = BitGo(
    env='prod',  # Use 'prod' for Mainnet
    access_token="v2xf652aa6d346ebbc9d54526204c6b125fd71113bfa42c27dd200146984c59f557"  # Replace with your mainnet access token
)

# Define the coins and wallet IDs
trx_coin = 'trx'
sol_coin = 'sol'
trx_wallet_id = "6664971ece8d97a8157f3a050272a1af"
sol_wallet_id = "6664856273d52dc3802e3819058026b4"

def get_wallet_transfers(coin, wallet_id):
    try:
        # Get wallet instance
        wallet_instance = bitgo_detail.coin(coin).wallets().get(wallet_id)
        
        # Fetch transfers from the wallet
        transfers = wallet_instance.transfers()

        # Print transfers
        print(f"Transfers for {coin} wallet ID {wallet_id}:")
        print(transfers)
    except Exception as e:
        print(f"An error occurred while fetching transfers for {coin}: {e}")

def main():
    # Fetch transfers for TRX20 wallet
    get_wallet_transfers(trx_coin, trx_wallet_id)
    
    # Fetch transfers for Solana wallet
    get_wallet_transfers(sol_coin, sol_wallet_id)

if __name__ == "__main__":
    main()
