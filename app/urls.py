from django.urls import path
from .views import PersonAuthentication

urlpatterns = [
    path('register/', PersonAuthentication.as_view(), name='register')
]