# Prova de Django - MTV, DRF e JWT

## Instruções

1. Clone este repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Complete as tarefas descritas nos arquivos na pasta `tasks/`
6. <span style="color: red;">O projeto deve ser chamado : servicos </span>
7. Para criar o projeto, crie na pasta raiza, ou seja, `django-admin startproject nome_do_projeto .`
8. Em settings.py, alterar o campo `ALLOWED_HOSTS = []` mudar para `ALLOWED_HOSTS = ['*', 'testserver']`
8. Submeta seu projeto quando terminar

## Tarefas

1. Implementar uma aplicação MTV básica
2. Criar endpoints API com DRF usando @api_view
3. Implementar autenticação JWT com usuário personalizado
