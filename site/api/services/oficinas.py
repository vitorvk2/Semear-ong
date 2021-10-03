from django.views.decorators.http import require_http_methods
from core.decorator import has_data_body, validate_dataclass
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest
import json
from api.dto.oficina import oficina_create_dto
from orientador.models import Orientador
from oficinas.models import Oficinas
from alunos.models import Alunos



@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(oficina_create_dto.CreateOficina)
@has_data_body
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
def get_oficina_by_id(request: HttpRequest, id: str) -> JsonResponse:
    oficina = Oficina.objects.filter(id=id, deleted=0).values()

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
def get_oficina(request: HttpRequest) -> JsonResponse:
    oficina = Oficina.objects.filter(deleted=0).order_by("-id").values()[:30]

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
def update_oficina(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    oficina = Oficina.objects.filter(id=data['id'], deleted=0)

    if not oficina.exists():
        return JsonResponse(
        {
            'success': False,
            'msg': 'Oficina does not exists'
        }, 
        status=200
    )
    
    oficina.update(nome=data['nome'])
    oficina.update(decricao=data['descricao'])
    oficina.update(horario=data['horario_aula'])
    oficina.update(local=data['local'])
    oficina.update(link=data['link'])

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
def delete_oficina(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    oficina = Oficina.objects.filter(id=data['id'], deleted=0)

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
@validate_dataclass(oficina_aluno_create_dto.CreateOficina)
@has_data_body
def create_aluno_oficina(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        orientador = Orientador.objects.get(id=data['orientador'])
        aluno = Alunos.objects.get(id=data['aluno_id'])

    except Orientador.DoesNotExist:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Orientador and/or Aluno does not exists'
            }, 
            status=422
        )

    oficina = OficinaAluno(
        orientador=orientador,
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
    oficina = OficinaAluno.objects.filter(id=id, deleted=0).values()

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
def get_oficina_aluno(request: HttpRequest) -> JsonResponse:
    oficina = OficinaAluno.objects.filter(deleted=0).order_by("-id").values()[:30]

    return JsonResponse(
        {
            'success': True,
            'oficina_alunos': list(oficina),
        }, 
        status=200
    )