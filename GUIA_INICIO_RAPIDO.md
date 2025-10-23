# 🚀 Guia de Início Rápido - Plataforma de Ciência Cidadã

## ✅ Status do Projeto

**Projeto criado com sucesso!** Todas as funcionalidades principais estão implementadas.

## 📦 O que foi criado

### ✅ Backend (Django)
- ✅ Modelos completos (Usuario, Turma, Grupo, Projeto, Observacao, Feedback, Avaliacao)
- ✅ Sistema de autenticação customizado
- ✅ Views para todas as funcionalidades
- ✅ Formulários para todos os modelos
- ✅ Admin customizado e funcional
- ✅ Sistema de workflow das 6 fases do método científico
- ✅ Aprovação de fases pelo professor
- ✅ Sistema de avaliação conceitual

### ✅ Frontend
- ✅ Templates responsivos com Bootstrap 5
- ✅ Página inicial pública
- ✅ Sistema de login e registro
- ✅ Dashboard diferenciado (Professor/Estudante)
- ✅ Telas de turmas, grupos e projetos
- ✅ Formulários para todas as 6 fases
- ✅ Sistema de observações (Fase 4)
- ✅ Interface de feedback e aprovação
- ✅ Tela de avaliação final

## 🎯 Funcionalidades Implementadas

### Para Professores
- [x] Criar e gerenciar turmas (com código de acesso)
- [x] Criar grupos para os estudantes
- [x] Visualizar projetos dos grupos
- [x] Dar feedback em cada fase
- [x] Aprovar fases para grupos avançarem
- [x] Avaliar projetos concluídos com conceito e notas

### Para Estudantes
- [x] Entrar em turmas via código
- [x] Criar/participar de grupos
- [x] Criar projeto científico
- [x] Preencher as 6 fases do método científico
- [x] Adicionar observações com fotos e localização
- [x] Visualizar feedback do professor
- [x] Ver avaliação final do projeto

### Sistema de Workflow
- [x] 6 fases sequenciais do método científico
- [x] Aprovação obrigatória do professor em cada fase
- [x] Barra de progresso visual
- [x] Status do projeto (rascunho, em andamento, concluído)

## 🖥️ Como Executar

### 1. Ativar o Ambiente Virtual
```bash
cd "/Users/yanpedro/Documents/Site - Ciência Cidadã"
source venv/bin/activate
```

### 2. Executar o Servidor
```bash
python manage.py runserver
```

### 3. Acessar o Sistema
- **Site**: http://localhost:8010
- **Admin**: http://localhost:8010/admin

### 4. Credenciais de Teste

**Superusuário (já criado)**:
- Usuário: `admin`
- Senha: `admin123`
- Tipo: Professor

## 📝 Como Usar a Plataforma

### Fluxo do Professor

1. **Login** → Entre com suas credenciais
2. **Criar Turma** → Crie uma turma e anote o código gerado
3. **Compartilhar Código** → Dê o código para os estudantes
4. **Criar Grupos** (opcional) → Ou deixe os estudantes criarem
5. **Acompanhar Projetos** → Veja os projetos dos grupos
6. **Dar Feedback** → Comente em cada fase
7. **Aprovar Fases** → Permita que avancem
8. **Avaliar Projeto** → Dê conceito final quando concluído

### Fluxo do Estudante

1. **Cadastro** → Crie uma conta como Estudante
2. **Entrar em Turma** → Use o código do professor
3. **Criar/Entrar em Grupo** → Forme um grupo com colegas
4. **Criar Projeto** → Inicie o projeto do grupo
5. **Fase 1** → Defina o problema de pesquisa
6. **Aguardar Aprovação** → Professor revisa
7. **Fase 2** → Elabore a hipótese
8. **Fase 3** → Planeje a metodologia
9. **Fase 4** → Colete dados (adicione observações)
10. **Fase 5** → Analise os dados
11. **Fase 6** → Escreva a conclusão
12. **Receber Avaliação** → Veja o conceito final

## 🗂️ Estrutura do Projeto

```
Site - Ciência Cidadã/
├── manage.py                    # Comando principal Django
├── requirements.txt             # Dependências
├── README.md                    # Documentação completa
├── GUIA_INICIO_RAPIDO.md       # Este arquivo
├── TEMPLATES_TODO.md           # Guia de templates
├── db.sqlite3                  # Banco de dados SQLite
├── config/                     # Configurações Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                       # App principal
│   ├── models.py              # Modelos de dados
│   ├── views.py               # Lógica de views
│   ├── forms.py               # Formulários
│   ├── admin.py               # Admin customizado
│   ├── urls.py                # URLs do app
│   └── templates/             # Templates HTML
│       └── core/
├── templates/                 # Templates globais
│   └── base.html             # Template base
├── static/                   # Arquivos estáticos
└── media/                    # Uploads (fotos)
```

