from django.urls import path
from .text_chat import TextChatQueryView

urlpatterns = [
    path('check-writing/', TextChatQueryView.as_view(), name='check-writing'),
]