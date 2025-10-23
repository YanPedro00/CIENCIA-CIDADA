# 🌐 Como Configurar Domínio .ME Grátis (GitHub Education)

## 📋 Pré-requisitos

- ✅ GitHub Education Pack ativado
- ✅ Site funcionando no Railway
- ⏳ Escolher um nome de domínio disponível

---

## 🎓 PASSO 1: Ativar GitHub Education Pack (se ainda não tem)

### 1.1 Verificar se já está ativo:
1. Acesse: https://education.github.com/pack
2. Se aparecer **"You have access to the pack"** → Já está ativo! ✅
3. Se não, continue para 1.2

### 1.2 Solicitar acesso:
1. Clique em **"Get your Student Pack"** ou **"Benefits for Teachers"**
2. Preencha o formulário:
   - Email institucional (.edu ou da universidade)
   - Comprovante de matrícula/vínculo (foto/PDF)
   - Nome da instituição
3. Aguarde aprovação (1-3 dias úteis)

---

## 🛒 PASSO 2: Conseguir Domínio .ME Grátis no Namecheap

### 2.1 Acessar oferta do GitHub Education:
1. Vá em: https://education.github.com/pack/offers
2. Busque por **"Namecheap"**
3. Clique em **"Get access to Namecheap"**
4. Copie o **código promocional** (algo como: `GITHUB-STUDENT-DOMAIN`)

### 2.2 Criar conta no Namecheap (se não tem):
1. Acesse: https://www.namecheap.com/
2. Clique em **"Sign Up"** (canto superior direito)
3. Preencha seus dados:
   - Email
   - Username
   - Senha
4. Confirme o email

### 2.3 Ativar benefício GitHub Education no Namecheap:
1. Faça login no Namecheap
2. Vá em **Account → GitHub Student Developer Pack**
3. Cole o código promocional que copiou
4. Clique em **"Apply"**

### 2.4 Buscar e registrar seu domínio .me:
1. No site do Namecheap, use a barra de busca
2. Digite o nome que você quer (sem o .me):
   - Exemplos:
     - `cienciacidada` → cienciacidada.me
     - `cientistascidadaos` → cientistascidadaos.me
     - `projetociencia` → projetociencia.me
     - `labciencia` → labciencia.me

3. Se estiver disponível (bolinha verde ✅), clique em **"Add to Cart"**
4. Vá para o carrinho (**Cart**)
5. Na seção de pagamento:
   - Aplique o cupom do GitHub Education
   - O preço deve ficar **$0.00** (1 ano grátis!)
6. Finalize o pedido (**Confirm Order**)

**🎉 Parabéns! Você tem um domínio .me!**

---

## 🔧 PASSO 3: Configurar DNS no Namecheap

Agora você precisa apontar seu domínio para o Railway.

### 3.1 Acessar configurações do domínio:
1. No Namecheap, vá em **Domain List**
2. Clique no botão **"Manage"** ao lado do seu domínio

### 3.2 Configurar DNS:
1. Vá na aba **"Advanced DNS"**
2. Você verá uma seção **"Host Records"**
3. **Delete** todos os registros existentes (se tiver)
4. Clique em **"Add New Record"**

### 3.3 Adicionar registros DNS:

