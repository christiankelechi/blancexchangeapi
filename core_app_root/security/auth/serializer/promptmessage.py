from rest_framework import serializers
from core_app_root.security.auth.models import MessagePromptModel
class MessagePrompt(serializers.ModelSerializer):
    class Meta:
        model=MessagePromptModel
        fields=["message_body"]