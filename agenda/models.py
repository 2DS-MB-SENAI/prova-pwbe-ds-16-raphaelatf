from django.db import models

#--------------------------Servicos-------------------------------

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.PositiveIntegerField()  # Duração minutos
    preco = models.DecimalField(max_digits=6, decimal_places=2)  # preço com até 6 dígitos e 2 casas decimais

    def __str__(self):
        return self.nome

#--------------------------Agendamento-------------------------------

class Agendamento(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)  # fazendo o relacionamento com Servico
    data_hora = models.DateTimeField()
    cliente_nome = models.CharField(max_length=100)
    cliente_email = models.EmailField()

    def __str__(self):
        return f'{self.cliente_nome} - {self.servico.nome} - {self.data_hora}'
        #vai retornar o nome do cliente, serviço e hora