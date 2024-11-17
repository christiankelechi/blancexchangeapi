from rest_framework import serializers
from core_app_root.wallet_management.models import VirTualNigeriaNWallet
class VirtualNigeriaWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=VirTualNigeriaNWallet
        fields="__all__"