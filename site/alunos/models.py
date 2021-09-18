from django.db import models
from core.models import User


class Responsavel(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15, unique=True)
    data_nasc = models.DateField()
    tel = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(default=0)


class Alunos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(default=0)