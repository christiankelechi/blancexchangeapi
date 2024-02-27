from rest_framework import viewsets
from core_app_root.user_services.bankmanagement.serializers.bankmanagementserializer import BankManagementSerializer,UserBankDetailsSerializer
from rest_framework import permissions
from core_app_root.user_services.bankmanagement.models import BankAdminManager
import requests
from requests.exceptions import JSONDecodeError
from rest_framework.response import Response
from rest_framework import status
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
        return Response({"data":bank_names},status=status.HTTP_200_OK) 
    
    

class UserBankDetailsViewset(viewsets.ModelViewSet):
    serializer_class=UserBankDetailsSerializer
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=['get']
    
    def get(self,request):
        all_bank_details=BankAdminManager.objects.all()
        return Response({"data":all_bank_details},status=status.HTTP_200_OK) 
    def get_queryset(self):
        return super().get_queryset()
    