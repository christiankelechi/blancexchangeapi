from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework import permissions, status
from drf_yasg import openapi
from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers

from bitgo.models import Address
from bitgo.serializers import AddressSerializer
from dashboard.base_viewsets import LRUViewSet, RViewSet, RLViewSet
from dashboard.models import Wallet, Bank_Account, Deposit, Withdrawal, Notification
from dashboard.profile_model import Profile
from .serializers import NotificationSerializer, ProfileSerializer, WalletSerializer, BankAccountSerializer, DepositSerializer, WithdrawalSerializer
from .permissions import IsOwnerAndReadOnly, IsOwnerOrAdmin, IsOwner



class ProfileViewSet(LRUViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)
        


class WalletViewSet(RLViewSet):
    # queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsOwnerAndReadOnly]
    
    def get_queryset(self):
        return Wallet.objects.filter(profile=self.request.user.profile)

    def retrieve(self, request, *args, **kwargs):
        wallet = request.user.profile.wallet
        serializer = WalletSerializer(wallet)

        return Response(serializer.data)

class BankAccountViewSet(viewsets.ModelViewSet): 
    
    serializer_class = BankAccountSerializer
    # permission_classes = [IsOwnerOrAdminCanDelete]
    permission_classes = [IsOwner]

    def get_queryset(self):
        return self.request.user.profile.bank_accounts
    
    def create(self, request, *args, **kwargs):
        profile = request.user.profile
        name = request.data.get('name')
        acc_no = request.data.get('acc_no')
        bank = request.data.get('bank')
        is_default = request.data.get('is_default')

        bank_choices = [choice[0] for choice in Bank_Account.Banks.choices]
        if bank not in bank_choices:
            return Response({'error': 'Invalid bank.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BankAccountSerializer(data={
            'name': name,
            'acc_no': acc_no,
            'bank': bank,
            'is_default': is_default
        })

        if not serializer.is_valid():
            # Log invalid serializer errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            if is_default:
                Bank_Account.objects.filter(profile=profile).update(is_default=False)
                
            instance = serializer.save(profile=profile)
        except Exception as e:
            # Log the exception
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
class NotificationViewSet(RLViewSet):
    # queryset = Notification.objects.all()
    permission_classes = [IsOwnerAndReadOnly]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.request.user.profile.notifications

class AddressViewset(RLViewSet):
    serializer_class = AddressSerializer
    permission_classes = [IsOwnerAndReadOnly]

    
    def get_queryset(self):
        return self.request.user.profile.addresses
    
    # def list(self, request):
    #     try:
    #         queryset = self.get_queryset()
    #     except Exception as e:
    #         return Response({'unable to fetch addresses': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    #     queryset = self.get_queryset()

    #     if queryset.count() == 0:
    #         Address.initialise_addresses(self.request.user.profile)
    #         return Response({"data": []}, status=status.HTTP_200_OK)
        
    #     serializer = AddressSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     id = kwargs.get('id')
    #     address = request.user.profile.addresses.filter(id=id)
    #     serializer = AddressSerializer(address)

    #     return Response(serializer.data)


class DepositViewSet(RLViewSet):
    permission_classes = [IsOwnerAndReadOnly]
    serializer_class = DepositSerializer

    def get_queryset(self):
        return self.request.user.profile.deposits

class WithdrawalViewSet(RLViewSet):
    permission_classes = [IsOwnerAndReadOnly]
    serializer_class = WithdrawalSerializer

    def get_queryset(self):
        return self.request.user.profile.withdrawals





class ConfirmDepositView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            if user.profile:
                try:
                    Deposit.update_deposits(user.profile)
                except Exception as e:
                    return Response({'text':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
            else:
                Profile.objects.get_or_create(user=user)
                return Response({'text':'profile created'}, status=status.HTTP_201_CREATED)
            return Response({
                'text':'your deposits are currently being updated'
            }, status=status.HTTP_200_OK)
        return Response({
                'text':'you are not authenticated'
            }, status=status.HTTP_401_UNAUTHORIZED)

class WithdrawView(APIView):
    # @swagger_auto_schema(
    #     request_body=serializers.Serializer(),
    #     responses={200: serializers.Serializer()},
    #     request_body_description="Withdrawal request",
    #     manual_parameters=[
    #         openapi.Parameter(
    #             name="amount",
    #             in_=openapi.IN_QUERY,
    #             description="Amount to withdraw",
    #             type=openapi.TYPE_FLOAT,
    #             required=True
    #         ),
    #         openapi.Parameter(
    #             name="account_number",
    #             in_=openapi.IN_QUERY,
    #             description="Bank account number to withdrawal from",
    #             type=openapi.TYPE_STRING,
    #             required=True
    #         ),
    #     ]
    # )
    def post(self, request):
        user = request.user
        amount = request.POST['amount']
        acc_no = request.POST['account_number']

        if user.is_authenticated:
            if user.profile:
                bank_acc = get_object_or_404(Bank_Account, acc_no=acc_no)
                withdrawal = Withdrawal.objects.create(user=user, amount=amount, bank_account=bank_acc)
                withdrawal.confirm()
            else:
                Profile.objects.get_or_create(user=user)

            return Response({
                'text':'withdrawal initiated'                                                                                                                                                 
            }, status=status.HTTP_200_OK)
        return Response({
                'text':'you are not authenticated'
            }, status=status.HTTP_401_UNAUTHORIZED)
    
