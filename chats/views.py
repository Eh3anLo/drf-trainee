from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import json

from .utils import custom_sort

class MessageView(APIView):

    def get(self , request , filename="data.json"):
        with open(filename , "r") as response_file:
            respones_json = json.load(response_file)
        respones_json = custom_sort(respones_json)
        return Response(respones_json)
    
    

    # def get(self , request):
    #     with open("data.json" , "r") as response_file:
    #         respones_json = json.load(response_file)
    #     return Response(respones_json)