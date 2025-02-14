from django.db import models
from core.models import User


class Responsavel(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    cpf = models.CharField(max_length=15, unique=True, db_index=True)
    data_nasc = models.DateField()
    tel = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(default=0, db_index=True)


class Alunos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(default=0, db_index=True)