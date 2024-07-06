from rest_framework import routers
from core_app_root.security.auth.viewsets.register import RegisterViewSet,ActivateAccountView
from core_app_root.security.auth.viewsets.login import LoginViewSet
from core_app_root.security.auth.viewsets.promptmessage import MessagePromptViewset
router=routers.SimpleRouter()
router.register(r'register',RegisterViewSet,basename='register')
router.register(r'login',LoginViewSet,basename='login'),
router.register(r'activate_account',ActivateAccountView,basename='activate_account')
router.register(r'prompt/message',MessagePromptViewset,basename='promptmessage')



urlpatterns=[
    *router.urls
]
