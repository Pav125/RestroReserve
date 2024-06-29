from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('status/', views.status_table, name = 'status'),
    path('about/', views.about, name = 'about'),
    path('register/', views.register, name = 'register')
]