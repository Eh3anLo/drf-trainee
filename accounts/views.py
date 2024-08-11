from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, authenticate
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import UserSerializer


# Create your views here.


class UserAuthentication(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser,]

    def get(self, request):
        user_queryset = User.objects.all()
        serializer = UserSerializer(instance=user_queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token" : token.key, "created" : created}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error' : "user_not_found_or_something", "message" : user}, status=status.HTTP_400_BAD_REQUEST)

