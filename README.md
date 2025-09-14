🌤️ Weather API

API REST desenvolvida com Django REST Framework (DRF) que consome a API pública da OpenWeather para consultar dados climáticos em tempo real.
O projeto permite que usuários autenticados consultem o clima de uma cidade e salvem cidades favoritas para consultas futuras.

📌 Funcionalidades

🔐 Autenticação JWT (login, refresh token).

👤 Cadastro de usuários com username, email, senha e cidade.

🌍 Consulta de clima em tempo real usando a API pública da OpenWeather.

⭐ Favoritar cidades (apenas cidade e país, sem histórico de clima).

📋 Listagem de cidades favoritas do usuário autenticado.

❌ Remover cidades favoritas.

🛠️ Tecnologias Utilizadas

Python 3.12+

Django 5

Django REST Framework

Simple JWT

PostgreSQL

Requests

OpenWeather API

📂 Estrutura do Projeto
weather_api/
│-- core/ # Configurações principais do Django
│-- weather/ # App principal da API
│-- templates/ # (Opcional) Templates HTML/MVT
│-- .env # Variáveis de ambiente (não versionar)
│-- .gitignore
│-- requirements.txt
│-- docker-compose.yml # (se usar Docker)
│-- README.md

⚙️ Configuração do Ambiente
1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/weather_api.git
cd weather_api

2️⃣ Criar e ativar um ambiente virtual
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Criar o arquivo .env

Exemplo:

# Django

SECRET_KEY=django-insecure-sua-chave
DEBUG=1
ALLOWED_HOSTS=127.0.0.1,localhost

# PostgreSQL

DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=weather_database
DB_HOST=localhost
DB_PORT=5432

# OpenWeather

OPENWEATHER_API_KEY=sua_chave_api

🔑 A chave da OpenWeather pode ser gerada gratuitamente em: https://home.openweathermap.org/api_keys

5️⃣ Rodar as migrações
python manage.py migrate

6️⃣ Criar superusuário (opcional)
python manage.py createsuperuser

7️⃣ Rodar o servidor
python manage.py runserver

🔐 Autenticação

A API utiliza JWT (JSON Web Token).
Endpoints principais:

POST /api/users/ → Criação de usuário.

POST /api/token/ → Obter token de acesso e refresh.

POST /api/token/refresh/ → Renovar token de acesso.

Exemplo de login:

{
"username": "ruann",
"password": "123456"
}

Resposta:

{
"refresh": "eyJhbGciOiJIUzI1NiIsInR...",
"access": "eyJhbGciOiJIUzI1NiIsInR..."
}

🌍 Endpoints da API
🔹 Usuários

POST /api/users/ → Criar usuário.

GET /api/users/ → Listar dados do usuário logado.

PUT /api/users/{id}/ → Atualizar usuário logado.

🔹 Clima

GET /api/weather/?city=Recife → Retorna clima em tempo real de Recife.

🔹 Favoritos

GET /api/weather/history/ → Listar cidades favoritas do usuário.

POST /api/weather/history/ → Criar favorito (cidade/país).

GET /api/weather/history/{id}/ → Buscar clima atualizado da cidade favorita.

DELETE /api/weather/history/{id}/ → Remover favorito.
