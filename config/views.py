from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import json

class MessageView(APIView):

    def get(self , request):
        with open("/home/arses/my_files/work/DRF_TR/data.json" , "r") as response_file:
            respones_json = json.load(response_file)
        return Response(respones_json)