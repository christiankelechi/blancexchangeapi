from rest_framework import serializers
class VerifySerializer(serializers.Serializer):
    code_authentication=serializers.CharField(max_length=1000)
    