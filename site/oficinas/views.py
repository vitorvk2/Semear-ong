from core.decorator import is_authenticated
from django.shortcuts import render
from django.http import HttpRequest


@is_authenticated
def listagem(request: HttpRequest):
    return render(request, 'oficinas/listagem.html', context={'active': 'oficinas', 'admin': request.is_admin})


@is_authenticated
def detalhes(request: HttpRequest, id: str):
    return render(request, 'oficinas/detalhes.html', context={'active': 'oficinas', "id": id, 'admin': request.is_admin})


@is_authenticated
def criar(request: HttpRequest):
    return render(request, 'oficinas/create.html', context={'active': 'oficinas', 'admin': request.is_admin})
