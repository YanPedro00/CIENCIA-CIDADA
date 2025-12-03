# 📄 Cloudinary: Suporte para Documentos (PDF, CSV, DOCX)

## 🔧 PROBLEMA IDENTIFICADO

O Cloudinary estava configurado apenas para **imagens** (`MediaCloudinaryStorage`), o que causava problemas ao fazer upload de:
- PDFs
- CSVs  
- DOCX
- PPTX
- Outros arquivos não-imagem

**Sintoma:** URLs geradas tentavam tratar documentos como imagens, resultando em erros 404 ou arquivos corrompidos.

Exemplo de URL problemática:
```
https://res.cloudinary.com/dyh2rsljf/image/upload/v1/media/relatorios/Prova3-2018_1_fbvunb
```
Note o `/image/upload/` - deveria ser `/raw/upload/` para documentos.

---

## ✅ SOLUÇÃO IMPLEMENTADA

### 1. Criado Storage Customizado

**Arquivo:** `core/storage.py`

```python
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class DocumentStorage(RawMediaCloudinaryStorage):
    """
    Storage para documentos não-imagem (PDF, CSV, DOCX, etc)
    Usa resource_type='raw' do Cloudinary
    """
    pass
```

### 2. Atualizado Models

**Campos que agora usam `DocumentStorage()`:**

#### Modelo `Projeto`:
- `relatorio_final` - PDFs, DOCX
- `apresentacao` - PPT, PDF
- `anexo_extra1` - Qualquer arquivo
- `anexo_extra2` - Qualquer arquivo
- `anexo_extra3` - Qualquer arquivo

#### Modelo `Atividade`:
- `arquivo` - Materiais de apoio, tarefas

**Campos que continuam usando storage padrão (imagens):**
- `foto_equipe` - Fotos (ImageField)

### 3. Migração Criada

**Arquivo:** `core/migrations/0004_cloudinary_document_storage.py`

Altera todos os campos `FileField` para usar `DocumentStorage()`.

---

## 🚀 COMO FUNCIONA AGORA

### Imagens (ImageField)
```python
foto_equipe = models.ImageField(...)
```
- Usa: `MediaCloudinaryStorage` (padrão)
- URL: `https://res.cloudinary.com/.../image/upload/.../foto.jpg`
- Suporta: JPG, PNG, GIF, WEBP

### Documentos (FileField com DocumentStorage)
```python
relatorio_final = models.FileField(storage=DocumentStorage(), ...)
```
- Usa: `RawMediaCloudinaryStorage`
- URL: `https://res.cloudinary.com/.../raw/upload/.../relatorio.pdf`
- Suporta: PDF, CSV, DOCX, PPTX, TXT, ZIP, etc.

---

## 📋 DEPLOY NO RAILWAY

### Passo 1: Commit e Push
```bash
git add -A
git commit -m "Fix: Adicionar suporte Cloudinary para documentos PDF/CSV/DOCX"
git push origin main
```

### Passo 2: Railway Aplicará Automaticamente
O `start.sh` já está configurado para rodar migrações:
```bash
python manage.py migrate --noinput
```

### Passo 3: Testar Upload
1. Acesse um projeto
2. Clique em "Anexar Documentos"
3. Faça upload de um PDF ou CSV
4. Verifique se a URL gerada contém `/raw/upload/`

---

## 🧪 TESTE LOCAL (Opcional)

Se quiser testar localmente antes do deploy:

```bash
# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Aplicar migração
python manage.py migrate

# Rodar servidor
python manage.py runserver
```

---

## 📊 VARIÁVEIS DE AMBIENTE

As mesmas variáveis do Cloudinary continuam válidas:

```bash
CLOUDINARY_CLOUD_NAME=dyh2rsljf
CLOUDINARY_API_KEY=837349511372969
CLOUDINARY_API_SECRET=xH95tItuVO-tdzDG4SSwjwbc-NM
```

Já configuradas no Railway ✅

---

## ⚠️ OBSERVAÇÕES

1. **Arquivos já enviados:** Arquivos enviados antes desta correção podem não funcionar. Será necessário fazer novo upload.

2. **Tamanho máximo:** Cloudinary free tier tem limite de 10MB por arquivo.

3. **Formatos suportados:** Praticamente qualquer formato de arquivo é suportado no modo `raw`.

4. **Performance:** Downloads de documentos são rápidos e confiáveis via CDN do Cloudinary.

---

## 🔍 VERIFICAÇÃO

Após o deploy, verifique se as URLs geradas seguem o padrão correto:

✅ **Correto (Documentos):**
```
https://res.cloudinary.com/dyh2rsljf/raw/upload/v1/media/relatorios/arquivo.pdf
```

✅ **Correto (Imagens):**
```
https://res.cloudinary.com/dyh2rsljf/image/upload/v1/media/fotos_equipe/foto.jpg
```

❌ **Incorreto (Documento tratado como imagem):**
```
https://res.cloudinary.com/dyh2rsljf/image/upload/v1/media/relatorios/arquivo.pdf
```

---

## 📚 REFERÊNCIAS

- [Cloudinary Django SDK](https://cloudinary.com/documentation/django_integration)
- [RawMediaCloudinaryStorage](https://github.com/klis87/django-cloudinary-storage)

