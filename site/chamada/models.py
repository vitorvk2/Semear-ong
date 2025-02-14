from oficinas.models import Oficinas
from alunos.models import Alunos
from django.db import models


class Chamada(models.Model):
    decricao = models.TextField()
    oficina = models.ForeignKey(Oficinas, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(default=0, db_index=True)


class ChamadaAluno(models.Model):
    chamada = models.ForeignKey(Chamada, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    presente = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(default=0, db_index=True)