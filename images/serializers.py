from rest_framework import serializers

from .models import Images

class ImageSerializer(serializers.Serializer):
    id =  serializers.IntegerField(required=False)
    origin_image = serializers.ImageField()
    processed_image = serializers.ImageField(required=False)



    def create(self, validated_data):
        print("saveded")
        return Images.objects.create(**validated_data)
