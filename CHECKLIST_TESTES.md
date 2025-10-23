# ✅ Checklist de Testes - Plataforma de Ciência Cidadã

Use este checklist para validar que todas as funcionalidades estão operacionais.

---

## 🏠 Testes Básicos

### Página Inicial
- [ ] Acessar http://localhost:8010
- [ ] Verificar que a página carrega
- [ ] Links de Login e Cadastro funcionam
- [ ] Layout responsivo (testar redimensionando janela)
- [ ] Estatísticas aparecem (projetos, estudantes)

### Sistema de Autenticação
- [ ] Cadastrar novo usuário (Professor)
- [ ] Cadastrar novo usuário (Estudante)
- [ ] Fazer login como Professor
- [ ] Fazer login como Estudante
- [ ] Fazer logout
- [ ] Tentar acessar página protegida sem login (deve redirecionar)

---

## 👨‍🏫 Testes do Professor

### Dashboard
- [ ] Login como professor
- [ ] Ver dashboard do professor
- [ ] Verificar estatísticas
- [ ] Botão "Nova Turma" aparece

### Gerenciar Turmas
- [ ] Criar nova turma
- [ ] Código de acesso é gerado automaticamente
- [ ] Turma aparece no dashboard
- [ ] Editar turma existente
- [ ] Ver detalhes da turma
- [ ] Desativar turma

### Gerenciar Grupos
- [ ] Criar grupo em uma turma
- [ ] Adicionar membros ao grupo
- [ ] Definir líder do grupo
- [ ] Editar grupo
- [ ] Ver detalhes do grupo

### Acompanhar Projetos
- [ ] Ver lista de projetos das turmas
- [ ] Abrir detalhes de um projeto
- [ ] Ver todas as 6 fases do projeto
- [ ] Verificar status e progresso visual

### Dar Feedback
- [ ] Abrir um projeto em andamento
- [ ] Clicar em "Dar Feedback"
- [ ] Escrever comentário
- [ ] Marcar "Aprovar fase" (ou não)
- [ ] Enviar feedback
- [ ] Verificar que feedback aparece no projeto

### Aprovar Fases
- [ ] Abrir projeto na Fase 1
- [ ] Clicar em "Aprovar Fase 1"
- [ ] Confirmar aprovação
- [ ] Verificar que projeto avançou para Fase 2
- [ ] Repetir para outras fases

### Avaliar Projeto
- [ ] Abrir projeto concluído (todas 6 fases aprovadas)
- [ ] Clicar em "Avaliar Projeto"
- [ ] Preencher conceito (A, B, C, D)
- [ ] Dar notas para cada fase (0-10)
- [ ] Escrever feedback qualitativo
- [ ] Salvar avaliação
- [ ] Verificar que avaliação aparece no projeto

---

## 👨‍🎓 Testes do Estudante

### Dashboard
- [ ] Login como estudante
- [ ] Ver dashboard do estudante
- [ ] Verificar estatísticas
- [ ] Botão "Entrar em Turma" aparece

### Entrar em Turma
- [ ] Clicar em "Entrar em Turma"
- [ ] Digitar código da turma
- [ ] Entrar com sucesso
- [ ] Turma aparece no dashboard
- [ ] Tentar entrar com código inválido (deve dar erro)
- [ ] Tentar entrar na mesma turma novamente (deve avisar)

### Participar de Grupo
- [ ] Ver lista de grupos da turma
- [ ] Criar novo grupo
- [ ] OU entrar em grupo existente
- [ ] Grupo aparece no dashboard

### Criar Projeto
- [ ] Abrir grupo
- [ ] Clicar em "Criar Projeto"
- [ ] Preencher informações básicas
  - Título
  - Área da ciência
  - Descrição breve
- [ ] Criar projeto
- [ ] Ser redirecionado para Fase 1

### Fase 1: Problema de Pesquisa
- [ ] Preencher pergunta de pesquisa
- [ ] Preencher justificativa
- [ ] Preencher objetivos
- [ ] Salvar Fase 1
- [ ] Voltar ao projeto
- [ ] Verificar que dados foram salvos
- [ ] Aguardar aprovação do professor

### Fase 2: Hipótese
- [ ] Após Fase 1 aprovada, acessar Fase 2
- [ ] Preencher hipótese principal
- [ ] Preencher fundamentação
- [ ] Salvar Fase 2
- [ ] Verificar que dados foram salvos

### Fase 3: Metodologia
- [ ] Após Fase 2 aprovada, acessar Fase 3
- [ ] Preencher método de coleta
- [ ] Preencher materiais
- [ ] Preencher cronograma
- [ ] Preencher local da pesquisa
- [ ] Salvar Fase 3

