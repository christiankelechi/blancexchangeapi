from django.db import models
from core_app_root.security.user.models import User
# Create your models here.
class TrxWalletModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)