from django.urls import path
from . import views
urlpatterns = [
    path('chats/', views.ChatView.as_view() , name='chat-list')
]