# DEBUG: Problema com PDFs no Cloudinary

## SITUAÇÃO ATUAL

**Link fornecido pelo usuário:**
```
https://res.cloudinary.com/dyh2rsljf/raw/upload/v1/media/anexos/projeto_beneficios-da-energia-solar_2_zv4psr.pdf
```

**Status:**
- ✅ URL contém `/raw/upload/` (correto)
- ❌ PDF não abre no navegador
- ✅ Novo upload já foi feito após correção

---

## POSSÍVEIS CAUSAS

### 1. Configuração de "resource_type" no Cloudinary

O Cloudinary tem 3 tipos de recursos:
- `image` - Imagens (JPG, PNG, etc.)
- `video` - Vídeos
- `raw` - Outros arquivos (PDF, DOCX, CSV, etc.)

**Diagnóstico:** Verificar se `DocumentStorage` está realmente usando `resource_type='raw'`.

### 2. Configurações de Upload no Cloudinary Dashboard

No dashboard do Cloudinary (https://cloudinary.com/console):

1. Vá em **Settings** → **Upload**
2. Verifique **Upload presets**
3. Procure por restrições de formato
4. Verifique se PDFs estão bloqueados

### 3. Limite de Tamanho

**Free tier do Cloudinary:**
- Máximo de **10MB** por arquivo
- Máximo de **25 créditos** de transformação/mês

**Verificar:**
- Tamanho do PDF enviado
- Uso de créditos no dashboard

### 4. CORS (Cross-Origin Resource Sharing)

PDFs podem ser bloqueados por CORS se acessados de domínio diferente.

**Teste:**
1. Abra o link diretamente no navegador (não pelo site)
2. Se funcionar → problema de CORS
3. Se não funcionar → problema no Cloudinary

### 5. Nome do Arquivo

O nome tem caracteres especiais que podem causar problema:
```
projeto_beneficios-da-energia-solar_2_zv4psr.pdf
```

**Possíveis problemas:**
- Underscores múltiplos
- Hífens no nome
- Nome muito longo

---

## TESTES PARA FAZER

### Teste 1: Acessar Diretamente

1. Copie o link completo
2. Cole em uma nova aba do navegador
3. Pressione Enter

**Resultado esperado:** PDF deve abrir OU iniciar download

### Teste 2: cURL (Terminal)

```bash
curl -I "https://res.cloudinary.com/dyh2rsljf/raw/upload/v1/media/anexos/projeto_beneficios-da-energia-solar_2_zv4psr.pdf"
```

**Verificar:**
- Status Code (deve ser 200)
- Content-Type (deve ser `application/pdf`)
- Content-Length (tamanho do arquivo)

### Teste 3: Arquivo Simples

1. Crie um PDF **muito simples** (1 página, texto básico)
2. Tamanho máximo: 1MB
3. Nome simples: `teste.pdf`
4. Faça upload
5. Teste o link gerado

### Teste 4: Dashboard do Cloudinary

1. Acesse https://cloudinary.com/console
2. Vá em **Media Library**
3. Procure pelo arquivo `projeto_beneficios-da-energia-solar_2_zv4psr.pdf`
4. Clique nele
5. Verifique:
   - Tipo de recurso (deve ser "Raw")
   - Tamanho
   - URL pública

### Teste 5: Download vs Visualização

Adicione parâmetros à URL:

**Forçar download:**
```
https://res.cloudinary.com/dyh2rsljf/raw/upload/fl_attachment/v1/media/anexos/projeto_beneficios-da-energia-solar_2_zv4psr.pdf
```

**Inline (visualizar):**
```
https://res.cloudinary.com/dyh2rsljf/raw/upload/fl_attachment:false/v1/media/anexos/projeto_beneficios-da-energia-solar_2_zv4psr.pdf
```

---

## SOLUÇÃO PROVISÓRIA: Download em vez de Visualização

Se o problema for do navegador não conseguir visualizar inline, podemos forçar download.

### Alterar View para Forçar Download

Em `core/views.py`, criar uma view proxy:

```python
from django.http import FileResponse, HttpResponse
import urllib.request

@login_required
def download_anexo(request, slug, campo):
    """Proxy para download de anexo via Cloudinary"""
    projeto = get_object_or_404(Projeto, slug=slug)
    
    # Verificar permissão
    if request.user.is_estudante():
        if request.user not in projeto.grupo.membros.all():
            return HttpResponse("Sem permissão", status=403)
    
    # Pegar arquivo
    arquivo = getattr(projeto, campo)
    if not arquivo:
        return HttpResponse("Arquivo não encontrado", status=404)
    
    # Download do Cloudinary
    response = urllib.request.urlopen(arquivo.url)
    file_data = response.read()
    
    # Retornar como download
    http_response = HttpResponse(file_data, content_type='application/pdf')
    http_response['Content-Disposition'] = f'attachment; filename="{campo}.pdf"'
    return http_response
```

---

## SOLUÇÃO ALTERNATIVA: Usar Signed URLs

PDFs podem estar sendo bloqueados por serem públicos. Cloudinary permite signed URLs:

```python
import cloudinary.utils

def get_signed_url(public_id):
    """Gerar URL assinada com expiração"""
    return cloudinary.utils.cloudinary_url(
        public_id,
        resource_type="raw",
        sign_url=True,
        type="authenticated"
    )[0]
```

---

## VERIFICAR LOGS DO RAILWAY

No Railway, vá em **Deployments** → **Logs** e procure por erros relacionados a:
- Cloudinary
- Upload de arquivos
- Exceções durante `projeto_anexos`

---

## CHECKLIST DE DIAGNÓSTICO

- [ ] Testei o link diretamente no navegador (nova aba)
- [ ] Verifiquei o console do navegador (F12) para erros
- [ ] Acessei o dashboard do Cloudinary e encontrei o arquivo
- [ ] Verifiquei o tipo de recurso no Cloudinary (deve ser "Raw")
- [ ] Tamanho do arquivo é menor que 10MB
- [ ] Testei com cURL no terminal
- [ ] Criei PDF simples de teste (teste.pdf)
- [ ] Verifiquei logs do Railway

---

## SOLUÇÃO RÁPIDA: Forçar Download

Enquanto não resolvemos o problema de visualização inline, você pode:

1. **Adicionar aviso no template:**
   "Se o PDF não abrir, clique com botão direito → Salvar link como"

2. **Mudar texto do link:**
   Em vez de "Ver Arquivo", usar "Baixar Arquivo"

3. **Adicionar JavaScript para forçar download:**
```html
<a href="{{ projeto.relatorio_final.url }}" download class="btn btn-primary">
    <i class="bi bi-download"></i> Baixar PDF
</a>
```

---

## RESPOSTA PARA O USUÁRIO

**Por favor, faça os seguintes testes:**

1. **Teste 1:** Copie este link e cole em uma NOVA ABA do navegador (não clique pelo site):
   ```
   https://res.cloudinary.com/dyh2rsljf/raw/upload/v1/media/anexos/projeto_beneficios-da-energia-solar_2_zv4psr.pdf
   ```
   
2. **Teste 2:** Pressione F12 no navegador, vá na aba "Console" e me diga se aparece algum erro em vermelho

3. **Teste 3:** Acesse https://cloudinary.com/console/c-1a7c8e9f8c9d3e5a/media_library/folders/home?view_mode=list
   - Procure pelo arquivo
   - Veja se ele está lá
   - Qual o "Resource Type" dele?

4. **Teste 4:** Qual o tamanho do PDF? (Verifique no Windows Explorer ou Finder)

5. **Teste 5:** Tente fazer upload de um PDF BEM SIMPLES (1 página, <1MB) com nome `teste.pdf` e veja se funciona

---

**Me envie os resultados desses testes que eu vou saber exatamente qual é o problema!**

