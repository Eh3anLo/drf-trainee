import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import ChatSerializer
from .models import Chat
# Create your views here.

class ChatView(APIView):

    
    def get(self,request):
        chat_querysets = Chat.objects.all()
        serializer = ChatSerializer(chat_querysets , many=True)
        return Response(serializer.data)
    
