from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('viewEmployees/',views.view_employees),
    path('adddepandpro/',views.dep_project),
    path('mgrrequestsview/',views.mgr_requests_view),
    path('mgrfeedbackview/',views.mgr_Feedback_view),
    path('employeeviewstatus/',views.Employee_view_Status),
    path('', views.dashboard)
]