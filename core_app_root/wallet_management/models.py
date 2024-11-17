from django.db import models
from core_app_root.security.user.models import User
# Create your models here.
class OutflowTransactions(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    amount=models.FloatField(null=True,blank=True)
    date_initiated=models.DateTimeField(auto_now_add=True,blank=True,null=True)

class InflowTransactions(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    amount=models.FloatField(null=True,blank=True)
    date_initiated=models.DateTimeField(auto_now_add=True,blank=True,null=True)
class VirTualNigeriaNWallet(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    account_balance=models.FloatField(null=True,blank=True,default=0)
    date_created=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    

    