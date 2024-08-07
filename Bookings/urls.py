from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", views.home, name="home"),
    path('status/', views.status_table, name = 'status'),
    path('about/', views.about, name = 'about'),
    path('register/<int:id>/', views.register, name = 'register'),
    path('menu/', views.menu_view, name = 'menu'),
    path('contact/', views.feedback_view, name = 'contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
