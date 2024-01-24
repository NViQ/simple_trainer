from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_KEY')


class UserQueryView(APIView):
    def post(self, request, format=None):
        user_id = request.data.get('user_id')
        user_query = request.data.get('user_query')

        if user_query is None:
            return Response({'error': 'Error there is no request text'}, status=status.HTTP_400_BAD_REQUEST)

        # Шаблон запроса, использующий переменную
        prompt_template = (
            "Check this text for grammatical errors, the words in which there were errors, "
            "if any, and the percentage of the correct text: {user_query}"
        )
        prompt = ChatPromptTemplate.from_template(prompt_template)
        model = ChatOpenAI(model="gpt-3.5-turbo-1106", openai_api_key=OPENAI_API_KEY)
        output_parser = StrOutputParser()
        chain = prompt | model | output_parser

        # Передача user_query как словаря
        response = chain.invoke({"user_query": user_query})

        return Response({'user_id': user_id, 'response': response})