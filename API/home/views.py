from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import *
from .serializer import *
from rest_framework.views import APIView
# Create your views here.


@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serializers = Bookserializer(book_objs , many=True)
    return Response({'status':200 ,'payload':serializers.data}) 

class StudentAPI(APIView):
    def get(self,request):
        student_objs = Student.objects.all()
        serializer = studentserializer(student_objs,many=True)
        return Response({'status': 200 , 'payload' : serializer.data})
    
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403,'errors':serializers.errors, 'messge':'Something went wrong'})
        
        serializer.save( ) 
        return Response({'status' : 200,'payload' :serializer.data ,'messge':'you send'})




    def post(self,request):
        pass
    def put(self,request):
        pass
    def patch(self,request):
        pass
    def delete(self,request):
        pass    























# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = studentserializer(student_objs,many=True)
#     return Response({'status':200 , 'payload' : serializer.data})

# @api_view(['POST'])
# def post_Student(request):
#     data = request.data
#     data = request.data
#     serializer = studentserializer(data=request.data)

#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status': 403, 'messge':'Something went wrong'})
#     serializer.save( ) 

#     return Response({'status' : 200,'payload' :data ,'messge':'you send'})



# @api_view(['PUT'])
# def update_Student(request,id):
#     try:
#         student_obj = Student.ojects.get(id=id)
#         serializer = studentserializer(student_obj,data=request.data, partial=True)

#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403, 'errors':serializer.errors,'messge':'Something went wrong'})
#         serializer.save( ) 
#         return Response({'status' : 200,'payload' :serializer .data ,'messge':'you send'})

#     except Exception as e:
#         return Response({'status':403,'massage':'invalid id'})

# @api_view(['DELETE'])
# def delete_student(request,id):
#     try:
        
#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'status':200,'message':'deleted'})
    
#     except Exception as e:
#         print(e)
#         return Response({'status':403,'message':'invalid id'})