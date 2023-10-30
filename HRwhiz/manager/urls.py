from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('viewEmployees/',views.view_employees),
    path('add_dep_and_pro/',views.dep_project),
    path('', views.dashboard)
]