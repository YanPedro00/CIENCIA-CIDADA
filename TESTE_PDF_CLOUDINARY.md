# TESTE: Upload de PDF no Cloudinary

## PROBLEMA IDENTIFICADO

PDFs enviados **ANTES** da correção do DocumentStorage não funcionam porque foram salvos com `resource_type='image'` em vez de `resource_type='raw'`.

## SOLUÇÃO

Fazer **NOVO UPLOAD** após o deploy da correção.

---

## PASSO A PASSO PARA TESTAR

### 1. Verificar Deploy no Railway

1. Acesse https://railway.app
2. Vá no seu projeto
3. Clique em **Deployments**
4. Verifique se o último commit é `Fix: Adicionar suporte Cloudinary...`
5. Status deve ser: **SUCCESS**

### 2. Verificar Logs de Migração

1. Ainda em Deployments
2. Clique no deploy mais recente
3. Abra **View Logs**
4. Procure por:
   ```
   🔄 Running migrations...
   Running migrations:
     Applying core.0004_cloudinary_document_storage... OK
   ```
5. Se encontrou "OK", a migração foi aplicada ✅

### 3. Fazer Novo Upload de PDF

#### Opção A: Criar Novo Projeto
1. Acesse https://ciencia-cidada.up.railway.app
2. Login como **estudante** (senha: `senha123`)
3. Crie um novo grupo de teste
4. Crie um projeto de teste
5. Vá em "Anexar Documentos"
6. Faça upload de um PDF qualquer
7. Clique no link gerado

#### Opção B: Atualizar Projeto Existente
1. Acesse um projeto que já tem
2. Vá em "Anexar Documentos"
3. **RE-ENVIE** o PDF (substitua o antigo)
4. Clique no link gerado

### 4. Verificar URL Gerada

**COPIE** a URL do PDF que aparece no navegador.

**Se a URL contém `/raw/upload/`:**
```
https://res.cloudinary.com/dyh2rsljf/raw/upload/v1/media/relatorios/arquivo.pdf
```
✅ **CORRETO!** O PDF deve abrir normalmente.

**Se a URL contém `/image/upload/`:**
```
https://res.cloudinary.com/dyh2rsljf/image/upload/v1/media/relatorios/arquivo.pdf
```
❌ **INCORRETO!** Este é um arquivo antigo. Faça novo upload.

---

## CHECKLIST DE VERIFICAÇÃO

- [ ] Deploy no Railway está com status SUCCESS
- [ ] Último commit é o da correção do Cloudinary
- [ ] Logs mostram migração 0004 aplicada
- [ ] Fiz novo upload de um PDF (não usei arquivo antigo)
- [ ] URL gerada contém `/raw/upload/`
- [ ] PDF abre corretamente no navegador

---

## TESTE COM DIFERENTES FORMATOS

### Documentos (devem usar `/raw/upload/`)
- [ ] PDF (.pdf) - Relatório Final
- [ ] DOCX (.docx) - Relatório Word
- [ ] PPTX (.pptx) - Apresentação
- [ ] CSV (.csv) - Dados
- [ ] TXT (.txt) - Texto

### Imagens (devem usar `/image/upload/`)
- [ ] JPG (.jpg) - Foto da Equipe
- [ ] PNG (.png) - Foto
- [ ] WEBP (.webp) - Foto

---

## SOLUÇÃO DE PROBLEMAS

### Problema 1: URL ainda tem `/image/upload/`

**Causa:** Arquivo foi enviado antes da correção.

**Solução:**
1. Delete o arquivo antigo
2. Faça novo upload
3. Verifique novamente a URL

### Problema 2: PDF não abre (erro 404)

**Causa:** Migração não foi aplicada OU arquivo muito grande.

**Solução:**
1. Verifique tamanho (limite: 10MB no free tier)
2. Verifique logs do Railway para confirmar migração
3. Se necessário, force redeploy no Railway

### Problema 3: "OperationalError: column does not exist"

**Causa:** Migração não foi aplicada.

**Solução:**
1. Acesse Railway → seu projeto
2. Settings → Redeploy
3. Aguarde deploy completar
4. Tente novamente

### Problema 4: Upload funciona mas download dá erro

**Causa:** Cloudinary credentials erradas.

**Solução:**
1. Verifique variáveis de ambiente no Railway:
   ```
   CLOUDINARY_CLOUD_NAME=dyh2rsljf
   CLOUDINARY_API_KEY=837349511372969
   CLOUDINARY_API_SECRET=xH95tItuVO-tdzDG4SSwjwbc-NM
   ```
2. Se estiverem corretas, force redeploy

---

## TESTE COMPLETO: FLUXO REAL

### Cenário: Projeto de Qualidade da Água

1. **Login como estudante**
   - Usuário: `estudante`
   - Senha: `senha123`

2. **Criar/acessar projeto**
   - Entre em um projeto qualquer
   - Ou crie um novo para teste

3. **Upload de múltiplos arquivos**
   - Relatório Final: `relatorio_agua.pdf` (10 páginas)
   - Apresentação: `slides_agua.pptx` (15 slides)
   - Foto Equipe: `equipe.jpg`
   - Anexo 1: `dados_coleta.csv`
   - Anexo 2: `analise_laboratorio.pdf`

4. **Verificar cada arquivo**
   - Clique em cada link
   - Verifique se abre corretamente
   - PDFs/DOCX/CSV devem ter `/raw/upload/` na URL
   - Imagens devem ter `/image/upload/` na URL

5. **Teste de download**
   - Clique com botão direito → "Salvar como"
   - Verifique se o arquivo baixado abre localmente

---

## RESULTADO ESPERADO

**✅ SUCESSO:**
- Todos os PDFs abrem no navegador
- URLs contêm `/raw/upload/` para documentos
- URLs contêm `/image/upload/` para imagens
- Downloads funcionam
- Arquivos não desaparecem após redeploy

**❌ FALHA:**
- PDFs dão erro 404
- URLs ainda têm `/image/upload/` para PDFs
- Arquivos não abrem

---

## CONTATO PARA SUPORTE

Se após todos esses testes ainda não funcionar:

1. **Copie o link exato do PDF que não abre**
2. **Copie os logs do Railway** (últimas 50 linhas)
3. **Tire screenshot** do formulário de upload
4. **Reporte** no GitHub com essas informações

---

## REFERÊNCIAS

- **Documentação:** `CLOUDINARY_DOCUMENTOS.md`
- **Variáveis:** `VARIAVEIS_AMBIENTE.md`
- **Setup:** `RAILWAY_CLOUDINARY_SETUP.md`

