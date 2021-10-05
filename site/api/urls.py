from api.services import chamada, oficinas, aluno
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
    path('chamadaaluno/<str:id>/', chamada.get_chamada_aluno_by_id),
    path('chamadaaluno/', chamada.get_chamada_aluno),

    #! Aluno

    path('aluno/create/', aluno.create_aluno),
    path('aluno/update/', aluno.update_aluno),
    path('aluno/delete/', aluno.delete_aluno),
    path('responsavel/create/', aluno.create_responsavel),
    path('responsavel/<str:id>/', aluno.get_responsavel_by_id),
    path('aluno/<str:id>/', aluno.get_aluno_by_id),
    path('aluno/', aluno.get_aluno),

    #! Oficina

    path('oficinas/create/', oficinas.create_oficina),
    path('oficinas/update/',oficinas.update_oficina),
    path('oficinas/delete/', oficinas.delete_oficina),
    path('oficinas/<str:id>/', oficinas.get_oficina_by_id),
    path('oficinas/', oficinas.get_oficina),
    path('oficinasaluno/create/', oficinas.create_aluno_oficina),
    path('oficinasaluno/<str:id>/', oficinas.get_oficina_aluno_by_id),
    path('oficinasaluno/', oficinas.get_oficina_aluno),
]