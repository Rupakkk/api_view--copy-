from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import APIView

class StudentApiView(APIView):
    def get(self,request,pk=None,format=None):
        id = pk  # Remember this , pk comes directly
        if id is not None:
            data = Student.objects.get(id=id)
            serialize = StudentSerializer(data)
            return Response({'msg':'This is get Respons','serialize':serialize.data})
        else:
            data = Student.objects.all()
            serialize = StudentSerializer(data,many = True)
            return Response(serialize.data)
                
    def post(self,request,format=None):
        data = request.data  # This is parsed data
        print(data.get('address'))
        serialize = StudentSerializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({'msg':'This is post Respons'},status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors)


    def put(self,request,pk=None,format=None):
        stu = Student.objects.get(id=pk)
        serialize = StudentSerializer(stu,data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'msg':'Complete Data edit complete'})
        else:
            return Response(serialize.errors)


    def patch(self,request,pk=None,format=None):
        stu = Student.objects.get(id=pk)
        serialize = StudentSerializer(stu,data = request.data,partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response({'msg':'Partial Data edit complete'})
        else:
            return Response(serialize.errors)

    def delete(self,request,pk=None,format=None):
        if pk is not None:
            data = Student.objects.get(id=pk)
            data.delete()
            return Response({'msg':'Deletion Successful'},status=status.HTTP_508_LOOP_DETECTED)
        else:
            data = Student.objects.all()
            data.delete()
            return Response("DEletion Succesful")

            


