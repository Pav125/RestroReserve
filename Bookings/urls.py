from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path('status/', views.status_table, name = 'status'),
    path('about/', views.about, name = 'about'),
    path('register/<int:id>/', views.register, name = 'register'),
    path('menu/', views.menu, name = 'menu'),
    path('contact/', views.contact, name = 'contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)