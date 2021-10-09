from django.shortcuts import render
from django.http import HttpRequest


def index(request: HttpRequest):
    return render(request, 'index.html')


def login_semear(request: HttpRequest):
    return render(request, 'login.html')