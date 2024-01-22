from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.environ.get('OPENAI_KEY')
llm = OpenAI(api_key=openai_api_key)


def format_system_prompt(user_query):
    return f"Проверь этот текст на наличие грамматических или пунктуационных ошибок: \n\n{user_query}"

class UserQueryView(APIView):
    def post(self, request, format=None):
        user_id = request.data.get('user_id')
        user_query = request.data.get('user_query')

        if user_query is None:
            return Response({'error': 'Отсутствует текст запроса'}, status=status.HTTP_400_BAD_REQUEST)

        system_prompt = format_system_prompt(user_query)
        response = llm.complete(prompt=system_prompt, max_tokens=100)

        return Response({'user_id': user_id, 'response': response['choices'][0]['text']})