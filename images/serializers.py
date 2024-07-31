from rest_framework import serializers

from .models import Image

class ImageSerializer(serializers.Serializer):
    id =  serializers.IntegerField(required=False)
    origin_image = serializers.ImageField()
    processed_image = serializers.ImageField(required=False)
    message = serializers.CharField(required=False)



    def create(self, validated_data):
        print("saveded")
        return Image.objects.create(**validated_data)
