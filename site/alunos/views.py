from core.decorator import is_authenticated
from django.shortcuts import render
from django.http import HttpRequest


@is_authenticated
def listagem(request: HttpRequest):
    return render(request, 'alunos/aluno/listagem.html', context={'active': 'alunos'})


@is_authenticated
def listagem_resp(request: HttpRequest):
    return render(request, 'alunos/responsavel/listagem.html', context={'active': 'resp'})


@is_authenticated
def detalhes(request: HttpRequest, id: str):
    return render(request, 'alunos/aluno/detalhes.html', context={'active': 'alunos', "id": id})


@is_authenticated
def create(request: HttpRequest):
    return render(request, 'alunos/aluno/create.html', context={'active': 'alunos'})


@is_authenticated
def detalhesResp(request: HttpRequest, id: str):
    return render(request, 'alunos/responsavel/detalhes.html', context={'active': 'resp', "id": id})


@is_authenticated
def createResp(request: HttpRequest):
    return render(request, 'alunos/responsavel/create.html', context={'active': 'resp'})
