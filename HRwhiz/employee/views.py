from django.shortcuts import render
from django.http import HttpResponse
# views.py
# from rest_framework import viewsets, permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Employee, Feedback
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
    return render(request, 'emp.html', {'name': request.session['name'], 'id': request.session['id'], 'designation': request.session['designation']})

from django.shortcuts import render, redirect
from .models import Feedback, askHR, leaverequest

def feedback(request):
    if request.method == 'POST':       
        id=request.POST.get('id')
        name=request.POST.get('name')
        fed_to=request.POST.get('feedback_to')
        des=request.POST.get('description')
        res=Feedback(id=id,name=name,fed_to=fed_to,message=des)
        res.save()
    
    return render(request, 'feedback.html')
def ask_hr(request):
    if request.method == 'POST':
        id=request.POST.get('employee_id')
        text=request.POST.get('query')
        res=askHR(id=id,text=text)
        res.save()
    return render(request,'askHR.html')

def leaverequest(request):
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        reason = request.POST.get('reason')

        # Create and save a new LeaveRequest object
        new_leave_request = leaverequest(date_from=date_from, date_to=date_to, reason=reason)
        new_leave_request.save()

        return redirect('success')  # Redirect to a success page after saving
    return render(request, 'leaverequest.html')

