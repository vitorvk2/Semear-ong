from orientador.models import Orientador
from alunos.models import Alunos
from functools import partial
from django.db import models


def random_image_name(field_name, instance, filename):
    newName = "%s.%s" % (User.objects.make_random_password(10), filename.split('.')[-1])
    return '/'.join([instance.__class__.__name__.lower(), field_name, newName])


class Oficinas(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    descricao = models.TextField()
    local = models.CharField(max_length=200, null=True, blank=True, db_index=True)
    link = models.CharField(max_length=300, null=True, blank=True, db_index=True)
    horario = models.TimeField()
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(default=0, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)


class OficinaImagem(models.Model):
    oficina = models.ForeignKey(Oficinas, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=partial(random_image_name, 'media'), blank=True)
    created_at = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(default=0)


class OficinaAluno(models.Model):
    oficina = models.ForeignKey(Oficinas, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(default=0, db_index=True)