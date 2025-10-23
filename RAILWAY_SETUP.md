# 🚂 Deploy no Railway - Configuração Simplificada

## 📋 Arquivos de Configuração

Este projeto está configurado para deploy automático no Railway com os seguintes arquivos:

### 1. **Procfile** ✅
Comando que o Railway executa para iniciar o servidor:
```
web: python manage.py migrate && python manage.py init_data && gunicorn config.wsgi --log-file -
```

- `migrate`: Roda migrações do banco de dados
- `init_data`: Cria usuários de teste automaticamente
- `gunicorn`: Servidor WSGI para produção

### 2. **runtime.txt** ✅
Especifica a versão do Python:
```
python-3.10.12
```

### 3. **build.sh** ✅
Script executado durante o build:
```bash
#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
```

### 4. **requirements.txt** ✅
Todas as dependências Python necessárias:
- Django 4.2.7
- gunicorn (servidor de produção)
- whitenoise (arquivos estáticos)
- psycopg2-binary (PostgreSQL)
- dj-database-url (parse de DATABASE_URL)

### 5. **config/settings.py** ✅
Configurado para detectar automaticamente Railway:
- Usa `DATABASE_URL` do Railway
- Detecta ambiente Railway via `RAILWAY_GIT_COMMIT_SHA`
- WhiteNoise para servir arquivos estáticos
- ALLOWED_HOSTS dinâmico

---

## 🚀 Como Fazer Deploy

### Passo 1: Criar Projeto no Railway
1. Acesse https://railway.app
2. Login com GitHub
3. New Project → Deploy from GitHub repo
4. Selecione: **CIENCIA-CIDADA**

### Passo 2: Adicionar PostgreSQL
1. No projeto, clique em **+ New**
2. Selecione **Database → PostgreSQL**
3. Railway conecta automaticamente via `DATABASE_URL`

### Passo 3: Configurar Variáveis (Opcional)
Clique no serviço Django → Variables:

```bash
DEBUG=False
SECRET_KEY=sua-chave-secreta-aqui
```

**OBS:** `DATABASE_URL` é criado automaticamente pelo Railway!

### Passo 4: Deploy Automático
Railway detecta automaticamente:
- ✅ Python pelo `runtime.txt`
- ✅ Django pelo `requirements.txt`
- ✅ Comando de start pelo `Procfile`
- ✅ Build pelo `build.sh`

### Passo 5: Pegar URL
1. Settings → Domains → Generate Domain
2. URL: `https://seu-projeto.up.railway.app`

---

## 👥 Usuários Criados Automaticamente

Após o primeiro deploy, estes usuários estarão disponíveis:

| Tipo | Username | Senha | Nome |
|------|----------|-------|------|
| Admin | `admin` | `admin123456` | Admin Sistema |
| Professor | `prof.silva` | `prof123` | Maria Silva |
| Estudante | `joao.santos` | `aluno123` | João Santos |
| Estudante | `ana.costa` | `aluno123` | Ana Costa |
| Estudante | `pedro.oliveira` | `aluno123` | Pedro Oliveira |
| Estudante | `maria.souza` | `aluno123` | Maria Souza |

---

## 🔄 Atualizações Futuras

Para atualizar o site:

```bash
git add .
git commit -m "Descrição da mudança"
git push
```

Railway faz redeploy automático! 🚀

---

## 🐛 Troubleshooting

### Erro: "Application failed to respond"
- Verifique se o PostgreSQL está conectado
- Verifique os logs: Deployments → Logs

### Erro: "ModuleNotFoundError"
- Verifique se o módulo está no `requirements.txt`
- Force rebuild: Settings → Redeploy

### Erro: "Static files not found"
- Execute: `python manage.py collectstatic`
- Verifique `STATIC_ROOT` no settings.py

---

## 📊 Monitoramento

No Railway você vê:
- 📈 **Metrics**: CPU, RAM, Requests
- 📋 **Logs**: Logs em tempo real
- 💰 **Usage**: Uso de recursos e créditos

---

## 💰 Custos

- **$5/mês grátis** para todos
- **$20/mês** após limite grátis
- Monitoramento em **Usage** tab

---

## ✅ Checklist de Deploy

- [x] `Procfile` criado
- [x] `runtime.txt` criado  
- [x] `build.sh` criado
- [x] `requirements.txt` atualizado
- [x] `settings.py` configurado para Railway
- [x] Script `init_data` para criar usuários
- [ ] Projeto criado no Railway
- [ ] PostgreSQL adicionado
- [ ] Deploy realizado com sucesso
- [ ] URL gerada e testada
- [ ] Login com usuários de teste funcionando

---

## 📝 Próximos Passos

1. **Domínio Personalizado** (opcional)
   - GitHub Education → Namecheap → Domínio .me grátis
   - Railway Settings → Domains → Add Custom Domain

2. **Backup do Banco** (importante!)
   - Railway → PostgreSQL → Backups
   - Download periódico dos dados

3. **Monitoramento** (recomendado)
   - Railway Logs
   - Sentry para erros (opcional)

---

**Última atualização:** $(date)