### Fase 4: Coleta de Dados
- [ ] Após Fase 3 aprovada, estar na Fase 4
- [ ] Clicar em "Adicionar Observação"
- [ ] Preencher título da observação
- [ ] Preencher descrição
- [ ] Upload de foto 1
- [ ] Upload de foto 2 (opcional)
- [ ] Preencher local
- [ ] Preencher latitude/longitude (opcional)
- [ ] Preencher data/hora da coleta
- [ ] Salvar observação
- [ ] Observação aparece na lista
- [ ] Adicionar mais 2-3 observações
- [ ] Editar uma observação
- [ ] Excluir uma observação

### Fase 5: Análise de Dados
- [ ] Após Fase 4 aprovada, acessar Fase 5
- [ ] Preencher organização dos dados
- [ ] Preencher interpretação
- [ ] Preencher discussão
- [ ] Salvar Fase 5

### Fase 6: Conclusão
- [ ] Após Fase 5 aprovada, acessar Fase 6
- [ ] Selecionar se hipótese foi confirmada
- [ ] Escrever conclusão
- [ ] Escrever aprendizados
- [ ] Escrever limitações
- [ ] Salvar Fase 6
- [ ] Projeto muda status para "Aguardando Aprovação"

### Projeto Concluído
- [ ] Após Fase 6 aprovada
- [ ] Projeto muda status para "Concluído"
- [ ] Ver avaliação do professor
- [ ] Ver conceito final
- [ ] Ver notas por fase
- [ ] Ver feedback qualitativo

---

## 🔄 Testes de Fluxo Completo

### Fluxo 1: Professor → Estudante → Projeto Completo

1. **Professor**
   - [ ] Criar turma "Turma Teste 2024"
   - [ ] Anotar código (ex: ABC12345)
   - [ ] Criar grupo "Grupo Água"
   - [ ] Adicionar 3 estudantes fictícios (criar contas)

2. **Estudante 1**
   - [ ] Entrar na turma com código
   - [ ] Entrar no "Grupo Água"
   - [ ] Criar projeto "Qualidade da Água"

3. **Estudante 1 (continua)**
   - [ ] Preencher Fase 1
   - [ ] Aguardar

4. **Professor**
   - [ ] Ver projeto no dashboard
   - [ ] Dar feedback na Fase 1
   - [ ] Aprovar Fase 1

5. **Estudante 1**
   - [ ] Ver feedback recebido
   - [ ] Preencher Fase 2
   - [ ] Aguardar

6. **Repetir passos 4-5 para Fases 2-6**

7. **Estudante 1 (Fase 4)**
   - [ ] Adicionar 5 observações
   - [ ] Com fotos
   - [ ] Com localizações

8. **Professor (Final)**
   - [ ] Aprovar Fase 6
   - [ ] Projeto concluído
   - [ ] Avaliar projeto
   - [ ] Dar conceito A
   - [ ] Preencher todas as notas

9. **Estudante 1 (Verificação)**
   - [ ] Ver projeto concluído
   - [ ] Ver avaliação
   - [ ] Ver conceito

---

## 🔐 Testes de Segurança/Permissões

### Isolamento de Dados
- [ ] Professor A não vê turmas do Professor B
- [ ] Estudante A não vê projetos do Estudante B (de outras turmas)
- [ ] Estudante não pode aprovar fases
- [ ] Professor não pode editar projeto de outro professor

### Validações
- [ ] Tentar criar turma sem nome (deve dar erro)
- [ ] Tentar criar grupo sem membros (deve dar erro)
- [ ] Tentar criar projeto sem área (deve dar erro)
- [ ] Tentar avançar fase sem aprovação (deve bloquear)
- [ ] Upload de arquivo muito grande (deve limitar)
- [ ] Upload de arquivo não-imagem em foto (deve rejeitar)

### Autenticação
- [ ] Tentar acessar /dashboard sem login (redireciona para /login)
- [ ] Tentar acessar /admin sem permissão (bloqueia)
- [ ] Logout limpa sessão corretamente

---

## 🎨 Testes de Interface

### Responsividade
- [ ] Abrir em desktop (1920x1080)
- [ ] Abrir em tablet (768x1024)
- [ ] Abrir em mobile (375x667)
- [ ] Menu hamburguer funciona em mobile
- [ ] Cards adaptam-se ao tamanho da tela
- [ ] Tabelas são scrolláveis em mobile

### Usabilidade
- [ ] Todos os botões têm ícones claros
- [ ] Mensagens de sucesso aparecem (verde)
- [ ] Mensagens de erro aparecem (vermelho)
- [ ] Breadcrumbs funcionam
- [ ] Links de navegação funcionam
- [ ] Hover nos cards funciona

