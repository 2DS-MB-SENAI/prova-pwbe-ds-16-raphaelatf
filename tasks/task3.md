# 🔐 Tarefa 3 - Autenticação Customizada com JWT

## 📌 Objetivo
Implementar um sistema completo de autenticação com:
- Modelo de usuário personalizado (Custom User)
- Autenticação por tokens JWT
- Endpoints protegidos com `permission_classes`
- User registration e profile management


## Aplicação
- A aplicação devera ser chamada de `custom_auth`

## 🛠 Requisitos Técnicos

### 1. Modelo `CustomUser`
Estender `AbstractUser` e adicionar:

| Field             | Type          | Validações                      |
|-------------------|---------------|---------------------------------|
| `phone`           | CharField     |  unique |
| `address`         | TextField     | Opcional                        |
| `birth_date`      | DateField     | Opcional, deve ser data passada |
| `is_verified`     | BooleanField  | Default=False                   |

### 2. Configuração Necessária
```python
# settings.py
AUTH_USER_MODEL = 'custom_auth.CustomUser'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'UPDATE_LAST_LOGIN': True,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```
# 🌐 Endpoints
## 🔓 Públicos
### User Registration

```json
POST /auth/register/
{
    "username": "newuser",
    "password": "SecurePass123!",
    "phone": "+5511999999999",
    "address": "123 Main St",
    "birth_date": "1990-01-01"
}
```

### User Login

```json
POST /auth/login/
{
    "username": "newuser",
    "password": "SecurePass123!"
}
```

## 🔐 Protegidos (Requerem JWT)
### Get User Profile
```
GET /auth/profile/
```

### Update Profile
```
PATCH /auth/profile/
{
    "address": "456 Oak Ave",
    "birth_date": "1990-01-15"
}
```

## ⚙️ Requisitos de Implementação

- User Registration:
  - Password requirements -> Use a biblioteca re:
    - Min 8 caracteres
    - 1 letra maiúscula
    - 1 número
    - 1 caractere especial

- Authentication:
  - Implementar JWT token generation
  - Usar @permission_classes([IsAuthenticated])
  - Status codes:
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden

- Profile Management:
  - Users só podem acessar próprio profile
  - Não expor password nas responses
