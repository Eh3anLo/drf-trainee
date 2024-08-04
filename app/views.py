from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import Person
from .serializers import PersonSerializer
# Create your views here.

class PersonAuthentication(APIView):

    def post(self, request):
        if request.data:
            serializer = PersonSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            person = serializer.validated_data
            person_ins = get_object_or_404(Person, person_number=person['person_number'])
            serializer = PersonSerializer(instance=person_ins, data=person)
            serializer.is_valid()
            serializer.save()
            
            return Response(serializer.data)
        return render(request, "app/register.html", context={"info" : "new_pass"})
            
