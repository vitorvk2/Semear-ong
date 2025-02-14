from django.urls import path
from . import views


urlpatterns = [
    path('listagem/', views.listagem),
    path('create/', views.create),
]