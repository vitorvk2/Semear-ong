from api.dto.aluno import aluno_create_dto, aluno_update_dto, aluno_delete_dto, aluno_aluno_create_dto
from django.views.decorators.http import require_http_methods
from core.decorator import has_data_body, validate_dataclass
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest
from oficinas.models import Oficinas
from alunos.models import Alunos, Responsavel
from core.models import User
import json


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(aluno_create_dto.CreateAluno)
@has_data_body
def create_aluno(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        responsavel = Responsavel.objects.get(id=data['responsavel'])

    except Responsavel.DoesNotExist:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Responsavel does not exists'
            }, 
            status=422
        )
    user = User(
        username = data['username'],
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

    aluno = Alunos(
        responsavel = responsavel,
        user = user
    )
    aluno.save()

    return JsonResponse(
        {
            'success': True,
            'id': aluno.id,
        }, 
        status=201
    )


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(aluno_create_dto.CreateResponsavel)
@has_data_body
def create_responsavel(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    responsavel = Responsavel(
        nome = data['nome'],
        cpf = data['cpf'],
        data_nasc = data['data_nasc'],
        tel = data['tel']
    )
    responsavel.save()

    return JsonResponse(
        {
            'success': True,
            'id': responsavel.id,
        }, 
        status=201
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_aluno_by_id(request: HttpRequest, id: str) -> JsonResponse:
    aluno = Alunos.objects.filter(id=id, deleted=0).values()

    if not aluno.exists():
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
            'chamada': aluno[0],
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_chamada(request: HttpRequest) -> JsonResponse:
    chamada = Chamada.objects.filter(deleted=0).order_by("-id").values()[:30]

    return JsonResponse(
        {
            'success': True,
            'chamadas': list(chamada),
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["PUT"])
#@validate_dataclass(chamada_update_dto.UpdateChamada)
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
#@validate_dataclass(chamada_delete_dto.DeleteChamada)
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
#@validate_dataclass(chamada_aluno_create_dto.CreateChamadaAluno)
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
def get_chamada_aluno_by_id(request: HttpRequest, id: str) -> JsonResponse:
    chamada = ChamadaAluno.objects.filter(id=id, deleted=0).values()

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
def get_chamada_aluno(request: HttpRequest) -> JsonResponse:
    chamada = ChamadaAluno.objects.filter(deleted=0).order_by("-id").values()[:30]

    return JsonResponse(
        {
            'success': True,
            'chamada_alunos': list(chamada),
        }, 
        status=200
    )