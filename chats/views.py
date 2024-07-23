from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import json
import os
class MessageView(APIView):

    def get(self , request , filename="data.json"):
        print(filename)
        with open(filename , "r") as response_file:
            respones_json = json.load(response_file)
        return Response(respones_json)

    # def get(self , request):
    #     with open("data.json" , "r") as response_file:
    #         respones_json = json.load(response_file)
    #     return Response(respones_json)