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
import os
# Define your secret key and base URL
import json
import requests
class BankManagementViewset(viewsets.ModelViewSet):
    http_method_names=['get']
    
    permission_classes=[permissions.AllowAny]
    serializer_class=BankManagementSerializer
    bank_list=[]
    def list(self,request):
        with open("bank_codes.json","r") as bank_data_file:
            banks=json.load(bank_data_file)
            
# Extract bank names from the queryset
        bank_names = list(banks.keys())
    
        return Response({"bank_names":bank_names},status=status.HTTP_200_OK) 
    
    
    


async def get_paystack_bank_info(bank_code, account_number):
    
    load_dotenv()

        # Fetch the secret key from environment variables
    secret_key = os.getenv('PRIVATE_PAYSTACK_KEY')
    
    response=requests.get(
        f"https://api.paystack.co/bank/resolve?account_number={account_number}&bank_code={bank_code}",
        headers={"Authorization": f"Bearer {secret_key}"},
    )
    return response

# async def runMainScript(account_number,bank_code):
#     account_number = account_number
#     bank_code = bank_code
        

    # async with aiohttp.ClientSession() as session:
    #     result = await get_paystack_bank_info(session, account_number, bank_code)
    #     bank_data=json.dumps(result, indent=4)
    #     return bank_data


class UserBankDetailsViewset(viewsets.ModelViewSet):
    serializer_class=UserBankDetailsSerializer
    permission_classes=[permissions.AllowAny]
    http_method_names=['get','post']
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        bank_code=""

        if serializer.is_valid():
            load_dotenv()

            # Fetch the secret key from environment variables
            secret_key = os.getenv('PRIVATE_PAYSTACK_KEY')
            with open("bank_codes.json","r") as bank_data_file:
                banks=json.load(bank_data_file)
    
            # print(banks)
           
            
            bank_code=banks[str(serializer.validated_data['bank_name'])]
            bank_response_data=asyncio.run(get_paystack_bank_info(str(bank_code),str(serializer.validated_data['account_number'])))
            print(bank_response_data.json())
            return Response({"status":True,"message":"bank name fetched successfully","data":bank_response_data.json()},status=status.HTTP_200_OK)
        
            

def get_queryset(self):
        return super().get_queryset()