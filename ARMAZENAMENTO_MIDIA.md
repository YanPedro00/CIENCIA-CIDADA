# ⚠️ ARMAZENAMENTO DE MÍDIA NO RAILWAY

**Data:** 27 de Novembro de 2025  
**Status:** PROBLEMA CONHECIDO

---

## 🔴 PROBLEMA

O Railway usa **armazenamento de arquivos efêmero**, o que significa que:

- ✅ Uploads funcionam normalmente
- ❌ Arquivos são **perdidos a cada deploy**
- ⚠️ Não é adequado para armazenamento permanente de mídia

### O que acontece:

1. Usuário faz upload de arquivo (relatório, foto, etc.)
2. Arquivo é salvo em `/app/media/`
3. Deploy acontece (atualização, restart, etc.)
4. **Todos os arquivos em `/media/` são perdidos**
5. Links quebram (erro 404)

---

## ✅ SOLUÇÕES

### SOLUÇÃO 1: CLOUDINARY (GRÁTIS - RECOMENDADO) 🌟

**Melhor opção para o projeto educacional:**

1. **Criar conta gratuita:**
   - Acesse: https://cloudinary.com/users/register/free
   - Plano gratuito: 25 GB de armazenamento + 25 GB de banda/mês

2. **Instalar biblioteca:**
```bash
pip install django-cloudinary-storage
```

3. **Atualizar `requirements.txt`:**
```txt
django-cloudinary-storage==0.3.0
```

4. **Configurar em `settings.py`:**
```python
INSTALLED_APPS = [
    # ...
    'cloudinary_storage',
    'cloudinary',
    # ...
]

# Cloudinary
import cloudinary

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET')
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

5. **Adicionar variáveis de ambiente no Railway:**
```
CLOUDINARY_CLOUD_NAME=seu_cloud_name
CLOUDINARY_API_KEY=sua_api_key
CLOUDINARY_API_SECRET=seu_api_secret
```

**Vantagens:**
- ✅ Gratuito (25 GB)
- ✅ Fácil configuração
- ✅ Otimização automática de imagens
- ✅ CDN global (rápido)

---

### SOLUÇÃO 2: AWS S3 (PROFISSIONAL)

**Para projetos em escala ou empresariais:**

1. **Instalar biblioteca:**
```bash
pip install django-storages boto3
```

2. **Atualizar `requirements.txt`:**
```txt
django-storages==1.14.2
boto3==1.34.14
```

3. **Criar bucket no S3:**
   - Acesse AWS Console
   - S3 → Create Bucket
   - Configure permissões públicas

4. **Configurar em `settings.py`:**
```python
INSTALLED_APPS = [
    # ...
    'storages',
    # ...
]

# AWS S3
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# Storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

**Vantagens:**
- ✅ Altamente escalável
- ✅ Durabilidade 99.999999999%
- ✅ Integração com AWS

**Desvantagens:**
- ❌ Pago (mas muito barato)
- ❌ Mais complexo

---

### SOLUÇÃO 3: GOOGLE DRIVE/DROPBOX (WORKAROUND)

**Solução temporária sem código:**

1. Usuários fazem upload no Google Drive/Dropbox
2. Copiam link de compartilhamento
3. Colam link no campo de descrição ou comentário
4. Outros acessam via link externo

**Vantagens:**
- ✅ Sem custo
- ✅ Sem código adicional
- ✅ Usuários já conhecem

**Desvantagens:**
- ❌ Não integrado
- ❌ Experiência do usuário pior
- ❌ Links podem quebrar

---

### SOLUÇÃO 4: MANTER COMO ESTÁ (TEMPORÁRIO)

**Status atual:**

- ✅ Uploads funcionam
- ❌ Arquivos perdidos a cada deploy
- ⚠️ Aviso adicionado no formulário

**Quando usar:**
- Apenas para testes/demonstração
- Projeto de curto prazo
- Poucos uploads

---

## 📊 COMPARAÇÃO DE SOLUÇÕES

