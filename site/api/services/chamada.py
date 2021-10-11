from api.dto.chamada import chamada_create_dto, chamada_update_dto, chamada_delete_dto, chamada_aluno_create_dto
from django.views.decorators.http import require_http_methods
from core.decorator import has_data_body, validate_dataclass
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest
from chamada.models import Chamada, ChamadaAluno
from oficinas.models import Oficinas
from alunos.models import Alunos
import json


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(chamada_create_dto.CreateChamada)
@has_data_body
def create_chamada(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        oficina = Oficinas.objects.get(id=data['oficina'])

    except Oficinas.DoesNotExist:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Oficina does not exists'
            }, 
            status=422
        )

    chamada = Chamada(
        decricao=data['descricao'],
        oficina=oficina
    )

    chamada.save()

    return JsonResponse(
        {
            'success': True,
            'id': chamada.id,
        }, 
        status=201
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_chamada_by_id(request: HttpRequest, id_oficina: str, id: str) -> JsonResponse:
    chamada = Chamada.objects.filter(id=id, oficina_id=id_oficina, deleted=0).values()

    if not chamada.exists():
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
            'chamada': chamada[0],
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_chamada(request: HttpRequest, id_oficina: str) -> JsonResponse:
    chamada = Chamada.objects.filter(deleted=0, oficina_id=id_oficina).order_by("-id").values()[:30]

    return JsonResponse(
        {
            'success': True,
            'chamadas': list(chamada),
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["PUT"])
@validate_dataclass(chamada_update_dto.UpdateChamada)
@has_data_body
def update_chamada(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    chamada = Chamada.objects.filter(id=data['id'], deleted=0)

    if not chamada.exists():
        return JsonResponse(
        {
            'success': False,
            'msg': 'Chamada does not exists'
        }, 
        status=200
    )
    
    chamada.update(decricao=data['descricao'])

    return JsonResponse(
        {
            'success': True,
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["DELETE"])
@validate_dataclass(chamada_delete_dto.DeleteChamada)
@has_data_body
def delete_chamada(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    chamada = Chamada.objects.filter(id=data['id'], deleted=0)

    if not chamada.exists():
        return JsonResponse(
        {
            'success': False,
            'msg': 'Chamada does not exists'
        }, 
        status=200
    )
    
    chamada.update(deleted=1)

    return JsonResponse(
        {
            'success': True,
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(chamada_aluno_create_dto.CreateChamadaAluno)
@has_data_body
def create_chamada_aluno(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        chamada = Chamada.objects.get(id=data['chamada_id'])
        aluno = Alunos.objects.get(id=data['aluno_id'])

    except (Oficinas.DoesNotExist, Alunos.DoesNotExist()):
        return JsonResponse(
            {
                'success': False,
                'msg': 'Chamada and/or Aluno does not exists'
            }, 
            status=422
        )

    chamada = ChamadaAluno(
        chamada=chamada,
        aluno=aluno,
        presente=data['presente']
    )

    chamada.save()

    return JsonResponse(
        {
            'success': True,
            'id': chamada.id,
        }, 
        status=201
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_chamada_aluno_by_id(request: HttpRequest, id_chamada: str, id: str) -> JsonResponse:
    chamada = ChamadaAluno.objects.filter(id=id, chamada_id=id_chamada, deleted=0).values()

    if not chamada.exists():
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
            'chamada_aluno': chamada[0],
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_chamada_aluno(request: HttpRequest, id_chamada: str) -> JsonResponse:
    chamada = ChamadaAluno.objects.filter(deleted=0, chamada_id=id_chamada).order_by("-id").values(
        "id",
        "chamada",
        "chamada__oficina__nome",
        "aluno__user__nome",
        "presente",
        "created_at",
    )

    return JsonResponse(
        {
            'success': True,
            'chamada_alunos': list(chamada),
        }, 
        status=200
    )