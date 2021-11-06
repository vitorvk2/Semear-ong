from api.dto.oficina import oficina_create_dto, oficina_aluno_create_dto, oficina_update_dto, oficina_delete_dto
from core.decorator import has_data_body, validate_dataclass, is_api_authenticated
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from oficinas.models import Oficinas, OficinaAluno
from django.http import JsonResponse, HttpRequest
from orientador.models import Orientador
from alunos.models import Alunos
import json


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(oficina_create_dto.CreateOficina)
@has_data_body
@is_api_authenticated
def create_oficina(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        orientador = Orientador.objects.get(id=data['orientador'])

    except Orientador.DoesNotExist:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Orientador does not exists'
            }, 
            status=422
        )

    oficina = Oficinas(
        nome=data['nome'],
        descricao=data['descricao'],
        local=data['local'],
        link=data['link'],
        horario=data['horario_aula'],
        orientador=orientador,
    )

    oficina.save()

    return JsonResponse(
        {
            'success': True,
            'id': oficina.id,
        }, 
        status=201
    )


@csrf_exempt
@require_http_methods(["GET"])
@is_api_authenticated
def get_oficina_by_id(request: HttpRequest, id: str) -> JsonResponse:
    if request.is_admin:
        oficina = Oficinas.objects.filter(id=id, deleted=0)
    
    else:
        oficina = Oficinas.objects.filter(id=id, deleted=0, orientador_id=request.id_user)

    oficina = oficina.values(
        "nome",
        "id",
        "descricao",
        "local",
        "link",
        "horario",
        "orientador__id",
        "orientador__user__nome",
        "created_at",
        "is_active"
    )

    if not oficina.exists():
        return JsonResponse(
            {
                'success': False,
                'msg': 'Id not found'
            }, 
            status= 422
        )

    return JsonResponse(
        {
            'success': True,
            'oficina': oficina[0],
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["GET"])
@is_api_authenticated
def get_oficina(request: HttpRequest) -> JsonResponse:
    if request.is_admin:
        oficina = Oficinas.objects.filter(deleted=0)

    else:
        oficina = Oficinas.objects.filter(deleted=0, orientador_id=request.id_user)

    oficina = oficina.order_by("-id").values(
        "nome",
        "id",
        "descricao",
        "local",
        "link",
        "horario",
        "orientador__id",
        "orientador__user__nome",
        "created_at",
        "is_active"
    )[:30]

    return JsonResponse(
        {
            'success': True,
            'oficina': list(oficina),
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["PUT"])
@validate_dataclass(oficina_update_dto.UpdateOficina)
@has_data_body
@is_api_authenticated
def update_oficina(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    if request.is_admin:
        oficina = Oficinas.objects.filter(id=data['id'], deleted=0)

    else:
        oficina = Oficinas.objects.filter(id=data['id'], deleted=0, orientador_id=request.id_user)

    if not oficina.exists():
        return JsonResponse(
        {
            'success': False,
            'msg': 'Oficina does not exists'
        }, 
        status=200
    )
    
    oficina.update(
        nome=data['nome'], 
        descricao=data['descricao'] , 
        horario=data['horario_aula'] , 
        local=data['local'], 
        link=data['link']
    )

    return JsonResponse(
        {
            'success': True,
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["DELETE"])
@validate_dataclass(oficina_delete_dto.DeleteOficina)
@has_data_body
@is_api_authenticated
def delete_oficina(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    if request.is_admin:
        oficina = Oficinas.objects.filter(id=data['id'], deleted=0)

    else:
        oficina = Oficinas.objects.filter(id=data['id'], deleted=0, orientador_id=request.id_user)

    if not oficina.exists():
        return JsonResponse(
        {
            'success': False,
            'msg': 'Oficina does not exists'
        }, 
        status=200
    )
    
    oficina.update(deleted=1)

    return JsonResponse(
        {
            'success': True,
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(oficina_aluno_create_dto.CreateOficinaAluno)
@has_data_body
@is_api_authenticated
def create_aluno_oficina(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        if request.is_admin:
            oficina = Oficinas.objects.get(id=data['oficina_id'])

        else:
            oficina = Oficinas.objects.get(id=data['oficina_id'], orientador_id=request.id_user)

        aluno = Alunos.objects.get(id=data['aluno_id'])

    except (Alunos.DoesNotExist, Oficinas.DoesNotExist):
        return JsonResponse(
            {
                'success': False,
                'msg': 'Oficina and/or Aluno does not exists'
            }, 
            status=422
        )

    oficina = OficinaAluno(
        oficina=oficina,
        aluno=aluno      
    )

    oficina.save()

    return JsonResponse(
        {
            'success': True,
            'id': oficina.id,
        }, 
        status=201
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_oficina_aluno_by_id(request: HttpRequest, id: str) -> JsonResponse:
    if request.is_admin:
        oficina = OficinaAluno.objects.filter(id=id, deleted=0).values()

    else:
        oficina = OficinaAluno.objects.filter(id=id, deleted=0, orientador_id=request.id_user).values()

    if not oficina.exists():
        return JsonResponse(
            {
                'success': False,
                'msg': 'Id not found'
            }, 
            status= 422
        )

    return JsonResponse(
        {
            'success': True,
            'oficina_aluno': oficina[0],
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["GET"])
@is_api_authenticated
def get_oficina_aluno(request: HttpRequest, id_oficina: str) -> JsonResponse:
    if request.is_admin:
        oficina = OficinaAluno.objects.filter(deleted=0, oficina_id=id_oficina)

    else:
        oficina = OficinaAluno.objects.filter(deleted=0, oficina_id=id_oficina, oficina__orientador_id=request.id_user)

    oficina = oficina.order_by("-id").values(
        "id",
        "oficina__nome",
        "aluno__user__nome",
        "aluno_id",
        "created_at"
    )[:30]

    return JsonResponse(
        {
            'success': True,
            'oficina_alunos': list(oficina),
        }, 
        status=200
    )

@csrf_exempt
@require_http_methods(["GET"])
def get_five_oficina(request: HttpRequest) -> JsonResponse:
    oficina = Oficinas.objects.filter(deleted=0).order_by("-id").values(
        "nome",
        "id",
        "descricao",
        "orientador__user__nome",
        "created_at",
        "is_active"
    )[:6]

    return JsonResponse(
        {
            'success': True,
            'oficina': list(oficina),
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(oficina_delete_dto.DeleteOficina)
@has_data_body
@is_api_authenticated
def get_aluno_oficinas_inscrito(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    oficina = Oficinas.objects.filter(oficinaaluno__aluno_id=data['id'], deleted=0).order_by("-id").values(
        "nome",
        "id",
        "descricao",
        "orientador__user__nome",
        "created_at",
        "horario",
        "is_active"
    )

    return JsonResponse(
        {
            'success': True,
            'oficinas': list(oficina),
        }, 
        status=200
    )