# 🚗 Cars - Django Project

Um projeto Django para gerenciamento completo de automóveis, incluindo cadastro de carros, marcas, inventário automático e sistema de autenticação de usuários.

## 📋 Descrição

O **Cars** é uma aplicação web desenvolvida com Django que permite aos usuários gerenciar uma frota de veículos. Inclui funcionalidades para cadastrar carros com detalhes como modelo, marca, anos de fabricação, placa, valor, foto e biografia. O sistema mantém um inventário automático atualizado via sinais (signals) do Django e oferece uma interface administrativa completa. Além disso, inclui um sistema de autenticação para usuários se registrarem e fazerem login.

## 🎯 Funcionalidades

- ✅ Cadastro, edição e exclusão de carros
- ✅ Gerenciamento de marcas de veículos
- ✅ Upload de fotos para os carros
- ✅ Inventário automático com contagem e valor total dos carros
- ✅ Sistema de autenticação de usuários (registro e login)
- ✅ Interface administrativa do Django
- ✅ Templates responsivos para visualização e gerenciamento
- ✅ Banco de dados SQLite para desenvolvimento

## 🛠️ Tecnologias Utilizadas

- **Framework**: Django 6.0.2
- **Linguagem**: Python 3.12
- **Banco de Dados**: SQLite (desenvolvimento)
- **Gerenciador de Pacotes**: pip
- **Bibliotecas Adicionais**:
  - Pillow (para manipulação de imagens)
  - httpx (para requisições HTTP)
  - pydantic (para validação de dados)
- **WSGI**: Python WSGI HTTP Server

## 📦 Pré-requisitos

- Python 3.12+
- pip (gerenciador de pacotes Python)
- Ambiente virtual (venv)

## 🚀 Instalação e Configuração

### 1. Clone o repositório

```bash
git clone <seu-repositório>
cd cars
```

### 2. Crie e ative o ambiente virtual

```bash
# Criar ambiente virtual
python3 -m venv venv_cars

# Ativar ambiente virtual (Linux/Mac)
source venv_cars/bin/activate

# Ativar ambiente virtual (Windows)
venv_cars\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Ou instale o Django manualmente:

```bash
pip install django==6.0.2
```

### 4. Configure o banco de dados

```bash
python manage.py migrate
```

### 5. Crie um superusuário (administrador)

```bash
python manage.py createsuperuser
```

## ▶️ Como Executar

### Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

O servidor estará disponível em: `http://127.0.0.1:8000/`

### Acesse o painel administrativo

```
http://127.0.0.1:8000/admin/
```

Utilize as credenciais do superusuário criado anteriormente.

## 📁 Estrutura do Projeto

```
cars/
├── app/                      # Configuração principal do Django
│   ├── settings.py          # Configurações do projeto
│   ├── urls.py              # Rotas principais
│   ├── wsgi.py              # Configuração WSGI
│   ├── asgi.py              # Configuração ASGI
│   └── templates/
│       └── base.html        # Template base
├── accounts/                 # App de autenticação
│   ├── models.py            # Modelos de usuário (se houver)
│   ├── views.py             # Views para login/registro
│   ├── admin.py             # Configuração do admin
│   ├── apps.py              # Configuração do app
│   ├── tests.py             # Testes
│   ├── migrations/          # Migrações
│   └── templates/
│       ├── login.html       # Template de login
│       └── register.html    # Template de registro
├── cars/                     # App principal para gerenciamento de carros
│   ├── models.py            # Modelos: Car, Brand, CarInventory
│   ├── views.py             # Views para CRUD de carros
│   ├── admin.py             # Configuração do admin
│   ├── forms.py             # Formulários para carros
│   ├── signal.py            # Sinais para atualizar inventário
│   ├── apps.py              # Configuração do app
│   ├── tests.py             # Testes
│   ├── urls.py              # Rotas da aplicação
│   ├── migrations/          # Migrações do banco de dados
│   └── templates/
│       ├── cars.html        # Lista de carros
│       ├── car_detail.html  # Detalhes do carro
│       ├── new_car.html     # Formulário para novo carro
│       ├── car_update.html  # Formulário para editar carro
│       └── car_delete.html  # Confirmação de exclusão
├── media/                   # Arquivos de mídia (fotos dos carros)
│   └── cars/                # Diretório para fotos dos carros
├── manage.py                # Utilitário de gerenciamento Django
├── db.sqlite3               # Banco de dados SQLite
├── requirements.txt         # Dependências Python
├── venv_cars/               # Ambiente virtual Python
└── README.md                # Este arquivo
```

## 🔧 Configurações Importantes

### settings.py

As principais configurações do projeto estão em `app/settings.py`:

- **INSTALLED_APPS**: Aplicações instaladas
- **DATABASES**: Configurações do banco de dados
- **ALLOWED_HOSTS**: Hosts permitidos
- **SECRET_KEY**: Chave secreta da aplicação

## 📚 Modelos

A aplicação utiliza os seguintes modelos Django em `cars/models.py`:

- **Brand**: Representa as marcas dos carros (ex: Toyota, Ford).
  - Campos: id, name

- **Car**: Modelo principal para os veículos.
  - Campos: id, model, brand (FK), factory_year, model_year, plate, value, photo, bio

- **CarInventory**: Mantém o inventário automático dos carros.
  - Campos: cars_count, cars_value, created_at
  - Atualizado automaticamente via sinais (signals) quando carros são criados/editados/excluídos.

## 🧪 Testes

Execute os testes da aplicação com:

```bash
python manage.py test
```

## 🔐 Segurança

- Mantenha a `SECRET_KEY` segura e não a compartilhe
- Use `DEBUG = False` em produção
- Configure `ALLOWED_HOSTS` adequadamente
- Use variáveis de ambiente para dados sensíveis

## 📝 Desenvolvimento

### Criar migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### Criar um novo app

```bash
python manage.py startapp nome_do_app
```

## 🚢 Deploy

Para fazer deploy em produção:

1. Configure as variáveis de ambiente
2. Configure um servidor web (Nginx, Apache)
3. Use um servidor WSGI (Gunicorn, uWSGI)
4. Configure um banco de dados robusto (PostgreSQL)
5. Ative o HTTPS

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push -u origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

## 📞 Contato

Para dúvidas ou sugestões, abra uma issue no repositório.

---

**Desenvolvido com ❤️ usando Django**

*Última atualização: 17 de março de 2026*