| Solução | Custo | Facilidade | Permanência | Recomendação |
|---------|-------|------------|-------------|--------------|
| **Cloudinary** | 🟢 Grátis (25GB) | 🟢 Fácil | 🟢 Permanente | ⭐⭐⭐⭐⭐ |
| **AWS S3** | 🟡 ~$0.023/GB | 🟡 Médio | 🟢 Permanente | ⭐⭐⭐⭐ |
| **Google Drive** | 🟢 Grátis | 🟢 Fácil | 🟡 Links externos | ⭐⭐⭐ |
| **Railway Local** | 🟢 Grátis | 🟢 Fácil | 🔴 Efêmero | ⭐⭐ |

---

## 🚀 IMPLEMENTAÇÃO RÁPIDA - CLOUDINARY

### Passo a Passo (15 minutos):

1. **Criar conta:**
   ```
   https://cloudinary.com/users/register/free
   ```

2. **Copiar credenciais:**
   - Dashboard → Account Details
   - Cloud Name, API Key, API Secret

3. **Instalar localmente:**
   ```bash
   pip install django-cloudinary-storage
   pip freeze > requirements.txt
   ```

4. **Atualizar `settings.py`:**
   ```python
   # Adicionar aos INSTALLED_APPS (ANTES de 'django.contrib.staticfiles')
   'cloudinary_storage',
   'cloudinary',
   
   # No final do arquivo
   import cloudinary
   CLOUDINARY_STORAGE = {
       'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME', default=''),
       'API_KEY': config('CLOUDINARY_API_KEY', default=''),
       'API_SECRET': config('CLOUDINARY_API_SECRET', default='')
   }
   
   # Usar Cloudinary para mídia
   if config('CLOUDINARY_CLOUD_NAME', default=''):
       DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
   ```

5. **Adicionar ao `.env` local:**
   ```
   CLOUDINARY_CLOUD_NAME=seu_cloud_name
   CLOUDINARY_API_KEY=sua_api_key
   CLOUDINARY_API_SECRET=seu_api_secret
   ```

6. **Adicionar variáveis no Railway:**
   - Railway Dashboard → Variables
   - Adicionar as 3 variáveis

7. **Commit e deploy:**
   ```bash
   git add -A
   git commit -m "Integrar Cloudinary para armazenamento permanente de mídia"
   git push origin main
   ```

8. **Testar:**
   - Faça upload de um arquivo
   - Redeploy
   - Verifique se o arquivo ainda está acessível

---

## ⚠️ IMPORTANTE

**Arquivos atuais já enviados:**
- ❌ Serão perdidos no próximo deploy
- ✅ Após configurar Cloudinary, novos uploads serão permanentes
- ⚠️ Não é possível recuperar arquivos perdidos

**Recomendação:**
1. Implementar Cloudinary **AGORA**
2. Avisar usuários para reenviar arquivos importantes
3. Documentar no sistema

---

## 📝 NOTAS

### Por que Railway não persiste arquivos?

Railway usa **containers Docker efêmeros**:
- Cada deploy cria um novo container
- Containers antigos são destruídos
- Sistema de arquivos local é resetado

### Alternativas ao Railway para mídia:

1. **Heroku** - Mesmo problema (efêmero)
2. **DigitalOcean App Platform** - Mesmo problema
3. **VPS tradicional** (DigitalOcean Droplet, Linode) - Persiste arquivos
4. **Vercel/Netlify** - Sem suporte para Django backend

**Conclusão:** Para qualquer plataforma serverless/PaaS, use armazenamento externo (S3/Cloudinary).

---

## 🎯 DECISÃO RECOMENDADA

**Para o Projeto de Ciência Cidadã:**

✅ **Implementar CLOUDINARY imediatamente**

**Motivos:**
1. Gratuito (suficiente para o projeto educacional)
2. Fácil de configurar (15 minutos)
3. Resolve o problema permanentemente
4. Melhora performance (CDN)
5. Profissional

**Tempo de implementação:** 15-20 minutos  
**Custo:** $0  
**Dificuldade:** Baixa

---

**Precisa de ajuda para implementar?** Posso fazer todo o processo agora mesmo! 🚀

