from . import views
from django.urls import path

urlpatterns = [
    path("add_employee/", views.add_employee),
    path("delete_employee/", views.delete_employee),
    path("req/",views.hr_requests_view),
    path('addmanager/', views.addmanager),
    path("", views.dashboard)
]

