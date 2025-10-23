# 🚀 Deploy no PythonAnywhere - Passo a Passo

## ✅ **Pré-requisitos**
- ✅ Projeto Django funcionando localmente
- ✅ Conta no GitHub (para subir o código)
- ✅ 30 minutos de tempo

---

## 📦 **PASSO 1: Subir Projeto no GitHub** (10 min)

### 1.1 Criar repositório no GitHub

1. Acesse https://github.com/new
2. Nome do repositório: `ciencia-cidada` (ou outro nome)
3. **Deixe PRIVADO** se quiser
4. **NÃO** adicione README, .gitignore ou license
5. Clique em **Create repository**

### 1.2 Subir código do seu computador

Abra o terminal e execute:

```bash
cd "/Users/yanpedro/Documents/Site - Ciência Cidadã"

# Verificar se já tem git iniciado
git status

# Se não tiver, inicializar
git init

# Adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Deploy inicial - Plataforma Ciência Cidadã"

# Conectar com GitHub (SUBSTITUA SEU_USUARIO e NOME_REPO)
git remote add origin https://github.com/SEU_USUARIO/ciencia-cidada.git

# Subir para GitHub
git branch -M main
git push -u origin main
```

**✅ Seu código agora está no GitHub!**

---

## 🌐 **PASSO 2: Criar Conta no PythonAnywhere** (5 min)

1. Acesse https://www.pythonanywhere.com
2. Clique em **Start running Python online in less than a minute!**
3. Clique em **Create a Beginner account**
4. Preencha:
   - Username: escolha um (será sua URL: `seuusuario.pythonanywhere.com`)
   - Email
   - Senha
5. Confirme email
6. Faça login

**✅ Conta criada!**

---

## 💻 **PASSO 3: Clonar Projeto no PythonAnywhere** (5 min)

### 3.1 Abrir Console Bash

1. No dashboard do PythonAnywhere
2. Clique na aba **Consoles**
3. Clique em **Bash**
4. Um terminal vai abrir

### 3.2 Clonar seu repositório

No console Bash do PythonAnywhere, digite:

```bash
# Clonar do GitHub (SUBSTITUA SEU_USUARIO e NOME_REPO)
git clone https://github.com/SEU_USUARIO/ciencia-cidada.git

# Entrar na pasta
cd ciencia-cidada

# Ver arquivos
ls
```

**✅ Código agora está no PythonAnywhere!**

---

## 🐍 **PASSO 4: Configurar Ambiente Virtual** (5 min)

No mesmo console Bash:

```bash
# Criar ambiente virtual com Python 3.10
mkvirtualenv --python=/usr/bin/python3.10 ciencia_cidada

# Verificar se ativou (vai aparecer (ciencia_cidada) no início da linha)

# Instalar dependências
pip install django==4.2.7 pillow python-decouple

# Verificar instalação
python --version
django-admin --version
```

**✅ Ambiente configurado!**

---

## 🗄️ **PASSO 5: Configurar Banco de Dados** (3 min)

```bash
# Certifique-se de estar na pasta do projeto
cd ~/ciencia-cidada

# Rodar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser
# Você vai ser perguntado:
# - Username: admin (ou outro)
# - Email: seu@email.com
# - Password: ******** (digite duas vezes)

# Coletar arquivos estáticos
python manage.py collectstatic --noinput
```

**✅ Banco configurado!**

---

## 🌐 **PASSO 6: Configurar Web App** (10 min)

### 6.1 Criar Web App

1. Volte ao Dashboard (clique em **Dashboard** no topo)
2. Clique na aba **Web**
3. Clique em **Add a new web app**
4. Clique em **Next**
5. Selecione **Manual configuration**
6. Selecione **Python 3.10**
7. Clique em **Next**

### 6.2 Configurar Virtual Environment

Na página do Web App:

1. Role até a seção **Virtualenv**
2. No campo **Enter path to a virtualenv**, digite:
   ```
   /home/SEUUSUARIO/.virtualenvs/ciencia_cidada
   ```
   (SUBSTITUA `SEUUSUARIO` pelo seu username do PythonAnywhere)
3. Clique no ✓ (check) para salvar

### 6.3 Configurar WSGI

1. Role até **Code**
2. Clique no link **WSGI configuration file** (vai abrir um editor)
3. **DELETE TODO O CONTEÚDO** do arquivo
4. Cole este código (SUBSTITUA `SEUUSUARIO`):

```python
import os
import sys

# Adicionar pasta do projeto ao path
path = '/home/SEUUSUARIO/ciencia-cidada'
if path not in sys.path:
    sys.path.insert(0, path)

# Configurar Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# Importar aplicação WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

5. Clique em **Save** (canto superior direito)

### 6.4 Configurar Static Files

Volte à página do Web App e role até **Static files**:

1. Clique em **Enter URL** → Digite: `/static/`
2. Clique em **Enter path** → Digite: `/home/SEUUSUARIO/ciencia-cidada/staticfiles`
3. Clique no ✓

4. Adicione mais um:
   - URL: `/media/`
   - Path: `/home/SEUUSUARIO/ciencia-cidada/media`

### 6.5 Configurar Settings Django

No console Bash do PythonAnywhere:

```bash
cd ~/ciencia-cidada

