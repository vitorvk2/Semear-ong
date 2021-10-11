from django.urls import path
from . import views


urlpatterns = [
    path('<str:id_oficina>/', views.listagem),
    path('<str:id_oficina>/create/', views.create),
    path('<str:id_chamada>/alunos/', views.listagem_aluno),
]