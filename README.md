# Plataforma de Ciência Cidadã Educacional

Plataforma web desenvolvida para o curso de extensão, onde grupos de estudantes desenvolvem projetos científicos completos seguindo as 6 fases do método científico.

## 🎯 Objetivo

Proporcionar uma ferramenta educacional onde estudantes trabalhem colaborativamente em projetos de ciência cidadã, aprendendo na prática o processo científico completo: desde a formulação do problema até a conclusão da pesquisa.

## 🚀 Funcionalidades Principais

### Para Professores
- Criar e gerenciar turmas
- Acompanhar progresso dos grupos
- Aprovar transições entre fases dos projetos
- Dar feedback em cada etapa
- Avaliar projetos concluídos

### Para Estudantes
- Entrar em turmas via código de acesso
- Formar grupos colaborativos
- Desenvolver projeto científico em 6 fases:
  1. Problema de Pesquisa
  2. Hipótese
  3. Metodologia
  4. Coleta de Dados
  5. Análise de Dados
  6. Conclusão
- Coletar dados colaborativamente
- Visualizar dados em gráficos

## 🛠️ Tecnologias

- **Backend**: Django 4.2
- **Frontend**: HTML, CSS (Bootstrap 5), JavaScript
- **Banco de Dados**: PostgreSQL
- **Autenticação**: Django Authentication System
- **Deploy**: Gunicorn + WhiteNoise

## 📋 Pré-requisitos

- Python 3.10+
- PostgreSQL 14+
- pip

## ⚙️ Instalação

### 1. Clone o repositório
```bash
git clone [url-do-repositorio]
cd "Site - Ciência Cidadã"
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

### 5. Configure o banco de dados PostgreSQL
```bash
# Entre no PostgreSQL
psql -U postgres

# Crie o banco de dados
CREATE DATABASE ciencia_cidada;
```

### 6. Execute as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crie um superusuário
```bash
python manage.py createsuperuser
```

### 8. Execute o servidor de desenvolvimento
```bash
python manage.py runserver 8010
```

Acesse: http://localhost:8010

## 📁 Estrutura do Projeto

```
ciencia_cidada/
├── manage.py
├── requirements.txt
├── README.md
├── .env
├── config/              # Configurações do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                # App principal
│   ├── models.py        # Modelos (Usuario, Turma, Grupo, Projeto)
│   ├── views.py         # Views
│   ├── forms.py         # Formulários
│   ├── admin.py         # Admin customizado
│   └── templates/       # Templates
├── static/              # Arquivos estáticos
└── media/               # Uploads (fotos de observações)
```

## 👥 Tipos de Usuário

1. **Professor**: Cria turmas, orienta grupos, aprova fases
2. **Estudante**: Participa de grupos, desenvolve projetos

## 📊 Modelo de Dados

- **Usuario**: Professor ou Estudante
- **Turma**: Criada por professor, contém grupos
- **Grupo**: 3-5 estudantes trabalhando juntos
- **Projeto**: Desenvolvido pelo grupo em 6 fases
- **Observacao**: Dados coletados na Fase 4
- **Feedback**: Comentários do professor
- **Avaliacao**: Nota conceitual final

## 🔒 Segurança

- Autenticação obrigatória
- Permissões por tipo de usuário
- Proteção CSRF
- Validação de uploads
- SQL Injection protection (ORM Django)

## 📝 Licença

Projeto desenvolvido para fins educacionais no curso de extensão.

## 👨‍💻 Desenvolvimento

Desenvolvido como parte do curso de extensão em Ciência Cidadã.

