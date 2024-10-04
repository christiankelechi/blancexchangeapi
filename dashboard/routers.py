from rest_framework import routers
from .views import AddressViewset, DepositViewSet, ProfileViewSet, NotificationViewSet, WithdrawalViewSet, WalletViewSet, BankAccountViewSet

app_name='dashboard'

router = routers.SimpleRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'banks', BankAccountViewSet, basename='bank')
router.register(r'wallet', WalletViewSet, basename='wallet')
router.register(r'addresses', AddressViewset, basename='addresses')
router.register(r'deposits', DepositViewSet, basename='deposits')
router.register(r'notifications', NotificationViewSet, basename='notifications')
router.register(r'withdrawals', WithdrawalViewSet, basename='withdrawals')


urlpatterns=[
    *router.urls
    ]