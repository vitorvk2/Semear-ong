from api.dto.orientador import orientador_create_dto, orientador_delete_dto, orientador_update_dto
from django.views.decorators.http import require_http_methods
from core.decorator import has_data_body, validate_dataclass
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest
from orientador.models import Orientador
from core.models import User
import json


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(orientador_create_dto.CreateOrientador)
@has_data_body
def create_orientador(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        user = User(
            username = data['username'],
            password = make_password(data['senha']),
            nome = data['nome'],
            cpf = data['cpf'],
            data_nasc = data['data_nasc'],
            endereco = data['endereco'],
            bairro = data['bairro'],
            cidade = data['cidade'],
            numero = data['numero'],
            uf = data['uf'],
            cep = data['cep']
        )
        user.save()

    except Exception:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Username or CPF duplicate'
            }, 
            status=422
        )

    orientador = Orientador(
        voluntario = data['voluntario'],
        user = user
    )
    orientador.save()

    return JsonResponse(
        {
            'success': True,
            'id': orientador.id,
        }, 
        status=201
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_orientador_by_id(request: HttpRequest, id: str) -> JsonResponse:
    orientador = Orientador.objects.filter(id=id, deleted=0).values(
        "id",
        "voluntario",
        "created_at",
        "deleted",
        "user__id",
        "user__nome",
        "user__cpf",
        "user__cep",
        "user__cidade",
        "user__endereco",
        "user__bairro",
        "user__numero",
        "user__uf",
        "user__cep",
        "user__data_nasc",
    )

    if not orientador.exists():
        return JsonResponse(
            {
                'success': False,
                'msg': 'Id not found'
            }, 
            status=422
        )

    return JsonResponse(
        {
            'success': True,
            'orientador': orientador[0]
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_orientador(request: HttpRequest) -> JsonResponse:
    orientador = Orientador.objects.filter(deleted=0).order_by("-id").values(
        "id",
        "voluntario",
        "created_at",
        "deleted",
        "user__id",
        "user__nome",
        "user__cpf",
        "user__cep",
        "user__cidade",
        "user__endereco",
        "user__bairro",
        "user__numero",
        "user__uf",
        "user__cep",
        "user__data_nasc",
    )[:30]

    return JsonResponse(
        {
            'success': True,
            'orientadores': list(orientador),
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["PUT"])
@validate_dataclass(orientador_update_dto.UpdateOrientador)
@has_data_body
def update_orientador(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        orientador = Orientador.objects.get(id=data['id'], deleted=0)

    except Orientador.DoesNotExist:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Orientador does not exists'
            }, 
            status=422
        )

    try:
        User.objects.filter(id=orientador.user_id).update(
            data_nasc = data['data_nasc'],
            endereco = data['endereco'],
            bairro = data['bairro'],
            cidade = data['cidade'],
            numero = data['numero'],
            uf = data['uf'],
            cep = data['cep']
        )

    except Exception:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Error'
            }, 
            status=422
        )

    Orientador.objects.filter(id=data['id']).update(voluntario=data['voluntario'])

    return JsonResponse(
        {
            'success': True,
            'msg': 'Updated data'
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["DELETE"])
@validate_dataclass(orientador_delete_dto.DeleteOrientador)
@has_data_body
def delete_orientador(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    orientador = Orientador.objects.filter(id=data['id'], deleted=0)

    if not orientador.exists():
        return JsonResponse(
            {
                'success': False,
                'msg': 'Orientador does not exists'
            }, 
            status=422
        )
    
    orientador.update(deleted=1)

    return JsonResponse(
        {
            'success': True,
        }, 
        status=200
    )
