from django.db import models
from funcionarios.models import Funcionario


# Create your models here.
class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, help_text='Motimo da Hora Extra')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.motivo
