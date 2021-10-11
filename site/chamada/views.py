from core.decorator import is_authenticated
from django.shortcuts import render
from django.http import HttpRequest


@is_authenticated
def listagem(request: HttpRequest, id_oficina: str):
    return render(request, 'chamada/listagem.html', context={'active': 'oficinas', 'id': id_oficina})


@is_authenticated
def create(request: HttpRequest, id_oficina: str):
    return render(request, 'chamada/create.html', context={'active': 'oficinas', 'id': id_oficina})


@is_authenticated
def listagem_aluno(request: HttpRequest, id_chamada: str):
    return render(request, 'chamada/listagem_aluno_chamada.html', context={'active': 'oficinas', 'id': id_chamada})

