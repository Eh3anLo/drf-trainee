from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import json
import os
class MessageView(APIView):

    # def get(self , request , filename):
    #     file_path =os.path.join(filename)
    #     print(file_path) 
    #     with open("/home/arses/my_files/work/DRF_TR/sample.json" , "r") as response_file:
    #         respones_json = json.load(response_file)
    #     return Response(respones_json)

    def get(self , request):
        with open("/home/arses/my_files/work/DRF_TR/data.json" , "r") as response_file:
            respones_json = json.load(response_file)
        return Response(respones_json)