# Editar settings.py
nano config/settings.py
```

Encontre a linha `ALLOWED_HOSTS = [...]` e altere para:

```python
ALLOWED_HOSTS = ['SEUUSUARIO.pythonanywhere.com', 'localhost', '127.0.0.1']
```

Pressione `Ctrl+O` para salvar, `Enter`, depois `Ctrl+X` para sair.

---

## 🚀 **PASSO 7: Recarregar e Testar** (2 min)

1. Volte à aba **Web** no PythonAnywhere
2. No topo, clique no botão verde **Reload SEUUSUARIO.pythonanywhere.com**
3. Aguarde recarregar (até 1 minuto)
4. Clique no link da sua URL: **https://SEUUSUARIO.pythonanywhere.com**

**🎉 SEU SITE ESTÁ NO AR!**

---

## ✅ **Verificar se Funcionou**

Teste estas URLs:

1. **Home**: `https://SEUUSUARIO.pythonanywhere.com/`
2. **Admin**: `https://SEUUSUARIO.pythonanywhere.com/admin`
3. **Login**: `https://SEUUSUARIO.pythonanywhere.com/login`

Se alguma página der erro 404 ou 500, veja seção de Troubleshooting abaixo.

---

## 🔧 **PASSO 8: Criar Dados de Teste** (opcional)

No console Bash:

```bash
cd ~/ciencia-cidada
python manage.py shell << 'EOF'
from core.models import Usuario

# Criar professor
prof = Usuario.objects.create_user(
    username='prof.teste',
    email='prof@escola.com',
    password='prof123',
    first_name='Professor',
    last_name='Teste',
    tipo='professor'
)

# Criar estudante
est = Usuario.objects.create_user(
    username='aluno.teste',
    email='aluno@escola.com',
    password='aluno123',
    first_name='Aluno',
    last_name='Teste',
    tipo='estudante'
)

print("✅ Usuários criados!")
EOF
```

---

## 🔄 **Como Atualizar o Site Depois**

Quando fizer alterações no código:

```bash
# 1. No seu computador, subir para GitHub
git add .
git commit -m "Descrição da alteração"
git push

# 2. No PythonAnywhere console Bash
cd ~/ciencia-cidada
git pull
python manage.py migrate  # Se alterou models
python manage.py collectstatic --noinput  # Se alterou CSS/JS

# 3. Na aba Web, clicar em Reload
```

---

## 🐛 **Troubleshooting (Problemas Comuns)**

### Erro 500 - Internal Server Error

**Causa**: Erro no código ou configuração

**Solução**:
1. Vá para **Web** → **Log files**
2. Clique em **Error log**
3. Veja o erro no final do arquivo
4. Corrija o erro e clique em **Reload**

### Static files não carregam (sem CSS)

**Solução**:
```bash
cd ~/ciencia-cidada
python manage.py collectstatic --noinput
```
Depois clique em **Reload** na aba Web

### Erro "DisallowedHost"

**Solução**:
```bash
nano config/settings.py
```
Adicione seu domínio em `ALLOWED_HOSTS`:
```python
ALLOWED_HOSTS = ['seuusuario.pythonanywhere.com']
```

### Imagens não aparecem

**Solução**:
1. Verifique se configurou `/media/` nos Static files
2. Verifique se o path está correto: `/home/SEUUSUARIO/ciencia-cidada/media`

---

## 📊 **Limitações do Plano Gratuito**

- ✅ 1 aplicação web
- ✅ 512MB de espaço
- ✅ 100 segundos de CPU/dia
- ✅ Funciona perfeitamente para curso de extensão!

**Para upgrade**: $5/mês (se precisar mais recursos)

---

## 🎯 **Checklist Final**

- [ ] Código no GitHub
- [ ] Conta PythonAnywhere criada
- [ ] Código clonado no PythonAnywhere
- [ ] Virtualenv configurado
- [ ] Dependências instaladas
- [ ] Migrações rodadas
- [ ] Superusuário criado
- [ ] Static files coletados
- [ ] Web App configurado
- [ ] WSGI configurado
- [ ] ALLOWED_HOSTS atualizado
- [ ] Site recarregado
- [ ] Site funcionando!

---

## 🎉 **Parabéns!**

Seu projeto está no ar e acessível de qualquer lugar!

**URL do seu site**: `https://SEUUSUARIO.pythonanywhere.com`

Compartilhe com seus alunos e professora! 🚀

---

## 📞 **Precisa de Ajuda?**

- 📚 Docs PythonAnywhere: https://help.pythonanywhere.com/
- 🐛 Se der erro, me mostre o error log
- 💬 Forum: https://www.pythonanywhere.com/forums/

---

**Desenvolvido com ❤️ - Outubro 2024**

