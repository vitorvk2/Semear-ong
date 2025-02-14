from api.services import chamada, oficinas, aluno, orientador
from . import views
from django.urls import path


urlpatterns = [
    #! Chamada

    path('chamada/create/', chamada.create_chamada),
    path('chamada/update/', chamada.update_chamada),
    path('chamada/delete/', chamada.delete_chamada),
    path('chamada/aluno/<str:oficina_id>/<str:aluno_id>/', chamada.get_chamada_by_aluno),
    path('chamada/<str:id_oficina>/<str:id>/', chamada.get_chamada_by_id),
    path('chamada/<str:id_oficina>/', chamada.get_chamada),

    #! Chamada Aluno

    path('chamadaaluno/create/', chamada.create_chamada_aluno),
    path('chamadaaluno/<str:id_chamada>/<str:id>/', chamada.get_chamada_aluno_by_id),
    path('chamadaaluno/<str:id_chamada>/', chamada.get_chamada_aluno),

    #! Aluno

    path('aluno/create/', aluno.create_aluno),
    path('aluno/update/', aluno.update_aluno),
    path('aluno/delete/', aluno.delete_aluno),
    path('aluno/<str:id>/', aluno.get_aluno_by_id),
    path('aluno/', aluno.get_aluno),

    #! Responsavel

    path('responsavel/create/', aluno.create_responsavel),
    path('responsavel/update/', aluno.update_responsavel),
    path('responsavel/delete/', aluno.delete_responsavel),
    path('responsavel/<str:id>/', aluno.get_responsavel_by_id),
    path('responsavel/', aluno.get_responsavel),

    #! Orientador

    path('orientador/create/', orientador.create_orientador),
    path('orientador/update/', orientador.update_orientador),
    path('orientador/delete/', orientador.delete_orientador),
    path('orientador/<str:id>/', orientador.get_orientador_by_id),
    path('orientador/', orientador.get_orientador),

    #! Oficina

    path('oficinas/create/', oficinas.create_oficina),
    path('oficinas/update/',oficinas.update_oficina),
    path('oficinas/delete/', oficinas.delete_oficina),
    path('oficinas/getname/', oficinas.get_oficinas_by_name),
    path('oficinas/detalhealunos/<str:id>/', oficinas.get_oficina_aluno_detalhe_by_id),
    path('oficinas/<str:id>/', oficinas.get_oficina_by_id),
    path('oficinas/', oficinas.get_oficina),
    path('oficinasfive/', oficinas.get_five_oficina),
    path('oficinasimg/add/', oficinas.add_image_oficina),

    #! Oficina Aluno

    path('oficinasaluno/create/', oficinas.create_aluno_oficina),
    path('oficinasaluno/getalunooficinas/', oficinas.get_aluno_oficinas_inscrito),
    path('oficinasaluno/<str:id_oficina>/<str:id>/', oficinas.get_oficina_aluno_by_id),
    path('oficinasaluno/<str:id_oficina>/', oficinas.get_oficina_aluno),

    #! usos gerais

    path('login_interno/', views.make_login_interno),
    path('login_aluno/', views.make_login_aluno),
    path('validate/', views.validate_login),
]