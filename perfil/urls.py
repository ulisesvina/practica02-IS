from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('confirmar/', views.confirmar_django, name='confirmar_django'),
]
