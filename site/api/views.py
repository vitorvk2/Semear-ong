from core.decorator import has_data_body, validate_dataclass, is_api_authenticated
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from django.contrib.auth import authenticate
from orientador.models import Orientador
from api.utils import get_pairs_token
from django.shortcuts import render
from alunos.models import Alunos
from api.dto import login_dto
from core.models import User
import json


@csrf_exempt
@has_data_body
@require_http_methods(["POST"])
@validate_dataclass(login_dto.MakeLogin)
def make_login_interno(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body)

    user = User.objects.filter(username=data['username'])

    if not user.exists():
        return JsonResponse(
            {
                'success': False,
                'msg': 'Orientador does not exists'
            }, 
            status=422
        )

    orientador = Orientador.objects.filter(user_id=user[0].id)

    if not orientador.exists():
        return JsonResponse(
            {
                'success': False,
                'msg': 'Orientador does not exists'
            }, 
            status=422
        )

    user_auth = authenticate(username=data['username'], password=data['password'])

    if user_auth and user_auth.is_active:
        orientador_dados = {
            'id': orientador[0].id,
            'is_admin': orientador[0].is_admin,
            'name': user[0].nome
        }
        
        token, validate = get_pairs_token(orientador_dados)

        return JsonResponse({
            "data": orientador_dados,
            'token': token,
            "validate": validate,
            'success': True,
        }, status=200)

    return JsonResponse(
        {
            'success': False,
            'msg': 'User and/or email incorrect'
        }, 
        status=401
    )


@csrf_exempt
@has_data_body
@require_http_methods(["POST"])
@validate_dataclass(login_dto.MakeLogin)
def make_login_aluno(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body)

    user = User.objects.filter(username=data['username'])

    if not user.exists():
        return JsonResponse(
            {
                'success': False,
                'msg': 'Aluno does not exists'
            }, 
            status=422
        )

    aluno = Alunos.objects.filter(user_id=user[0].id)

    if not aluno.exists():
        return JsonResponse(
            {
                'success': False,
                'msg': 'Aluno does not exists'
            }, 
            status=422
        )

    user_auth = authenticate(username=data['username'], password=data['password'])

    if user_auth and user_auth.is_active:
        aluno_dados = {
            'id': aluno[0].id,
            'is_admin': False,
            'name': user[0].nome
        }
        
        token, validate = get_pairs_token(aluno_dados)

        return JsonResponse({
            "data": aluno_dados,
            'token': token,
            "validate": validate,
            'success': True,
        }, status=200)

    return JsonResponse(
        {
            'success': False,
            'msg': 'User and/or email incorrect'
        }, 
        status=401
    )


@csrf_exempt
@is_api_authenticated
@require_http_methods(["POST"])
def validate_login(request: HttpRequest) -> JsonResponse:
    return JsonResponse({
        'success': True,
    }, status=200)