from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import json
from rest_framework import status

from .utils import custom_sort
from .serializers import MessageSerializer
# class MessageView(APIView):
#     def get(self , request , filename="data.json"):
#         with open(filename , "r") as response_file:
#             respones_json = json.load(response_file)
#         respones_json = custom_sort(respones_json)
#         serializer = MessageSerializer(respones_json)
        
#         return Response(serializer.values())

class MessageView(APIView):
    def get(self, request , filename="data.json"):
        with open(filename , "r") as response_file:
            respones_json = json.load(response_file , object_pairs_hook=list) # fix index issue
        # respones_json = custom_sort(respones_json)
        processed_data = self.process_data(respones_json)
        with open('sample.json' , 'w') as file:
            json_data = json.dump(processed_data , file ,skipkeys=True )
            
        return Response(json_data)

    def process_data(self, data):
        new_data = {}
        seen_keys = []
        for key in data:
            key_new = key[0]
            if key[0] in seen_keys:
                key_new = int(key[0]) + 1
                seen_keys.append(str(key_new))
                new_data[str(key_new)] = key[1]
            else:
                seen_keys.append(key[0])
                new_data[key[0]] = key[1]
        print(seen_keys)

        return new_data

    
    

    # def get(self , request):
    #     with open("data.json" , "r") as response_file:
    #         respones_json = json.load(response_file)
    #     return Response(respones_json)