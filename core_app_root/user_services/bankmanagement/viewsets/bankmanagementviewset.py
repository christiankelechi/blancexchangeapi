from rest_framework import viewsets
from core_app_root.user_services.bankmanagement.serializers.bankmanagementserializer import BankManagementSerializer,UserBankDetailsSerializer
from rest_framework import permissions
from core_app_root.user_services.bankmanagement.models import BankAdminManager
import requests
from requests.exceptions import JSONDecodeError
from rest_framework.response import Response
from rest_framework import status
from core_app_root.user_services.bankmanagement.models import BankAdminManager,UserBankAccountDetails
from dotenv import load_dotenv
import asyncio
import json
import aiohttp
# Define your secret key and base URL

import requests
class BankManagementViewset(viewsets.ModelViewSet):
    http_method_names=['get']
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=BankManagementSerializer
    def list(self,request):
        all_banks = BankAdminManager.objects.all()

# Extract bank names from the queryset
        bank_names = [bank.bank_name for bank in all_banks]
        bank_codes=[bank.bank_code for bank in all_banks]
        return Response({"bank_names":bank_names,"bank_codes":bank_codes},status=status.HTTP_200_OK) 
    
    


async def get_paystack_bank_info(session, account_number, bank_code, secret_key):
    async with session.get(
        f"https://api.paystack.co/bank/resolve?account_number={account_number}&bank_code={bank_code}",
        headers={"Authorization": f"Bearer {secret_key}"},
    ) as response:
        return await response.json()

async def runMainScript(account_number,bank_code):
    account_number = account_number
    bank_code = bank_code
        

    async with aiohttp.ClientSession() as session:
        result = await get_paystack_bank_info(session, account_number, bank_code, secret_key)
        bank_data=json.dumps(result, indent=4)
        return bank_data


class UserBankDetailsViewset(viewsets.ModelViewSet):
    serializer_class=UserBankDetailsSerializer
    permission_classes=[permissions.AllowAny]
    http_method_names=['get','post']
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
       
            
        load_dotenv()

        # Fetch the secret key from environment variables
        secret_key = os.getenv('PRIVATE_PAYSTACK_KEY')
        # Fetch the secret key from environment variables


        # # Define your base URL
        # base_url = 'https://api.paystack.co'

        # # Dummy data for serializer.validated_data to simulate request data
        # # In a real application, replace this with actual data
        # serializer_data = {
        #         'account_number': str(serializer.validated_data['account_number']),
        #         'bank_code': str(serializer.validated_data['bank_code'])
        #     }
        

        # # Define endpoint and parameters
        # endpoint = '/bank/resolve'
        

        # # Define headers
        # headers = {
        #     'Authorization': f'Bearer {secret_key}'
        # }

        # # Make GET request
        # response = requests.get(f'{base_url}{endpoint}', data=data, headers=headers)
        
        bank_response_data=asyncio.run(runMainScript(str(serializer.initial_data['account_number']),str(serializer.initial_data['bank_code'])))

        
        return Response({"status":True,"message":"bank name fetched successfully","data":bank_response_data},status=status.HTTP_200_OK)
        
        

def get_queryset(self):
        return super().get_queryset()