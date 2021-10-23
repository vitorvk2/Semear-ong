from core.decorator import is_authenticated
from django.shortcuts import render
from django.http import HttpRequest


@is_authenticated
def listagem(request: HttpRequest):
    return render(request, 'orientador/listagem.html', context={'active': 'orientador'})

@is_authenticated
def create(request: HttpRequest):
    return render(request, 'orientador/create.html', context={'active': 'orientador'})