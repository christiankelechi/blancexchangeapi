from django.db import models

# Create your models here.

class BitgoWallet(models.Model):
    class Type(models.TextChoices):
        TRX = 'trx', 'TRON'
        SOL = 'sol', 'Solana'
        POLYGON = 'polygon', 'Polygon'

    wallet_id = models.CharField(max_length=50)
    _type = models.CharField(max_length=20, choices=Type.choices)
    
    @classmethod
    def from_dict(cls, data):
        return cls.objects.bulk_create(data)
    
    def __str__(self):
        return self._type + 'wallet'