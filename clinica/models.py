from django.db import models
import re
from django.core.exceptions import ValidationError
from datetime import datetime, timezone


#--------------------------MÉDICO-------------------------------



# Função para validar o CRM
def validar_crm(value):
    if not re.match(r'^\d{2}/\d{5}$', value):
        raise ValidationError('CRM deve estar no formato XX/XXXXX.')

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    # escolha para especialidade
    escolhas_especialidade = (
    ('clinico', 'Clínico Geral'),
    ('cardiologia', 'Cardiologia'),
    ('neurologia', 'Neurologia'),
    ('ortopedia', 'Ortopedia'),
    ('psicologia', 'Psicologia'),
    ('pediatria', 'Pediatria')
    )
    especialidade = models.CharField(max_length=50, choices=escolhas_especialidade)
    crm = models.CharField(max_length=10, unique=True, validators=[validar_crm])
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome
    

    
#--------------------------CONSULTA-------------------------------


# Função para validar a data da consulta
def validar_data_futura(value):
    if value < datetime.now(timezone.utc):
        raise ValidationError('A consulta não pode ser agendada no passado.')

class Consulta(models.Model):
    paciente = models.CharField(max_length=100)
    data = models.DateTimeField(validators=[validar_data_futura])
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    escolha_status = (
    ('agendado', 'Agendado'),
    ('realizado', 'Realizado'),
    ('cancelado', 'Cancelado'),)
    status = models.CharField(max_length=10, choices=escolha_status, default='agendado')

    def __str__(self):
        return f'{self.paciente} - {self.medico.nome}'
