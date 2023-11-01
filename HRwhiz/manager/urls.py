from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    
    
    path('adddepandpro/',views.assign_dep_project),
    path('mgrrequestsview/',views.mgr_requests_view),
    path('mgrfeedbackview/',views.mgr_feedback_view),
    path('employeeviewstatus/',views.employee_view_status),
    path('', views.dashboard),
    path("assigntask/",views.assign_task),

]