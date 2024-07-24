
from django.urls import path
from . import views
urlpatterns = [
    path('' , views.MessageView.as_view() , name="message-list"),
    path('<filename>/' , views.MessageView.as_view())
]
