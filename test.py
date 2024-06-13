
import json
import requests

bitgo_access_token = 'v2x2031d89d2b3db163ec8c97b0c363c828231cd0f60bb171aef317af53aba8efb1'


class BitGo:

    def __init__(self, production=True):
        self.access_token = bitgo_access_token
        self.production=production
        
        if production:
            self.url = 'http://www.bitgo.com/api/v2'
            self.express_url = 'http://0.0.0.0:4000/api/v2'
        else:
            # self.url = settings.BITGO_TEST_URL
            self.express_url = 'http://0.0.0.0:3080/api/v2'

    def ping_express(self):
        r = requests.get(self.express_url + '/pingexpress', headers={
          'Authorization': 'Bearer %s' % self.access_token,
        })
        print(self.express_url + '/pingexpress')
        
        if r.status_code != 200:
            raise Exception('pinging express didnt work\n %s' % r.content)
        
        return r.json()
    

    def generate_wallet_exppress(self, coin):
        url = "%s/%s/wallet/generate" % (
                self.express_url,
                coin,
            )
        # payload = {
        #     "label": "Express Generated trx Wallet",
        #     "passphrase": "passphrase123456789",
        #     "enterprise": "663b3119e13a623a0ca95e689d91d4cb",
        #     "disableTransactionNotifications": True,
        #     "disableKRSEmail": True
        #     }
        payload = {
            "label": f"Express Generated {coin} Wallet",
            "multisigType": "tss",
            "type": "hot",
            "passphrase": "emminence",
            "enterprise": "663b3119e13a623a0ca95e689d91d4cb",
            "disableTransactionNotifications": True,
            "disableKRSEmail": True,
            "originalPasscodeEncryptionCode": "emminence"
        }        
        
        r = requests.post(url,
                          json=payload, 
                          headers={ 'Authorization': 'Bearer %s' % self.access_token,}
                          )
        if r.status_code != 200:
            raise Exception('unable to create wallet\n %s' % r.content)
        
        return r.json()
    
    def get_wallets(self):

        r = requests.get(self.url + '/wallets', headers={
          'Authorization': 'Bearer %s' % self.access_token,
        })

        return r.json()

    def get_wallet(self,coin, wallet_id):
        r = requests.get(self.url + f'/{coin}/wallet/' + wallet_id, headers={
          'Authorization': 'Bearer %s' % self.access_token,
        })
        return r.json()

    def get_balance(self, wallet_id, confirmations=0):
        r = requests.get(self.url + '/wallet/%s/unspents' % wallet_id, headers={
          'Authorization': 'Bearer %s' % self.access_token,
        })

        balance = 0
        for tx in r.json()['unspents']:
            if tx['confirmations'] >= confirmations:
                balance += tx['value']

        return balance

    def get_keychain(self, xpub):
        r = requests.post(self.url + '/keychain/%s' % xpub, headers={
          'Authorization': 'Bearer %s' % self.access_token,
        })
        return r.json()


    def get_unspents(self, wallet_id):
        r = requests.get(self.url + '/wallet/%s/unspents' % wallet_id, headers={
          'Authorization': 'Bearer %s' % self.access_token,
        })
        return r.json()

    
    def create_address(self,coin, wallet_id, chain=0):
        """
        :param wallet_id: the wallet id :P
        :param chain: 0 for main or 1 change
        :return:
        """
        create_url = "%s/%s/wallet/%s/address/" % (
                self.url,
                coin,
                wallet_id
            )

        r = requests.post(create_url,
                          json={"chain": chain, "label": "my address ttrx:usdt 1",}, 
                          headers={ 'Authorization': 'Bearer %s' % self.access_token,}
                          )
        
        if r.status_code != 200:
            raise Exception('unable to create address\n %s' % r.content)
        return r.json()

    def list_keys(self, coin):
        r = requests.get(self.url + '/%s/key' % coin, headers={
          'Authorization': 'Bearer %s' % self.access_token,
        })
        return r.json()
    
    
    
    def get_gpg_pubs(self, coin):
        r = requests.get(self.url + '/%s/tss/pubkey' % coin, headers={
          'Authorization': 'Bearer %s' % self.access_token,
        })
        return r.json()

    def create_key_express(self,coin):
        url = self.express_url + '/%s/keychain/local' % coin
        print(url)
        r = requests.post(url, headers={
          'Authorization': 'Bearer %s' % self.access_token,
        })
        return r.json() 
    
    def create_key(self, coin):
        url = self.url + '/%s/key' % coin
        payload = {
                    "source": "bitgo",
                    "enterprise": "65e40cd5e88a23df811fefe479ca3e18",
                    "pub": "xpub661MyMwAqRbcFVj15qMTefxcmpQVhahYRB6GKaEWwn24LxwuwmAMBbp9ZYhEK1bakaxq4AyXYmohpiea8jun5rBDne39P2XKboLTvYUYW95",
                    "type": "ttrx"
                 }
        r = requests.post(url,
                          json=payload, 
                          headers={ 'Authorization': 'Bearer %s' % self.access_token,}
                          )
        if r.status_code != 200:
            raise Exception('unable to create address\n %s' % r.content)
        return r.json()
    
    def get_enterprise(self, id):
        r = requests.get(self.url + '/enterprise/%s' % id, headers={
          'Authorization': 'Bearer %s' % self.access_token,
        })
        return r.json()
    
    def get_transactions(self,coin, wallet_id, address=None):
        url = self.url + f'/{coin}/wallet/' + wallet_id +'/transfer'

        if address:
            url += f'?address={address}&type=receive&state=confirmed'

        r = requests.get(url, headers={
          'Authorization': 'Bearer %s' % self.access_token,
        })
        return r.json()
    
    def update_comment(self, coin, wallet_id, transfer_id):
        url = self.url + f'/{coin}/wallet/' + wallet_id + f'/transfer/{transfer_id}/comment'

        payload = {
                "comment": "withdrawn"
                }
        r = requests.post(url,
                          json=payload, 
                          headers={ 'Authorization': 'Bearer %s' % self.access_token,}
                          )
        if r.status_code != 200:
            raise Exception('unable to create address\n %s' % r.content)
        return r.json()
    

if __name__=='__main__':
    bitgo =  BitGo()
    # x = bitgo.get_enterprise('663b3119e13a623a0ca95e689d91d4cb')
    # x = bitgo.generate_wallet_exppress('trx')
    # x = bitgo.ping_express()
    # x = bitgo.list_keys('polygon')
    # x = bitgo.get_wallets()
    x = bitgo.create_address('trx', '6664971ece8d97a8157f3a050272a1af')
    print(x)

    with open('last.json','w') as f:
        json.dump(x,f, indent=4)
