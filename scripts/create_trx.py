from tronpy import Tron
client = Tron()
# current_block=client.get_latest_block_number()
# print(current_block)
# current_block_id=client.get_latest_block_id()
# print(current_block_id)
# client.get_account_balance('TTzPiwbBedv7E8p4FkyPyeqq4RVoqRL3TW')

# client.get_account_asset_balance('TCrahg7N9cB1SwN21WzVMqxCptbRdvQata', 1002928)
# 989937719235000000


current_address=client.generate_address()
print(current_address)