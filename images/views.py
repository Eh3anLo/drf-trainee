from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework import renderers
from django.conf import settings
from django.shortcuts import get_object_or_404
from .serializers import ImageSerializer
from .models import Image

from .tasks import img_to_grayscale_task
# Create your views here.



class ImageApiView(APIView):

    def post(self, request):
        serializer = ImageSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        img = serializer.save()
        img_to_grayscale_task.apply_async(args=['~'+img.origin_image.url , img.origin_image.name , img.id])
        if img:
            message = {"message" : "تصویر شما با موفقیت آپلود شد. برای مشاهده نتیجه به پنل خود مراجعه کنید."}
        else:
            message = {"message" :"در هنگام آپلود فایل خطایی رخداد."}
        return Response(message,status=HTTP_200_OK)
    

    def get(self,reqeust):
        images_queryset = Image.objects.all()
        serializer = ImageSerializer(images_queryset, many=True)

        new_row = {}
        for items in serializer.data:
            keys_list = list(items.keys())
            new_row[int(items['id'])] = {
                keys_list[1]: settings.DOMAIN+str(items[keys_list[1]]),
                keys_list[2]: settings.DOMAIN+str(items[keys_list[2]]),
                keys_list[3]: items[keys_list[3]],
            }
            
        return Response({'images': new_row}, status=HTTP_200_OK)