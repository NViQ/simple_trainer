from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_KEY')


# def format_system_prompt(user_query):
#     return (
#         "Проверь этот текст на наличие грамматических или пунктуационных ошибок, "
#         "верни процент верного текста и если есть слова в которых были ошибки: "
#         "\n\n" + user_query
#     )


class UserQueryView(APIView):
    def post(self, request, format=None):
        user_id = request.data.get('user_id')
        user_query = request.data.get('user_query')

        if user_query is None:
            return Response({'error': 'Error there is no request text'}, status=status.HTTP_400_BAD_REQUEST)

        prompt = ChatPromptTemplate.from_template(
            "Check this text for grammatical errors, the words in which there were errors, "
            "if any, and the percentage of the correct text:" + user_query
            )
        output_parser = StrOutputParser()
        llm = OpenAI(model="gpt-3.5-turbo-instruct", openai_api_key=OPENAI_API_KEY)
        chain = (
                {"user_query": RunnablePassthrough()}
                | prompt
                | llm
                | output_parser
        )

        response = chain.invoke("user_query")

        return Response({'user_id': user_id, 'response': response})
