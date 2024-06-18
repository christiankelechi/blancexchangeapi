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
    
    

class UserBankDetailsViewset(viewsets.ModelViewSet):
    serializer_class=UserBankDetailsSerializer
    permission_classes=[permissions.AllowAny]
    http_method_names=['get','post']
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            
            load_dotenv()

            # Fetch the secret key from environment variables
            secret_key = os.getenv('PRIVATE_PAYSTACK_KEY')
            # Fetch the secret key from environment variables


            # Define your base URL
            base_url = 'https://api.paystack.co'

            # Dummy data for serializer.validated_data to simulate request data
            # In a real application, replace this with actual data
            serializer_data = {
                'validated_data': {
                    'account_number': str(serializer.validated_data['account_number']),
                    'bank_code': str(serializer.validated_data['bank_code'])
                }
            }

            # Define endpoint and parameters
            endpoint = '/bank/resolve'
            params = {
                'account_number': str(serializer_data['validated_data']['account_number']),
                'bank_code': str(serializer_data['validated_data']['bank_code'])
            }

            # Define headers
            headers = {
                'Authorization': f'Bearer {secret_key}'
            }

            # Make GET request
            response = requests.get(f'{base_url}{endpoint}', params=params, headers=headers)

            # Check for successful request
            if response.status_code == 200:
                data = response.json()
                account_name = data['data']['account_name']
                # print(f'Account Name: {account_name}')
                return Response({"status":False,"message":"bank name fetched successfully","data":data})
            else:
                return Response({"status":False,"message":"bank name fetched successfully","data":data})
            return Response({"status":False,"message":"bank name fetched successfully"})

    def get_queryset(self):
        return super().get_queryset()