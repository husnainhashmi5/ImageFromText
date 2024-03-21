from rest_framework import serializers
from .models import Openai

class OpenaiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Openai
        fields='__all__'
