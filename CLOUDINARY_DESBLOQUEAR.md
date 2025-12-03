# SOLUÇÃO: Desbloquear PDFs no Cloudinary

## PROBLEMA IDENTIFICADO

**"Blocked for delivery"** - Os arquivos estão sendo salvos como **authenticated/private** em vez de **public**.

Por isso os PDFs não abrem!

---

## SOLUÇÃO IMEDIATA: Desbloquear Manualmente no Dashboard

### Passo 1: Acessar Cloudinary
1. Acesse https://cloudinary.com/console
2. Login com suas credenciais

### Passo 2: Ir para Media Library
1. No menu lateral, clique em **Media Library**
2. Você verá todos os arquivos enviados

### Passo 3: Desbloquear TODOS os PDFs

Para **CADA arquivo PDF/DOCX** que você enviou:

1. **Clique no arquivo**
2. No painel direito, procure por **"Access control"**
3. Você verá: **"Blocked for delivery"** ❌
4. Clique em **"Change"** ou **"Edit"**
5. Mude para: **"Public"** ou **"Upload"** ✅
6. Clique em **"Save"**

### Passo 4: Testar
1. Volte ao site
2. Clique no link do PDF
3. Agora deve funcionar! ✅

---

## SOLUÇÃO PERMANENTE: Código Corrigido

Já corrigi o arquivo `core/storage.py` para garantir que **novos uploads** sejam públicos automaticamente.

### O que foi alterado:

**Antes (ERRADO):**
```python
class DocumentStorage(RawMediaCloudinaryStorage):
    pass
```

**Depois (CORRETO):**
```python
class DocumentStorage(RawMediaCloudinaryStorage):
    def _save(self, name, content):
        if not hasattr(self, 'OPTIONS'):
            self.OPTIONS = {}
        
        self.OPTIONS['type'] = 'upload'  # Público
        self.OPTIONS['resource_type'] = 'raw'  # Documentos
        
        return super()._save(name, content)
```

---

## AÇÃO NECESSÁRIA AGORA

### 1. Desbloquear Arquivos Antigos (MANUAL)

**Arquivos que você precisa desbloquear no dashboard:**
- `media/apresentacoes/projeto_beneficios-da-energia-solar_1_kpotcs`
- Todos os outros PDFs/DOCX que você enviou

**Como fazer:**
1. Cloudinary Console → Media Library
2. Clique em cada arquivo PDF
3. Access control → Mude para "Public"
4. Save

### 2. Fazer Deploy da Correção

```bash
git pull origin main
```

O Railway vai automaticamente fazer redeploy com a correção.

### 3. Testar Novo Upload

Após o deploy:
1. Delete um PDF antigo (use o botão de lixeira)
2. Faça novo upload do mesmo arquivo
3. O novo arquivo será público automaticamente
4. Teste o link

---

## VERIFICAÇÃO

### Arquivo Público (CORRETO) ✅
```
Access control: Public
Type: upload
Resource Type: raw
```

### Arquivo Bloqueado (ERRADO) ❌
```
Access control: Blocked for delivery
Type: authenticated
Resource Type: raw
```

---

## POR QUE ISSO ACONTECEU?

O `RawMediaCloudinaryStorage` por padrão usa `type='authenticated'` para segurança.

Mas para PDFs que queremos compartilhar publicamente, precisamos forçar `type='upload'`.

---

## RESUMO RÁPIDO

**AGORA (Emergência):**
1. Acesse Cloudinary Console
2. Media Library → Clique em cada PDF
3. Access control → Mude para "Public"
4. Save

**DEPOIS (Permanente):**
1. Aguarde deploy automático do Railway
2. Delete PDFs antigos
3. Faça novo upload
4. Novos arquivos serão públicos automaticamente

---

## TESTE FINAL

Após desbloquear manualmente, teste este link novamente:
```
https://res.cloudinary.com/dyh2rsljf/raw/upload/v1/media/apresentacoes/projeto_beneficios-da-energia-solar_1_kpotcs.pdf
```

Deve abrir perfeitamente! ✅

---

**IMPORTANTE:** Arquivos antigos precisam ser desbloqueados manualmente OU você pode deletá-los e fazer novo upload após o deploy.

