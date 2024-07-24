from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    data = serializers.JSONField()