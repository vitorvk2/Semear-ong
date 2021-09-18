from core.models import User
from django.db import models


class Orientador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voluntario = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    deleted = models.IntegerField(default=0)