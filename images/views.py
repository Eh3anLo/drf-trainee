from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework import renderers
from django.conf import settings
from django.shortcuts import get_object_or_404
from .serializers import ImageSerializer
from .utils import gray_scale
from .models import Images
# Create your views here.

class CustomRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {}
        if data:
            new_row = {}
            for items in data:
                keys_list = list(items.keys())
                new_row[int(items['id'])] = {keys_list[1]: settings.DOMAIN+str(items[keys_list[1]]) , keys_list[2]: settings.DOMAIN+str(items[keys_list[2]])}
            response_data['images'] = new_row
        return super().render(response_data, accepted_media_type, renderer_context)


class ImageApiView(APIView):
    renderer_classes = [CustomRenderer]

    def post(self, request):
        serializer = ImageSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        img = serializer.save()
        image_path = gray_scale(img.origin_image)
        up_image = get_object_or_404(Images, id=img.id)
        up_image.processed_image = image_path
        up_image.save()
        return Response(status=HTTP_200_OK)
    
    def get(self,reqeust):
        images_queryset = Images.objects.all()
        serializer = ImageSerializer(images_queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)