from . import views
from django.urls import path

urlpatterns = [
    path("addemployee/", views.add_employee),
    path("deleteemployee/", views.delete_employee),
    #path("req/",views.hr_requests_view),
    path('addmanager/', views.assign_manager),
    path('hrFeedbackview/',views.hr_Feedback_view),
    path("", views.dashboard)
]

