from django.contrib import admin
from core_app_root.wallet_management import models
# Register your models here.
admin.site.register(models.VirTualNigeriaNWallet)
admin.site.register(models.InflowTransactions)
admin.site.register(models.OutflowTransactions)