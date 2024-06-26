from django.urls import path
from . import views

urlpatterns = [
    path('status', views.status_table, name = 'status'),
    path("", views.home, name="home"),
]