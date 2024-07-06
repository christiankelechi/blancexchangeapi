from django.db import models
from core_app_root.security.user.models import User
# Create your models here.
class CodeGenerator(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    code_authentication=models.CharField(max_length=4)
    
    
    def __str__(self):
        return f" Authentication code sent successfully to user with email {self.user}"


class MessagePromptModel(models.Model):
    message_body=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.message_body)