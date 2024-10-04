from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework import status
from bitgo.bitgo_base import BitGo


from dashboard.permissions import IsOwnerOrAdmin
from rest_framework import permissions

from management.models import BitgoWallet
from management.serializers import BitgoWalletSerializer

# Create your views here.

class BitgoWalletViewSet(viewsets.ModelViewSet):
    queryset = BitgoWallet.objects.all()
    serializer_class = BitgoWalletSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        _type = request.data.get('_type')

        if not _type:
            return Response({'error': 'Type is required.'}, status=status.HTTP_400_BAD_REQUEST)

        if BitgoWallet.objects.filter(_type=_type).exists():
            return Response({'_type': 'Wallet of this type already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            bitgo = BitGo()
            wallet_data = bitgo.generate_wallet_exppress(_type)
        except Exception as e:
            # Log the exception
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if not wallet_data or 'id' not in wallet_data:
            return Response({'error': 'Failed to generate wallet.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = BitgoWalletSerializer(data={
            'wallet_id': wallet_data['id'],
            '_type': _type
        })

        if not serializer.is_valid():
            # Log invalid serializer errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = serializer.save()
        except Exception as e:
            # Log the exception
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        headers = self.get_success_headers(serializer.data)
        return Response(wallet_data, status=status.HTTP_201_CREATED, headers=headers)



class CoinPriceView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, coin_name):
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            'ids': coin_name,
            'vs_currencies': 'ngn'
        }
        
        response = requests.get(url, params=params)

        if response.status_code == 200:
            price_data = response.json()
            return Response(price_data)
        else:
            return Response({'error': 'Failed to fetch coin price'}, status=response.status_code)

