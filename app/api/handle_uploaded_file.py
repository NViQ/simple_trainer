import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

openai_api_key = os.environ.get('OPENAI_KEY')
client = OpenAI(api_key=openai_api_key)

def handle_uploaded_file(uploaded_file):
    try:
        temp_file_path = save_temp_file(uploaded_file)
        with open(temp_file_path, 'rb') as audio_file:
            transcription_response = client.audio.translations.create(
                model="whisper-1",
                file=audio_file
            )
        os.remove(temp_file_path)

        if hasattr(transcription_response, 'text'):
            audio_transcription = transcription_response.text
        else:
            return {'error': 'Transcription failed'}

        with open('app/text_example.txt', 'r') as file:
            text_example = file.read()
            print(text_example, type(text_example))

        prompt_template = (
            "Here are two texts: Text A: '{audio_transcription}' Text B: '{text_example}'. "
            "Please compare them and give me the percentage of similarity."
        )
        prompt = ChatPromptTemplate.from_template(prompt_template)
        model = ChatOpenAI(model="gpt-3.5-turbo-1106", openai_api_key=openai_api_key)
        output_parser = StrOutputParser()
        chain = prompt | model | output_parser

        similarity_response = chain.invoke({"audio_transcription": audio_transcription, "text_example": text_example})
        print(f'Percentage of match: {similarity_response}')
        return {'similarity_percentage': similarity_response}

    except Exception as e:
        print(f"Error processing the file: {e}")
        return {'error': str(e)}


def save_temp_file(uploaded_file):
    temp_file_path = f'temp_{uploaded_file.name}'
    with open(temp_file_path, 'wb+') as temp_file:
        for chunk in uploaded_file.chunks():
            temp_file.write(chunk)
    return temp_file_path