**Registro 1 - CNAME para www:**
- Type: `CNAME Record`
- Host: `www`
- Value: `web-production-e06df.up.railway.app` (sua URL do Railway SEM https://)
- TTL: `Automatic` ou `300`

**Registro 2 - CNAME para raiz:**
- Type: `CNAME Record`
- Host: `@`
- Value: `web-production-e06df.up.railway.app`
- TTL: `Automatic` ou `300`

**OBS:** Alguns provedores DNS não permitem CNAME no `@`. Nesse caso, use um **ALIAS Record** ou **ANAME Record** se disponível.

5. Clique em **"Save Changes"** (ícone de check verde)

### 3.4 Aguardar propagação DNS:
- Leva de **5 minutos a 48 horas**
- Geralmente funciona em **10-30 minutos**

---

## 🚂 PASSO 4: Adicionar Domínio no Railway

### 4.1 Acessar configurações do serviço:
1. Vá para seu projeto no Railway
2. Clique no serviço **Django** (web)
3. Vá na aba **"Settings"**

### 4.2 Adicionar domínio personalizado:
1. Role até a seção **"Networking"** ou **"Domains"**
2. Clique em **"+ Custom Domain"**
3. Digite seu domínio: `seudominio.me`
4. Clique em **"Add"**

### 4.3 Railway vai gerar certificado SSL:
- Railway automaticamente cria um certificado SSL grátis (Let's Encrypt)
- Aguarde alguns segundos até aparecer **"Active"** com check verde ✅

### 4.4 (Opcional) Adicionar www também:
1. Clique novamente em **"+ Custom Domain"**
2. Digite: `www.seudominio.me`
3. Clique em **"Add"**

---

## 🔐 PASSO 5: Atualizar Django Settings

Depois de adicionar o domínio no Railway, atualize o Django:

### 5.1 Editar `config/settings.py`:

Adicione seu domínio ao `CSRF_TRUSTED_ORIGINS`:

```python
# CSRF Trusted Origins (para Railway e domínios personalizados)
CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
    'https://*.up.railway.app',
    'https://seudominio.me',        # Adicione seu domínio
    'https://www.seudominio.me',     # Adicione com www também
]
```

### 5.2 Fazer commit e push:
```bash
git add config/settings.py
git commit -m "Adicionar domínio personalizado ao CSRF_TRUSTED_ORIGINS"
git push
```

Railway fará redeploy automático.

---

## ✅ PASSO 6: Testar seu Domínio!

Depois da propagação DNS (10-30 min):

1. **Acesse:** `https://seudominio.me`
2. **Deve carregar seu site!** 🎉
3. **Teste também:** `https://www.seudominio.me`
4. **Teste login:** Deve funcionar sem erros CSRF!

---

## 🔍 Verificar Status de Propagação DNS

### Ferramenta online:
- https://dnschecker.org/
- Digite seu domínio: `seudominio.me`
- Selecione tipo: `CNAME`
- Clique em **"Search"**
- Veja se o CNAME está apontando para `.railway.app` em diferentes locais

### Linha de comando:
```bash
# macOS/Linux
dig seudominio.me

# Windows
nslookup seudominio.me
```

---

## 🐛 Troubleshooting

### Problema 1: "This site can't be reached" após 48h
- Verifique se os registros DNS estão corretos no Namecheap
- Certifique-se de que usou a URL Railway correta (SEM https://)
- Tente limpar cache do DNS: `ipconfig /flushdns` (Windows) ou `sudo dscacheutil -flushcache` (macOS)

### Problema 2: "Certificate error" ou "Not secure"
- Aguarde alguns minutos. Railway está gerando o certificado SSL.
- Se persistir após 10 minutos, remova e adicione o domínio novamente no Railway.

### Problema 3: Erro CSRF no domínio personalizado
- Certifique-se de adicionar o domínio ao `CSRF_TRUSTED_ORIGINS`
- Faça commit e push
- Aguarde redeploy do Railway

### Problema 4: Domínio não aparece no Railway
- Verifique se o DNS foi configurado corretamente no Namecheap
- Aguarde 10-30 minutos para propagação
- Tente adicionar novamente

---

## 💰 Custos

- **Ano 1:** Grátis com GitHub Education! 🎓
- **Após 1 ano:** ~$20-30/ano para renovar (opcional)
- **SSL:** Grátis e automático no Railway! 🔒

---

## 🎯 Checklist Completo

- [ ] GitHub Education Pack ativado
- [ ] Código promocional Namecheap obtido
- [ ] Domínio .me registrado grátis
- [ ] DNS configurado no Namecheap (CNAME)
- [ ] Aguardado propagação (10-30 min)
- [ ] Domínio adicionado no Railway
- [ ] SSL certificado ativo no Railway
- [ ] `CSRF_TRUSTED_ORIGINS` atualizado
- [ ] Site acessível pelo domínio personalizado
- [ ] Login funcionando no domínio personalizado

---

## 🎉 Resultado Final

Antes:
- ❌ `https://web-production-e06df.up.railway.app` (feio)

Depois:
- ✅ `https://seudominio.me` (profissional!)
- ✅ SSL automático (cadeado verde 🔒)
- ✅ Domínio memorável e fácil de compartilhar

---

## 📚 Links Úteis

- GitHub Education Pack: https://education.github.com/pack
- Namecheap: https://www.namecheap.com/
- Railway Docs - Custom Domains: https://docs.railway.app/guides/public-networking#custom-domains
- DNS Checker: https://dnschecker.org/
- Let's Encrypt (SSL): https://letsencrypt.org/

---

**Última atualização:** Outubro 2025

