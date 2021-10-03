from api.services import chamada, oficinas
from django.urls import path


urlpatterns = [
    #! Chamada

    path('chamada/create/', chamada.create_chamada),
    path('chamada/update/', chamada.update_chamada),
    path('chamada/delete/', chamada.delete_chamada),
    path('chamada/<str:id>/', chamada.get_chamada_by_id),
    path('chamada/', chamada.get_chamada),

    #! Chamada Aluno

    path('chamadaaluno/create/', chamada.create_chamada_aluno),
    path('oficinaaluno/create/',oficinas.create_aluno_oficina),
    path('oficinaaluno/<str:id>/',oficinas.get_oficina_aluno_by_id),
    path('chamadaaluno/<str:id>/', chamada.get_chamada_aluno_by_id),
    path('chamadaaluno/', chamada.get_chamada_aluno),
    path('oficinas/create/', oficinas.create_oficina),
    path('oficinas/update/',oficinas.update_oficina),
    path('oficinas/delete/', oficinas.delete_chamada),
    path('oficinas/<str:id>/', oficinas.get_oficina_by_id),
    path('oficinas/', oficinas.get_oficina),
]