from django.urls import path
from .views import PersonLogin

urlpatterns = [
    # path('register/', PersonAuthentication.as_view(), name='register'),
    path('login/', PersonLogin.as_view(), name='login'),

]