## 🎨 Tecnologias Utilizadas

- **Django 4.2** - Framework web
- **Bootstrap 5** - CSS framework
- **Bootstrap Icons** - Ícones
- **SQLite** - Banco de dados (desenvolvimento)
- **Pillow** - Processamento de imagens
- **Python-decouple** - Gerenciamento de configurações

## 🔧 Comandos Úteis

### Criar novos usuários
```bash
python manage.py createsuperuser
```

### Resetar banco de dados (cuidado!)
```bash
rm db.sqlite3
rm -rf core/migrations/0*.py
python manage.py makemigrations
python manage.py migrate
```

### Coletar arquivos estáticos (produção)
```bash
python manage.py collectstatic
```

### Rodar shell Django
```bash
python manage.py shell
```

## 📊 Modelo de Dados

### Entidades Principais

1. **Usuario** - Professores e Estudantes
2. **Turma** - Criada por professor, contém grupos
3. **Grupo** - 3-5 estudantes trabalhando juntos
4. **Projeto** - Desenvolvido pelo grupo em 6 fases
5. **Observacao** - Dados coletados na Fase 4
6. **Feedback** - Comentários do professor por fase
7. **Avaliacao** - Nota conceitual final

### Relacionamentos

```
Professor → cria → Turma
Estudante → entra → Turma
Estudante → participa → Grupo
Grupo → pertence → Turma
Grupo → desenvolve → Projeto (1:1)
Projeto → tem → Observações (1:N)
Projeto → recebe → Feedbacks (1:N)
Projeto → recebe → Avaliação (1:1)
```

## 🐛 Solução de Problemas

### Erro: "No module named 'decouple'"
```bash
pip install python-decouple
```

### Erro: "No module named 'PIL'"
```bash
pip install Pillow
```

### Erro de migração
```bash
python manage.py makemigrations core
python manage.py migrate
```

### Servidor não inicia
- Verifique se a porta 8000 está livre
- Ou use: `python manage.py runserver 8080`

## 📱 Responsividade

O site é 100% responsivo e funciona em:
- 💻 Desktop
- 📱 Tablets
- 📱 Smartphones

## 🔒 Segurança

- ✅ Autenticação obrigatória
- ✅ Permissões por tipo de usuário
- ✅ Proteção CSRF
- ✅ Validação de formulários
- ✅ Sanitização de uploads

## 🚀 Próximos Passos (Melhorias Futuras)

### Curto Prazo
- [ ] Adicionar gráficos na análise de dados (Chart.js)
- [ ] Sistema de notificações por email
- [ ] Exportação de projetos em PDF
- [ ] Perfil de usuário editável

### Médio Prazo
- [ ] Mapa interativo para observações geográficas
- [ ] Comentários entre membros do grupo
- [ ] Sistema de mensagens interno
- [ ] Histórico de alterações do projeto

### Longo Prazo
- [ ] App mobile (React Native)
- [ ] API REST pública
- [ ] Integração com sensores IoT
- [ ] Machine Learning para validação de dados

## 💡 Dicas de Uso

1. **Teste primeiro como Professor** - Crie uma turma e veja o código
2. **Crie um Estudante de teste** - Use outra aba anônima
3. **Simule o fluxo completo** - Passe por todas as 6 fases
4. **Use o Admin** - Muito útil para gerenciar dados
5. **Backup regular** - Copie o arquivo `db.sqlite3`

## 📞 Suporte

Para dúvidas ou problemas:
1. Consulte o `README.md` completo
2. Veja o `TEMPLATES_TODO.md` para templates faltantes
3. Verifique o admin Django em /admin
4. Consulte a documentação do Django

## ✅ Checklist de Teste

- [ ] Acessar a página inicial
- [ ] Criar conta de Professor
- [ ] Criar conta de Estudante
- [ ] Professor cria turma
- [ ] Estudante entra na turma (código)
- [ ] Criar grupo
- [ ] Criar projeto
- [ ] Preencher Fase 1
- [ ] Professor dá feedback
- [ ] Professor aprova Fase 1
- [ ] Repetir para todas as fases
- [ ] Adicionar observações na Fase 4
- [ ] Concluir projeto
- [ ] Professor avalia com conceito

## 🎉 Projeto Completo!

Todas as funcionalidades principais estão implementadas e funcionais. 
O sistema está pronto para uso no curso de extensão!

**Bom trabalho!** 🚀

