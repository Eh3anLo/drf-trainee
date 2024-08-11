from django.urls import path
from . import views
urlpatterns =[
    path('login/' , views.UserAuthentication.as_view(), name='register'),
]