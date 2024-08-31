
from django.urls import path
from . import views
urlpatterns = [
    path('' , views.MyAPIView.as_view()),
]
