from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .handle_uploaded_file import handle_uploaded_file

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        print(request.data)  # Для отладки
        if 'audioFile' in request.FILES:
            file_obj = request.FILES['audioFile']
            # Обработка файла и получение результата
            result = handle_uploaded_file(file_obj)
            return Response({'transcription': result})
        else:
            return Response({'error': 'No file provided'}, status=400)
