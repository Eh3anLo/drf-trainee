from django.urls import path
from . import views
urlpatterns = [
    path('', views.ImageApiView.as_view())
]