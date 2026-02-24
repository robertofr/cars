# 🚗 Cars - Django Project

Um projeto Django moderno e bem estruturado para gerenciamento de automóveis.

## 📋 Descrição

O **Cars** é uma aplicação web desenvolvida com Django que fornece uma plataforma completa para gerenciar informações sobre veículos, incluindo cadastro, consulta e administração de dados relacionados a automóveis.

## 🎯 Funcionalidades

- ✅ Gerenciamento de veículos
- ✅ Interface administrativa intuitiva
- ✅ API RESTful para integração
- ✅ Banco de dados SQLite integrado
- ✅ Sistema de autenticação do Django

## 🛠️ Tecnologias Utilizadas

- **Framework**: Django 6.0.2
- **Linguagem**: Python 3.12
- **Banco de Dados**: SQLite
- **Gerenciador de Pacotes**: pip
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
│   └── asgi.py              # Configuração ASGI
├── cars/                     # Aplicação principal
│   ├── models.py            # Modelos de dados
│   ├── views.py             # Lógica das visualizações
│   ├── admin.py             # Configuração do admin
│   ├── urls.py              # Rotas da aplicação
│   └── migrations/          # Migrações do banco de dados
├── manage.py                # Utilitário de gerenciamento Django
├── db.sqlite3               # Banco de dados SQLite
└── venv_cars/               # Ambiente virtual Python
```

## 🔧 Configurações Importantes

### settings.py

As principais configurações do projeto estão em `app/settings.py`:

- **INSTALLED_APPS**: Aplicações instaladas
- **DATABASES**: Configurações do banco de dados
- **ALLOWED_HOSTS**: Hosts permitidos
- **SECRET_KEY**: Chave secreta da aplicação

## 📚 Modelos

A aplicação utiliza modelos Django para definir a estrutura de dados. Verifique `cars/models.py` para mais detalhes.

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

*Última atualização: 23 de fevereiro de 2026*
