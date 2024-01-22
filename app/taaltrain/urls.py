from django.urls import path
from app.api.v1.text_chat import UserQueryView

urlpatterns = [
    path('process-query/', UserQueryView.as_view(), name='process_query'),
]