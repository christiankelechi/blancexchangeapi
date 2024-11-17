from rest_framework import routers
from core_app_root.wallet_management.viewsets.virtual_nigerian_wallet import VirtualNigeriaWalletViewset

router=routers.SimpleRouter()
router.register(r'ngn_wallet',VirtualNigeriaWalletViewset,basename='ngn_wallet')


urlpatterns=[
    *router.urls
]
