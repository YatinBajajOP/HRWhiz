from django.contrib import admin
from django.urls import path
from . import views
# urls.py
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import EmployeeViewSet, EmployeeRegistration, EmployeeLogin

# router = DefaultRouter()
# router.register(r'employees', EmployeeViewSet)
# 
# urlpatterns = [
#     # path('', include(router.urls)),
#     # path('register/', EmployeeRegistration.as_view(), name='employee-registration'),
#     # path('login/', EmployeeLogin.as_view(), name='employee-login'),
# ]

urlpatterns = [
    path("", views.dashboard),
    path("feedback/", views.feedback, name='submit_feedback'),
    path("ask_hr/", views.ask_hr, name='submit_hr_query'),
    path('leaverequest/', views.leaverequest, name='submit_leave'),

]