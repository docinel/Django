from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento',
                                       auto_now=False, auto_now_add=False)
    data_criacao = models.DateTimeField(verbose_name='Data da Criacao',
                                        auto_now=True, auto_now_add=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


class Meta:
    db_table = 'evento'


def __str__(self):
    return self.titulo


def get_data_evento(self):
    return self.data_evento.strftime('%d/%m/%Y %H:%M')


def input_evento(self):
    return self.data_evento.strftime('%Y-%m-%dT%H:%M')
