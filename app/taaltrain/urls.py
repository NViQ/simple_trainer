from django.urls import path
from app.api.v1.text_chat import UserQueryView

urlpatterns = [
    path('check-writing/', UserQueryView.as_view(), name='check-writing'),
]