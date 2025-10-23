# 🚀 Guia de Deploy - Plataforma de Ciência Cidadã

## 📋 Opções de Deploy

Este guia apresenta diferentes opções para colocar a plataforma no ar.

---

## 🎯 Opção 1: Deploy Simples (PythonAnywhere) - RECOMENDADO

### Por que PythonAnywhere?
- ✅ **Gratuito** para projetos pequenos
- ✅ **Fácil** de configurar
- ✅ **Django nativo** (suporte completo)
- ✅ **Sem cartão de crédito** necessário
- ✅ **Ideal para projetos educacionais**

### Passo a Passo

1. **Criar conta** em https://www.pythonanywhere.com

2. **Upload do código**
   - Fazer upload via Git ou arquivo ZIP
   - Ou usar console Bash do PythonAnywhere

3. **Configurar ambiente**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 mysite
   pip install -r requirements.txt
   ```

4. **Configurar Web App**
   - Dashboard → Web → Add a new web app
   - Manual configuration → Python 3.10
   - Configurar WSGI file
   - Apontar para seu projeto

5. **Configurar banco de dados**
   - SQLite funciona direto
   - Ou usar MySQL gratuito do PythonAnywhere

6. **Coletar arquivos estáticos**
   ```bash
   python manage.py collectstatic
   ```

7. **Criar superusuário**
   ```bash
   python manage.py createsuperuser
   ```

### Limitações do Plano Gratuito
- 1 web app
- 512MB de espaço
- 100 segundos de CPU/dia
- Acesso via: `seuusuario.pythonanywhere.com`

---

## 🎯 Opção 2: Heroku (Pago)

**Nota**: Heroku não é mais gratuito desde novembro de 2022.

### Custo
- ~$5-7/mês (Eco Dynos)

### Passo a Passo

1. **Instalar Heroku CLI**
   ```bash
   brew install heroku/brew/heroku  # macOS
   ```

2. **Preparar projeto**
   ```bash
   # Criar Procfile
   echo "web: gunicorn config.wsgi" > Procfile
   
   # Criar runtime.txt
   echo "python-3.10.12" > runtime.txt
   ```

3. **Deploy**
   ```bash
   heroku login
   heroku create nome-do-projeto
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

4. **Configurar variáveis**
   ```bash
   heroku config:set SECRET_KEY='sua-secret-key'
   heroku config:set DEBUG=False
   ```

---

## 🎯 Opção 3: Railway (Moderno)

### Por que Railway?
- ✅ Deploy automático via Git
- ✅ $5 de crédito grátis/mês
- ✅ Interface moderna
- ✅ PostgreSQL incluído

### Passo a Passo

1. **Criar conta** em https://railway.app

2. **Novo projeto**
   - New Project → Deploy from GitHub
   - Conectar repositório

3. **Configurar variáveis**
   - Variables → Add variables
   - `SECRET_KEY`, `DEBUG=False`

4. **Railway cuida do resto**
   - Detecta Django automaticamente
   - Instala dependências
   - Roda migrações

---

## 🎯 Opção 4: Render (Alternativa ao Heroku)

### Por que Render?
- ✅ Plano gratuito disponível
- ✅ PostgreSQL gratuito
- ✅ Deploy automático
- ✅ SSL grátis

### Limitações Gratuitas
- App "dorme" após 15 min inativo
- 750h de uptime/mês

### Passo a Passo

1. **Criar conta** em https://render.com

2. **Novo Web Service**
   - New → Web Service
   - Conectar GitHub

3. **Configurar**
   ```
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn config.wsgi:application
   ```

4. **Variáveis de ambiente**
   - Environment → Add variables

---

## 🎯 Opção 5: VPS (Avançado)

### Servidores VPS
- **DigitalOcean**: $4-6/mês
- **Linode**: $5/mês
- **Vultr**: $2.50-5/mês

### Quando usar?
- Controle total necessário
- Múltiplos projetos
- Personalização avançada
- Você tem experiência com Linux

### Stack Recomendada
```
Ubuntu 22.04 LTS
↓
Nginx (web server)
↓
Gunicorn (WSGI server)
↓
Django
↓
PostgreSQL
```

### Passo a Passo Resumido

1. **Configurar servidor**
   ```bash
   # Atualizar sistema
   sudo apt update && sudo apt upgrade
   
   # Instalar dependências
   sudo apt install python3-pip python3-venv nginx postgresql
   ```

2. **Configurar projeto**
   ```bash
   # Clone e setup
   git clone seu-repositorio
   cd projeto
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configurar Nginx**
   ```nginx
   server {
       listen 80;
       server_name seu-dominio.com;
       
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
       }
       
       location /static/ {
           alias /caminho/para/staticfiles/;
       }
       
       location /media/ {
           alias /caminho/para/media/;
       }
   }
   ```

4. **Configurar Gunicorn**
   ```bash
   gunicorn config.wsgi:application --bind 127.0.0.1:8000 --daemon
   ```

5. **Configurar systemd** (manter rodando)
   ```ini
   [Unit]
   Description=Ciencia Cidada
   
   [Service]
   User=usuario
   WorkingDirectory=/caminho/projeto
   ExecStart=/caminho/venv/bin/gunicorn config.wsgi:application
   
   [Install]
   WantedBy=multi-user.target
   ```

---

## 🔧 Configurações de Produção

### settings.py (Produção)

```python
# NUNCA use DEBUG=True em produção!
DEBUG = False

