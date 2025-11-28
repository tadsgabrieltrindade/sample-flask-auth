# sample-flask-auth

Repositório criado para armazenar o código da API de autenticação com banco de dados

## 📋 Sobre o Projeto

API REST desenvolvida em Python utilizando Flask para demonstrar conceitos fundamentais de autenticação e persistência de dados. O projeto implementa endpoints para login e uma rota básica de verificação da API.

## 🎯 Principais Conceitos Aplicados

### 1. **Framework Flask**
- **O que é**: Flask é um microframework web para Python que permite criar APIs e aplicações web de forma simples e flexível
- **Aplicação no código**: Utilizado para criar rotas HTTP (`@app.route`), processar requisições e retornar respostas JSON

### 2. **Rotas e Métodos HTTP**
- **O que são**: Rotas definem os endpoints da API; métodos HTTP (GET, POST, etc.) indicam o tipo de operação
- **Aplicação no código**:
  - `@app.route('/login', methods=['POST'])` - Rota para autenticação que aceita dados via POST
  - `@app.route("/", methods=['GET'])` - Rota raiz que retorna status da API via GET

### 3. **Manipulação de Requisições e Respostas**
- **request.json**: Extrai dados JSON enviados pelo cliente na requisição
- **jsonify()**: Converte dicionários Python em respostas JSON formatadas
- **Status Codes HTTP**: 
  - `200` - Sucesso
  - `401` - Não autorizado (credenciais inválidas)
  - `500` - Erro interno do servidor

### 4. **ORM (Object-Relational Mapping) com SQLAlchemy**
- **O que é**: SQLAlchemy é uma ferramenta que permite trabalhar com bancos de dados usando objetos Python ao invés de SQL puro
- **Flask-SQLAlchemy**: Extensão que integra SQLAlchemy ao Flask
- **Aplicação no código**:
  - `db = SQLAlchemy()` em `database.py` - Instância do ORM
  - `db.init_app(app)` - Vincula o banco de dados à aplicação Flask
  - `db.create_all()` - Cria as tabelas no banco de dados automaticamente

### 5. **Modelos de Dados (Models)**
- **O que são**: Classes Python que representam tabelas do banco de dados
- **Aplicação no código** (`models/user.py`):
  ```python
  class User(db.Model, UserMixin):
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(50), nullable=False, unique=True)
      password = db.Column(db.String(50), nullable=False)
  ```
  - `db.Model`: Herança que transforma a classe em um modelo SQLAlchemy
  - `db.Column`: Define colunas da tabela com tipos e restrições
  - `primary_key=True`: Define a chave primária
  - `unique=True`: Garante valores únicos na coluna
  - `nullable=False`: Campo obrigatório

### 6. **Flask-Login (Gerenciamento de Sessões)**
- **O que é**: Extensão do Flask para gerenciar sessões de usuários autenticados
- **UserMixin**: Classe que fornece implementações padrão para métodos de autenticação
- **LoginManager**: Gerenciador que coordena o processo de login/logout
- **Aplicação no código**:
  - `LoginManager()` inicializa o gerenciador de login
  - `UserMixin` é herdado pela classe `User` para adicionar funcionalidades de autenticação

### 7. **Configuração da Aplicação**
- **SECRET_KEY**: Chave secreta usada para criptografar sessões e cookies
- **SQLALCHEMY_DATABASE_URI**: String de conexão com o banco de dados
  - `sqlite:///database.db` - Usa SQLite (banco de dados em arquivo local)

### 8. **Context Manager (app.app_context)**
- **O que é**: Contexto de aplicação que permite acessar recursos do Flask fora de uma requisição
- **Aplicação no código**:
  ```python
  with app.app_context():
      db.create_all()
  ```
  - Necessário para criar tabelas antes da aplicação começar a receber requisições

### 9. **Tratamento de Exceções**
- **try/except**: Captura erros durante a execução para evitar que a aplicação quebre
- **Aplicação no código**: Bloco try/except na rota `/login` retorna erro 500 se algo falhar

### 10. **Validação de Dados**
- **Aplicação no código**:
  ```python
  username = data.get("username")
  password = data.get("password")
  if username and password:
      # Processa autenticação
  ```
  - Verifica se campos obrigatórios foram enviados antes de processar

### 11. **Modo Debug**
- **O que é**: Modo de desenvolvimento que recarrega automaticamente o servidor quando o código muda e mostra erros detalhados
- **Aplicação no código**: `app.run(debug=True)`

## 🗂️ Estrutura do Projeto

```
sample-flask-auth/
├── app.py              # Arquivo principal com rotas e configurações
├── database.py         # Configuração do SQLAlchemy
├── models/
│   └── user.py        # Modelo de dados do usuário
├── requirements.txt    # Dependências do projeto
├── instance/          # Pasta onde o SQLite armazena o database.db
└── README.md          # Documentação
```

## 🚀 Como Executar

1. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

2. **Execute a aplicação**:
```bash
python app.py
```

3. **A API estará disponível em**: `http://127.0.0.1:5000`

## 📍 Endpoints

### GET /
- **Descrição**: Verifica se a API está funcionando
- **Resposta**: 
  ```json
  {
    "message": "API running"
  }
  ```
- **Status**: 200

### POST /login
- **Descrição**: Endpoint de autenticação (em desenvolvimento)
- **Body**:
  ```json
  {
    "username": "seu_usuario",
    "password": "sua_senha"
  }
  ```
- **Respostas**:
  - 200: Autenticação bem-sucedida
  - 401: Credenciais inválidas
  - 500: Erro no servidor

## 📚 Tecnologias Utilizadas

- **Python 3.x**
- **Flask 2.3.0** - Framework web
- **Flask-Login 0.6.3** - Gerenciamento de autenticação
- **Flask-SQLAlchemy 3.1.1** - ORM para banco de dados
- **SQLite** - Banco de dados relacional leve

## 🎓 Conceitos Python Fundamentais Aplicados

- **Importações de módulos**: `from flask import Flask`
- **Decoradores**: `@app.route()` - Funções que modificam outras funções
- **Dicionários**: `data.get("username")` - Estrutura chave-valor
- **Métodos de classe**: `db.init_app(app)`
- **Herança de classes**: `class User(db.Model, UserMixin)` - Herança múltipla
- **Condicional if/else**: Validação de dados
- **Blocos with**: Gerenciamento de contexto
- **Tuplas**: `return jsonify(...), 200` - Retorno de múltiplos valores