from django.shortcuts import render

# Create your views here.
from rest_framework.views import  APIView
from .models import student_data
from .serializers import student_dataSerializer
from rest_framework.response import Response
from rest_framework import status
class student_data_api_view(APIView):
    def get(self, request):
        st = student_data.objects.all()
        print(st)
        serialize = student_dataSerializer(st, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = student_dataSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status = status.HTTP_201_CREATED)
        return Response(serialize.data, status = status.HTTP_400_BAD_REQUEST)

    def get_object(self, id):
        try:
            return student_data.objects.get(id=id)
        except:
            return Response(status= status.HTTP_404_NOT_FOUND)

    def put(self, request):
        pk = request.data.get('id')
        serialize = student_dataSerializer(self.get_object(pk), data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        pk = request.data.get('id')
        self.get_object(pk).delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

