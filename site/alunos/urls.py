from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.listagem),
    path('detail/<str:id>/', views.detalhes),
    path('create/', views.create),
    path('detailResp/<str:id>/', views.detalhesResp),
]
