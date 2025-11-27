# 🚀 CONFIGURAR CLOUDINARY NO RAILWAY - PASSO A PASSO

**⏱️ Tempo:** 2 minutos  
**Status:** ✅ Código já está no GitHub

---

## 📋 CHECKLIST RÁPIDO

- [x] Código do Cloudinary implementado
- [x] Commit e push para GitHub
- [ ] **VOCÊ PRECISA FAZER:** Adicionar variáveis no Railway
- [ ] Aguardar redeploy (2-3 minutos)
- [ ] Testar upload

---

## 🎯 PASSO 1: ACESSAR RAILWAY DASHBOARD

1. Abra: https://railway.app/
2. Faça login
3. Selecione o projeto **ciencia-cidada**
4. Clique no **serviço Django** (não no PostgreSQL)

---

## 🔧 PASSO 2: ADICIONAR VARIÁVEIS DE AMBIENTE

1. No serviço Django, clique na aba **"Variables"**
2. Clique em **"+ New Variable"** ou **"RAW Editor"**

### Opção A: Adicionar uma por uma

Clique em **"+ New Variable"** e adicione cada uma:

**Variável 1:**
```
Name: CLOUDINARY_CLOUD_NAME
Value: dyh2rsljf
```

**Variável 2:**
```
Name: CLOUDINARY_API_KEY
Value: 837349511372969
```

**Variável 3:**
```
Name: CLOUDINARY_API_SECRET
Value: xH95tItuVO-tdzDG4SSwjwbc-NM
```

### Opção B: RAW Editor (Mais Rápido) ⭐

Clique em **"RAW Editor"** e cole tudo de uma vez:

```
CLOUDINARY_CLOUD_NAME=dyh2rsljf
CLOUDINARY_API_KEY=837349511372969
CLOUDINARY_API_SECRET=xH95tItuVO-tdzDG4SSwjwbc-NM
```

3. Clique em **"Add"** ou **"Update Variables"**

---

## ⏳ PASSO 3: AGUARDAR REDEPLOY

Após salvar as variáveis:

1. Railway vai **automaticamente fazer redeploy** (2-3 minutos)
2. Veja a aba **"Deployments"** para acompanhar
3. Aguarde até aparecer **"SUCCESS"** ✅

---

## 🧪 PASSO 4: VERIFICAR SE FUNCIONOU

### 1. Verificar Logs

Na aba **"Deployments"** → Clique no último deployment → **"View Logs"**

Procure por:
```
✅ Cloudinary configurado para armazenamento de mídia
```

**Se aparecer:**
```
⚠️  Cloudinary não configurado - usando armazenamento local (efêmero no Railway)
```

→ Significa que as variáveis não foram adicionadas corretamente. Verifique se os nomes estão **exatamente** como mostrado acima.

### 2. Testar Upload

1. Acesse: http://ciencia-cidada.up.railway.app/
2. Faça login como aluno
3. Entre em um projeto
4. Clique em **"Anexar Documentos"**
5. Faça upload de um arquivo qualquer
6. Clique em **"Salvar Anexos"**
7. Volte para a página do projeto
8. Veja se o arquivo aparece na **sidebar de anexos**
9. Clique no link do arquivo → deve abrir/baixar

### 3. Verificar no Cloudinary Dashboard

1. Acesse: https://console.cloudinary.com/
2. Faça login com sua conta
3. Vá em **"Media Library"**
4. Você deve ver os arquivos uploadados lá!

---

## 🎉 PRONTO!

Se tudo funcionou, agora:

✅ Arquivos são **permanentes** (nunca mais serão perdidos)  
✅ CDN global (downloads rápidos de qualquer lugar)  
✅ 25 GB grátis  
✅ Pode fazer quantos deploys quiser  
✅ Arquivos antigos continuam funcionando  

---

## 🐛 TROUBLESHOOTING

### Problema: Erro 404 ao clicar no arquivo

**Causa:** Variáveis não foram configuradas ou deploy não terminou.

**Solução:**
1. Verifique na aba "Variables" do Railway se as 3 variáveis estão lá
2. Aguarde o deploy terminar completamente
3. Verifique os logs para a mensagem "✅ Cloudinary configurado"
4. Tente fazer um novo upload (arquivos antigos ainda estarão no Railway local)

### Problema: "⚠️ Cloudinary não configurado" nos logs

**Causa:** Variáveis não foram adicionadas ou têm nomes errados.

**Solução:**
1. Verifique os **nomes exatos** das variáveis:
   - `CLOUDINARY_CLOUD_NAME` (não `CLOUD_NAME`)
   - `CLOUDINARY_API_KEY` (não `API_KEY`)
   - `CLOUDINARY_API_SECRET` (não `API_SECRET`)
2. Certifique-se de que não há espaços nos valores
3. Salve novamente e aguarde redeploy

### Problema: Arquivos antigos ainda dão 404

**Causa:** Arquivos antigos estavam no armazenamento local do Railway (perdidos).

**Solução:**
- Arquivos antigos não podem ser recuperados
- Apenas **novos uploads** (após configurar Cloudinary) serão permanentes
- Peça aos usuários para refazerem uploads se necessário

---

## 📊 COMO FUNCIONA AGORA

### Antes:
```
Usuário → Upload → Railway Local Storage → ❌ Perdido no próximo deploy
```

### Depois:
```
Usuário → Upload → Cloudinary CDN → ✅ Permanente + Rápido + Backup
```

---

## 💰 CUSTOS

**Cloudinary Plano Gratuito:**
- 25 GB de armazenamento
- 25 GB de banda/mês
- Transformações de imagem ilimitadas
- CDN global incluído

**Para o projeto educacional:** Mais que suficiente! 🎓

Se um dia precisar de mais:
- Plano Plus: $99/mês (75 GB)
- Mas dificilmente será necessário

---

## 🎓 RESUMO PARA A PROFESSORA

"Agora a plataforma usa **Cloudinary** para armazenar arquivos (relatórios, apresentações, fotos). 

**Benefícios:**
- ✅ Arquivos **nunca são perdidos** (antes eram perdidos a cada atualização)
- ✅ Downloads **mais rápidos** (CDN global)
- ✅ **25 GB grátis** (suficiente para o curso inteiro)
- ✅ Profissional e escalável"

---

**Configurado em:** 27 de Novembro de 2025  
**Por:** Yan Pedro  
**Commit:** fc0ffb1

