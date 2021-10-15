from core.decorator import is_authenticated
from django.shortcuts import render
from django.http import HttpRequest


@is_authenticated
def listagem(request: HttpRequest):
    return render(request, 'alunos/listagem.html', context={'active': 'alunos'})


@is_authenticated
def detalhes(request: HttpRequest, id: str):
    return render(request, 'alunos/detalhes.html', context={'active': 'alunos', "id": id})

@is_authenticated
def detalhesResp(request: HttpRequest, id: str):
    return render(request, 'alunos/detalhesResp.html', context={'active': 'alunos', "id": id})

@is_authenticated
def create(request: HttpRequest):
    return render(request, 'alunos/create.html', context={'active': 'alunos'})

@is_authenticated
def createResp(request: HttpRequest):
    return render(request, 'alunos/createresp.html', context={'active': 'alunos'})
