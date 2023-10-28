from django.shortcuts import render
# views.py
# from rest_framework import viewsets, permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Employee
from .serializers import EmployeeSerializer

# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeRegistration(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request):
#         data = request.data
#         try:
#             employee = Employee.objects.create_user(
#                 email=data['email'],
#                 password=data['password'],
#                 name=data['name'],
#                 address=data['address'],
#                 phone_number=data['phone_number'],
#                 pid=data['pid'],
#                 did=data['did'],
#                 manager_id=data['manager_id'],
#                 status=data['status'],
#                 profile_url=data['profile_url']
#             )
#             return Response(EmployeeSerializer(employee).data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# class EmployeeLogin(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = authenticate(email=email, password=password)

#         if user:
#             payload = api_settings.JWT_PAYLOAD_HANDLER(user)
#             token = api_settings.JWT_ENCODE_HANDLER(payload)
#             return Response({'token': token})
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
def dashboard(request):
    return render(request, 'emp.html')

def feedback(request):
    return render(request, 'feedback.html')

