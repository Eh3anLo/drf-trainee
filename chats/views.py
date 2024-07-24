import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import ChatSerializer
from .models import Chat
# Create your views here.

class ChatView(APIView):
    
    def post(self,request):
        cleaned_data = []
        with open("data.json") as file:
            data_post = json.load(file)
            for value in data_post.values():
                for data in value:
                    cleaned_data.append(data)
        serializer = ChatSerializer(data=cleaned_data , many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(f"{serializer.validated_data} created." , status=status.HTTP_201_CREATED)
    
    def get(self,request):
        chat_querysets = Chat.objects.all()
        serializer = ChatSerializer(chat_querysets , many=True)
        return Response(serializer.data)
    
