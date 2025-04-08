from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Servico, Agendamento
from .serializers import ServicoSerializer, AgendamentoSerializer #importa os serializers

#-------------------Servicos------------------

# listando todos os serviços disponíveis aaa✓
@api_view(['GET'])
def listar_servicos(request):
    servicos = Servico.objects.all()
    serializer = ServicoSerializer(servicos, many=True)
    return Response(serializer.data)

# criando um novo serviço ✓
@api_view(['POST'])
def criar_servico(request):
    if request.method == 'POST':
        serializer = ServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# detalh um servico especifico ✓
@api_view(['GET'])
def detalhes_servico(request, id):
    try:
        servico = Servico.objects.get(pk=id)
    except Servico.DoesNotExist:
        return Response({'erro': 'Servico não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ServicoSerializer(servico)
    return Response(serializer.data)


#-------------------Agendamento------------------

# listando todos os agendamentos ✓
@api_view(['GET'])
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    serializer = AgendamentoSerializer(agendamentos, many=True)
    return Response(serializer.data)

# criando um novo agendamento✓
@api_view(['POST'])
def criar_agendamento(request):
    if request.method == 'POST':
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# detalhes de um agendamento específico✓
@api_view(['GET'])
def detalhes_agendamento(request, id):
    try:
        agendamento = Agendamento.objects.get(pk=id)
    except Agendamento.DoesNotExist:
        return Response({'erro': 'Agendamento não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = AgendamentoSerializer(agendamento)
    return Response(serializer.data)
