from rest_framework import serializers
from core_app_root.security.auth.models import CodeGenerator
class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model=CodeGenerator
        fields=['code_authentication']
    