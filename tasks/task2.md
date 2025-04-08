# 🌐 Tarefa 2 - Implementação de API com @api_view

## 📌 Objetivo
Desenvolver endpoints RESTful utilizando exclusivamente o decorator `@api_view` do Django REST Framework, sem implementação de autenticação.

## Aplicação
- A aplicação devera ser chamada de `agenda`

## 🛠 Modelo de Dados
Implementar um sistema de agendamento com os seguintes modelos:
Servico:
| Field             | Type          | 
|-------------------|---------------|
| `nome`           | CharField -> max_length=100    | 
| `duracao`         | PositiveIntegerField     | 
| `preco`      | DecimalField -> max_digits=6,decimal_places=2     | 

Agendamento:
| Field             | Type          | 
|-------------------|---------------|
| `servico`           | ForeignKey -> Servico, on_delete=models.CASCADE    | 
| `data_hora`         | DateTimeField     | 
| `cliente_nome`      | CharField -> max_length=100    | 
| `cliente_email`      | EmailField   | 


## 🌐 Endpoints Requeridos
### Serviços
- GET /api/servicos/ - Lista todos os serviços disponíveis
- POST /api/servicos/ - Cria um novo serviço
- GET /api/servicos/<id>/ - Detalhes de um serviço específico

### Agendamentos
- GET /api/agendamentos/ - Lista todos os agendamentos
- POST /api/agendamentos/ - Cria novo agendamento
- GET /api/agendamentos/<id>/ - Detalhes de um agendamento



  