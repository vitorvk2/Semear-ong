from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.listagem),
    path('responsavel/list/', views.listagem_resp),
    path('detail/<str:id>/', views.detalhes),
    path('create/', views.create),
    path('detailresp/<str:id>/', views.detalhesResp),
    path('createresp/', views.createResp),
]