# Defina hosts permitidos
ALLOWED_HOSTS = ['seu-dominio.com', 'www.seu-dominio.com']

# Use PostgreSQL em produção
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Configure arquivos estáticos
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Segurança
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Email (configure seu servidor SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'sua-senha-app'
```

### Criar arquivo .env

```bash
SECRET_KEY=sua-chave-super-secreta-aqui
DEBUG=False
DATABASE_URL=postgres://usuario:senha@host:5432/banco
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
```

---

## 📦 Banco de Dados

### Migração SQLite → PostgreSQL

1. **Backup SQLite**
   ```bash
   python manage.py dumpdata > backup.json
   ```

2. **Configurar PostgreSQL**
   ```bash
   # Instalar
   pip install psycopg2-binary
   
   # Criar banco
   psql -U postgres
   CREATE DATABASE ciencia_cidada;
   CREATE USER usuario WITH PASSWORD 'senha';
   GRANT ALL PRIVILEGES ON DATABASE ciencia_cidada TO usuario;
   ```

3. **Migrar dados**
   ```bash
   # Com novo banco configurado
   python manage.py migrate
   python manage.py loaddata backup.json
   ```

---

## 🔒 Segurança (Checklist)

Antes de colocar no ar:

- [ ] `DEBUG = False`
- [ ] `SECRET_KEY` em variável de ambiente
- [ ] `ALLOWED_HOSTS` configurado
- [ ] HTTPS habilitado (SSL)
- [ ] Senhas fortes
- [ ] Backup automático do banco
- [ ] Monitoring configurado
- [ ] Logs configurados
- [ ] Firewall configurado (se VPS)
- [ ] Atualizações automáticas (se VPS)

---

## 🎛️ Variáveis de Ambiente

Criar arquivo `.env` (NUNCA commitar!):

```bash
# Django
SECRET_KEY=sua-chave-muito-secreta
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,seu-dominio.com

# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=ciencia_cidada
DB_USER=usuario
DB_PASSWORD=senha
DB_HOST=localhost
DB_PORT=5432

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=senha-app

# Storage (se usar S3)
AWS_ACCESS_KEY_ID=sua-key
AWS_SECRET_ACCESS_KEY=sua-secret
AWS_STORAGE_BUCKET_NAME=bucket
```

---

## 📊 Monitoramento

### Ferramentas Recomendadas

1. **Sentry** - Tracking de erros
   - https://sentry.io
   - Gratuito para projetos pequenos

2. **UptimeRobot** - Monitorar uptime
   - https://uptimerobot.com
   - Gratuito

3. **Google Analytics** - Estatísticas
   - Adicionar no template base

---

## 🔄 CI/CD (Opcional)

### GitHub Actions

Criar `.github/workflows/deploy.yml`:

```yaml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.10
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        python manage.py test
    
    - name: Deploy
      run: |
        # Seus comandos de deploy
```

---

## 📝 Comandos Úteis (Produção)

### Coletar arquivos estáticos
```bash
python manage.py collectstatic --no-input
```

### Rodar migrações
```bash
python manage.py migrate
```

### Criar superusuário
```bash
python manage.py createsuperuser
```

### Backup do banco
```bash
python manage.py dumpdata > backup_$(date +%Y%m%d).json
```

### Limpar sessões antigas
```bash
python manage.py clearsessions
```

---

## 🆘 Troubleshooting

### Erro: Static files não carregam
```python
# settings.py
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Executar
python manage.py collectstatic
```

### Erro: Media files não aparecem
```python
# urls.py (apenas desenvolvimento)
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Erro: CSRF failed
```python
# settings.py
CSRF_TRUSTED_ORIGINS = ['https://seu-dominio.com']
```

---

## ✅ Checklist Final de Deploy

- [ ] Código no GitHub/GitLab
- [ ] `.env` configurado (não no Git)
- [ ] `DEBUG=False`
- [ ] `SECRET_KEY` seguro
- [ ] `ALLOWED_HOSTS` configurado
- [ ] Banco de dados PostgreSQL
- [ ] Migrações rodadas
- [ ] Superusuário criado
- [ ] Static files coletados
- [ ] HTTPS configurado
- [ ] Domínio apontando
- [ ] Email configurado (opcional)
- [ ] Backup configurado
- [ ] Monitoramento ativo
- [ ] Testes realizados

---

## 🎯 Recomendação Final

**Para curso de extensão (3 meses):**

👉 **Use PythonAnywhere (gratuito)**
- Mais fácil de configurar
- Sem custos
- Suporte nativo ao Django
- Perfeito para fins educacionais

**Para projeto de longo prazo:**

👉 **Use Railway ou Render**
- Deploy automático
- PostgreSQL incluído
- Escala conforme necessidade
- ~$5/mês

---

## 📞 Suporte

Para dúvidas sobre deploy:
1. Documentação oficial do Django: https://docs.djangoproject.com
2. Documentação da plataforma escolhida
3. Stack Overflow
4. Django Brasil (Telegram)

---

**Boa sorte com o deploy! 🚀**

