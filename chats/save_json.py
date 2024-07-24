import json
from .serializers import ChatSerializer

def save_json_from_file(filename):
    cleaned_data = []
    with open(filename) as file:
        data_post = json.load(file)
        for value in data_post.values():
            for data in value:
                cleaned_data.append(data)
    serializer = ChatSerializer(data=cleaned_data , many=True)
    serializer.is_valid(raise_exception=True)
    if serializer.validated_data:
        serializer.save()
        print("Save from file completed ...")
        return
    return serializer.data
    

    