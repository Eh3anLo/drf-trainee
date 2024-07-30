from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework import renderers
from django.conf import settings
from django.shortcuts import get_object_or_404
from .serializers import ImageSerializer
from .utils import gray_scale
from .models import Image
# Create your views here.



class ImageApiView(APIView):



    def post(self, request):
        serializer = ImageSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        img = serializer.save()
        image_path = gray_scale(img.origin_image)
        up_image = get_object_or_404(Image, id=img.id)
        up_image.processed_image = image_path
        up_image.save()
        return Response(status=HTTP_200_OK)
    

    def get(self,reqeust):
        images_queryset = Image.objects.all()
        serializer = ImageSerializer(images_queryset, many=True)

        new_row = {}
        for items in serializer.data:
            keys_list = list(items.keys())
            new_row[int(items['id'])] = {keys_list[1]: settings.DOMAIN+str(items[keys_list[1]]) , keys_list[2]: settings.DOMAIN+str(items[keys_list[2]])}
            
        return Response({'images': new_row}, status=HTTP_200_OK)