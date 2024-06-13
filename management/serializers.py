from rest_framework import serializers

from management.models import BitgoWallet

class BitgoWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitgoWallet
        fields = ['wallet_id', '_type']