### Visual
- [ ] Cores consistentes (tema azul/verde)
- [ ] Badges coloridos por status
- [ ] Barra de progresso animada
- [ ] Ícones Bootstrap carregam
- [ ] Sem texto cortado
- [ ] Sem overlaps de elementos

---

## 🔧 Testes Técnicos

### Admin Django
- [ ] Acessar http://localhost:8010/admin
- [ ] Login com superusuário
- [ ] Ver todos os modelos listados
- [ ] Criar usuário via admin
- [ ] Editar turma via admin
- [ ] Ver estatísticas no admin

### Banco de Dados
- [ ] Dados salvos persistem após restart
- [ ] Relacionamentos mantidos (grupo→turma, projeto→grupo)
- [ ] Slugs gerados automaticamente
- [ ] Códigos de turma únicos

### Uploads
- [ ] Upload de foto de perfil funciona
- [ ] Upload de fotos de observação funciona
- [ ] Fotos aparecem corretamente
- [ ] Múltiplos uploads funcionam
- [ ] Arquivos salvos em /media

---

## 📊 Testes de Dados

### Populando Dados de Teste
- [ ] Criar 3 professores
- [ ] Criar 10 estudantes
- [ ] Criar 5 turmas
- [ ] Criar 10 grupos
- [ ] Criar 8 projetos
- [ ] Adicionar 30+ observações
- [ ] Sistema suporta carga

### Integridade
- [ ] Excluir turma não quebra sistema
- [ ] Excluir grupo não quebra projeto (se configurado)
- [ ] Excluir usuário trata dados órfãos
- [ ] Códigos de turma permanecem únicos

---

## 🚀 Testes de Performance

### Tempo de Carregamento
- [ ] Página inicial < 2s
- [ ] Dashboard < 2s
- [ ] Projeto com 20 observações < 3s
- [ ] Lista de 50 projetos < 3s

### Otimização
- [ ] Queries não fazem N+1
- [ ] Static files servidos corretamente
- [ ] Imagens carregam rápido
- [ ] Sem erros no console do navegador

---

## 📝 Testes de Conteúdo

### Textos
- [ ] Todos os textos em português correto
- [ ] Sem erros de ortografia
- [ ] Instruções claras
- [ ] Help texts úteis nos formulários

### Funcionalidades Educacionais
- [ ] 6 fases claramente separadas
- [ ] Workflow sequencial faz sentido
- [ ] Aprovação por fase é obrigatória
- [ ] Feedback é visível para estudantes
- [ ] Avaliação é justa e completa

---

## ✅ Checklist Final de Qualidade

### Antes de Entregar
- [ ] Todos os testes acima passaram
- [ ] README.md está completo
- [ ] GUIA_INICIO_RAPIDO.md está claro
- [ ] Código comentado onde necessário
- [ ] Sem console.logs ou debugs esquecidos
- [ ] requirements.txt atualizado
- [ ] .gitignore configurado
- [ ] Projeto roda do zero (testar em outra máquina se possível)

### Documentação
- [ ] README principal
- [ ] Guia de início rápido
- [ ] Guia de deploy
- [ ] Este checklist
- [ ] Resumo do projeto
- [ ] Templates TODO (para expansões)

---

## 🎯 Critérios de Aceitação

O projeto está pronto quando:

✅ **Funcionalidade**
- Todas as funcionalidades principais funcionam
- Workflow das 6 fases operacional
- Professor pode aprovar fases
- Sistema de avaliação funciona

✅ **Usabilidade**
- Interface intuitiva
- Responsivo em mobile
- Mensagens claras
- Sem erros visíveis

✅ **Técnico**
- Sem erros no console
- Código limpo e organizado
- Documentação completa
- Fácil de instalar e rodar

✅ **Educacional**
- Atende proposta pedagógica
- Guia estudantes pelo método científico
- Permite acompanhamento do professor
- Sistema de avaliação adequado

---

## 📊 Resultado dos Testes

Preencha conforme testa:

- Testes realizados: ___/150+
- Testes passados: ___/150+
- Bugs encontrados: ___
- Bugs críticos: ___
- Status: [ ] Pronto [ ] Precisa ajustes

---

**Data dos testes**: ___/___/___

**Testador**: _________________

**Observações**: 
```
[Espaço para anotações]
```

---

## 🐛 Bugs Conhecidos (se houver)

Liste aqui quaisquer bugs encontrados durante os testes:

1. _Nenhum conhecido no momento_

---

## 🎉 Conclusão

Após completar este checklist, o projeto está validado e pronto para uso!

**Boa sorte! 🚀**

