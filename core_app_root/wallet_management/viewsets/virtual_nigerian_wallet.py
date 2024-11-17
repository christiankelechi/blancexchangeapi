from rest_framework import viewsets
from core_app_root.wallet_management.models import VirTualNigeriaNWallet
from core_app_root.wallet_management.serializers.virtual_nigerian_wallet import VirtualNigeriaWalletSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class VirtualNigeriaWalletViewset(viewsets.ModelViewSet):
    serializer_class=VirtualNigeriaWalletSerializer
    http_method_names=['post','get']
    queryset=VirTualNigeriaNWallet.objects.all()
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"status":True,"message":f"created a new walletus for the user {request.user.email}"})
    
    def list(self,request):
        try:
            current_account=self.queryset.get(user=request.user)
            current_account_balance=current_account.account_balance
            return Response({"status":True,"message":"User Wallet Retrieved Successfully","data":{"balance":current_account_balance,"username":request.user.username}})

        except VirTualNigeriaNWallet.DoesNotExist:
            VirTualNigeriaNWallet.objects.create(user=request.user,account_balance=0.0)
            current_account=self.queryset.get(user=request.user)
            current_account_balance=current_account.account_balance
            error_message="created a new wallet since the user does not have wallet before"
            return Response({"status":False,"message":f"{error_message}","data":{"balance":current_account_balance,"username":request.user.username}})
        # return super().get_object()

    