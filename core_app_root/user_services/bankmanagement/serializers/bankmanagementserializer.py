from rest_framework import serializers
from core_app_root.user_services.bankmanagement.models import BankAdminManager,UserBankAccountDetails
class BankManagementSerializer(serializers.ModelSerializer):
    class Meta:
        fields=['bank_code','bank_name']
        model=BankAdminManager

class UserBankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields=['bank_code','account_number','bank_name','account_name']
        model=UserBankAccountDetails