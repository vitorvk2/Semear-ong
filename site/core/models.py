from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import gettext
from django.core import validators
from django.urls import reverse
from django.db import models
import re


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        gettext('Apelido'),
        max_length=40,
        unique=True,
        validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                gettext('O nome do usuário só pode conter letras digitos ou os seguintes caraters: @/./+/-/_'),
                'invalid'
            )
        ]
    )

    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15, unique=True)
    data_nasc = models.DateField()
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    numero = models.IntegerField()
    uf = models.CharField(max_length=2)
    cep = models.IntegerField()

    is_active = models.BooleanField(gettext('Esta ativo?'), blank=True, default=True)
    is_staff = models.BooleanField(gettext('equipe'), blank=True, default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(gettext('Data de Criacao'), auto_now_add=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.name or self.username

    def save(self, *args, **kwargs):
        return super(User, self).save(*args, **kwargs)