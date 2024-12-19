from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Data

class SubmitDataView(APIView):
    def post(self, request):
        name = request.data.get('name')
        value = request.data.get('value')
        data = Data.objects.create(name=name, value=value)
        return Response({"message": "Data saved successfully"})

class DisplayDataView(APIView):
    def get(self, request):
        data = Data.objects.all().values('name', 'value', 'created_at')
        return Response(list(data))