from django.urls import path
from .text_chat import TextChatQueryView
from .views import FileUploadView

urlpatterns = [
    path('check-writing/', TextChatQueryView.as_view(), name='check-writing'),
    path('upload-file/', FileUploadView.as_view(), name='file-upload'),
]