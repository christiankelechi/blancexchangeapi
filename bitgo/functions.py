import os
from django.conf import settings
from bitgo.models import Address
from .bitgo_base import BitGo
import qrcode
# from pycoin.symbols.tether import network


def create_addresses(profile):
    Address.initialise_addresses(profile)
    

def fetch_deposits(profile):
    
    bitgo = BitGo()
    addresses = profile.addresses.all()

    deposits = []
    for address in addresses:
        response = bitgo.get_transactions(f'{address._type}:usdt', wallet_id=address.wallet, address=address.address)
        print(response)
        
        
        for transfer in response['transfers']:
            try:
                data = {}
                data['transaction_id'] = transfer['id']
                data['amount'] = (int(transfer['baseValueWithoutFees']) - int(transfer['feeString']) - int(transfer['payGoFee'])) / 10**6
                data['address'] = address
                data['comment'] = transfer.get('comment')
                data['status'] = transfer.get('state')
                data['date'] = transfer.get('date')
                

                deposits.append(data)
            except Exception as e: 
                print('error in fetch_deposits:', e)
                continue
    return deposits    

def update_comment(txn):
    bitgo = BitGo()
    bitgo.update_comment(txn.address._type,txn.address.wallet,txn.transaction_id)





def generate_qr_code(address):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(address)
    qr.make(fit=True)

    qr_code_img = qr.make_image(fill_color="black", back_color="white")

    name = os.path.abspath(os.path.join('files',f"{address}.png"))
    qr_code_img.save(name)
    return name
