from django.urls import path
from . import views

urlpatterns = [
    # do servico
    path('servicos/', view=views.listar_servicos, name='listar_servicos'),
    path('criar/servico', view=views.criar_servico, name='criar_servico'),
    path('detalhe/servico<int:id>/', view=views.detalhes_servico, name='detalhes_servico'),
    # do agendamento
    path('agendamentos/', view=views.listar_agendamentos, name='listar_agendamentos'),
    path('criar/agendamentos/',view=views.criar_agendamento, name='criar_agendamento'),
    path('detalhes/agendamentos/<int:id>/', view=views.detalhes_agendamento, name='detalhes_agendamento'),
]

