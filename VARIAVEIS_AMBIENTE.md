# 🔐 VARIÁVEIS DE AMBIENTE

Este documento lista todas as variáveis de ambiente necessárias para o projeto.

---

## 📝 RAILWAY - CONFIGURAÇÃO

No Railway Dashboard, vá em **Variables** e adicione:

### Django Settings
```
SECRET_KEY=django-insecure-sua-secret-key-aqui
DEBUG=False
ALLOWED_HOSTS=.railway.app,.up.railway.app
```

### Database
```
DATABASE_URL=(gerado automaticamente pelo Railway quando adicionar PostgreSQL)
```

### Cloudinary (Armazenamento de Mídia) ⭐ NOVO
```
CLOUDINARY_CLOUD_NAME=dyh2rsljf
CLOUDINARY_API_KEY=837349511372969
CLOUDINARY_API_SECRET=xH95tItuVO-tdzDG4SSwjwbc-NM
```

---

## 💻 DESENVOLVIMENTO LOCAL

Crie um arquivo `.env` na raiz do projeto:

```env
# Django
SECRET_KEY=django-insecure-development-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (SQLite localmente)
# DATABASE_URL não é necessário (usa SQLite por padrão)

# Cloudinary
CLOUDINARY_CLOUD_NAME=dyh2rsljf
CLOUDINARY_API_KEY=837349511372969
CLOUDINARY_API_SECRET=xH95tItuVO-tdzDG4SSwjwbc-NM
```

---

## ✅ VERIFICAR CONFIGURAÇÃO

### No Railway (depois do deploy):

Veja os logs do deploy para confirmar:
```
✅ Cloudinary configurado para armazenamento de mídia
```

Se aparecer:
```
⚠️  Cloudinary não configurado - usando armazenamento local (efêmero no Railway)
```

Significa que as variáveis não foram configuradas corretamente.

---

## 🔧 TESTAR LOCALMENTE

1. Criar arquivo `.env` com as variáveis acima
2. Instalar dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Rodar servidor:
   ```bash
   python manage.py runserver 8010
   ```
4. Fazer upload de arquivo
5. Verificar no Cloudinary Dashboard: https://console.cloudinary.com/

---

## 📊 CLOUDINARY DASHBOARD

**URL:** https://console.cloudinary.com/  
**Login:** Sua conta Cloudinary

**O que você verá:**
- Media Library: Todos os arquivos uploadados
- Usage: Quanto de armazenamento/banda foi usado (25 GB grátis)
- Settings: Suas credenciais

---

## 🚨 SEGURANÇA

⚠️ **NUNCA** commitar o arquivo `.env` no Git!

O `.gitignore` já está configurado para ignorar:
- `.env`
- `venv/`
- `db.sqlite3`

---

## ✅ CHECKLIST DE CONFIGURAÇÃO

### Railway:
- [ ] Adicionar variável `CLOUDINARY_CLOUD_NAME`
- [ ] Adicionar variável `CLOUDINARY_API_KEY`
- [ ] Adicionar variável `CLOUDINARY_API_SECRET`
- [ ] Fazer deploy
- [ ] Verificar logs para mensagem "✅ Cloudinary configurado"
- [ ] Testar upload de arquivo
- [ ] Verificar arquivo no Cloudinary Dashboard

### Local:
- [ ] Criar arquivo `.env`
- [ ] Adicionar credenciais Cloudinary
- [ ] Instalar dependências: `pip install -r requirements.txt`
- [ ] Rodar servidor: `python manage.py runserver 8010`
- [ ] Testar upload
- [ ] Verificar no Cloudinary Dashboard

---

## 🎯 RESULTADO ESPERADO

### Antes (Railway Local):
- ✅ Upload funciona
- ❌ Arquivos perdidos a cada deploy
- ❌ Erro 404 após redeploy

### Depois (Com Cloudinary):
- ✅ Upload funciona
- ✅ Arquivos **permanentes**
- ✅ CDN global (rápido)
- ✅ Backup automático
- ✅ Sem limite de deploys

---

**Configurado em:** 27 de Novembro de 2025  
**Plano Cloudinary:** Gratuito (25 GB)

