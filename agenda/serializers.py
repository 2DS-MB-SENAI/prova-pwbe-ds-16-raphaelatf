from rest_framework import serializers
from .models import Servico, Agendamento

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['id', 'nome', 'duracao', 'preco'] #fields para incluir quais campos quero na saida

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['id', 'servico', 'data_hora', 'cliente_nome', 'cliente_email']
