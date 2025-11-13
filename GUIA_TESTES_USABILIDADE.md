# GUIA DE TESTES DE USABILIDADE - PLATAFORMA CIÊNCIA CIDADÃ

## OBJETIVO DOS TESTES

Este documento serve como guia para realizar testes de usabilidade na plataforma Ciência Cidadã. O objetivo é avaliar a facilidade de uso, clareza da interface e eficiência dos fluxos de trabalho tanto para professores quanto para estudantes.

---

## PERFIS DE TESTE

### Professor
- **Username:** prof_teste
- **Senha:** prof123456

### Estudante 1
- **Username:** aluno1
- **Senha:** aluno123456

### Estudante 2
- **Username:** aluno2
- **Senha:** aluno123456

---

## CENÁRIO 1: FLUXO COMPLETO DO PROFESSOR

### 1.1 Autenticação e Dashboard

**Objetivo:** Verificar facilidade de acesso e clareza do dashboard

**Passos:**
1. Acesse a URL da plataforma
2. Faça login com as credenciais do professor
3. Observe o dashboard inicial

**O que avaliar:**
- [ ] Login foi rápido e intuitivo?
- [ ] Dashboard mostra informações relevantes (turmas, projetos pendentes)?
- [ ] Menu de navegação é claro e organizado?
- [ ] É fácil entender onde ir para cada funcionalidade?

**Pontos de atenção:**
- Tempo para encontrar cada seção
- Clareza dos ícones e textos
- Organização visual das informações

---

### 1.2 Criar Turma

**Objetivo:** Avaliar o processo de criação de turma

**Passos:**
1. No menu, clique em "Minhas Turmas"
2. Clique em "Criar Turma"
3. Preencha os campos:
   - Nome: "Turma de Teste Usabilidade"
   - Descrição: "Turma para testes de usabilidade da plataforma"
   - Ano/Semestre: "2024.2"
   - Máximo de grupos: 5
   - Máximo de membros por grupo: 4
4. Salve a turma
5. Observe o código de acesso gerado

**O que avaliar:**
- [ ] Campos do formulário são claros?
- [ ] Labels e placeholders ajudam a preencher?
- [ ] Código de acesso é destacado claramente?
- [ ] Mensagem de sucesso é clara?

**Pontos de atenção:**
- Dificuldades no preenchimento
- Dúvidas sobre algum campo
- Visibilidade do código de acesso

---

### 1.3 Criar Atividade para Turma

**Objetivo:** Testar a funcionalidade de postar atividades/avisos

**Passos:**
1. Entre na turma recém-criada
2. Clique em "Atividades"
3. Clique em "Nova Atividade"
4. Crie uma atividade do tipo "Aviso":
   - Título: "Bem-vindos à disciplina!"
   - Tipo: Aviso
   - Descrição: "Olá turma! Sejam bem-vindos. Nossa primeira tarefa será definir o problema de pesquisa."
   - Fixar no topo: Sim
5. Salve a atividade
6. Crie outra atividade do tipo "Tarefa":
   - Título: "Definir tema do projeto"
   - Tipo: Tarefa
   - Descrição: "Em grupo, escolham um tema científico de interesse e preparem uma pergunta de pesquisa."
   - Data de Entrega: (próxima semana)
7. Salve a tarefa

**O que avaliar:**
- [ ] Processo de criação de atividade é intuitivo?
- [ ] Diferença entre tipos de atividade está clara?
- [ ] Campo de data funciona bem?
- [ ] É fácil visualizar atividades criadas?
- [ ] Atividade fixada aparece em destaque?

**Pontos de atenção:**
- Facilidade de editar/excluir atividades
- Clareza visual dos tipos de atividade
- Organização da lista de atividades

---

### 1.4 Criar Grupo

**Objetivo:** Avaliar criação de grupos na turma

**Passos:**
1. Volte aos detalhes da turma
2. Clique em "Criar Grupo"
3. Crie um grupo:
   - Nome: "Grupo Alpha"
   - Selecione 2-3 estudantes
   - Defina um líder
4. Salve o grupo

**O que avaliar:**
- [ ] Processo de seleção de membros é claro?
- [ ] É fácil definir o líder?
- [ ] Visualização do grupo criado é adequada?

---

### 1.5 Avaliar Projeto (Fases)

**Objetivo:** Testar aprovação de fases do método científico

**Passos:**
1. Navegue até "Projetos"
2. Abra um projeto existente (se houver)
3. Leia a Fase 1 (Problema de Pesquisa)
4. Clique em "Dar Feedback - Fase 1"
5. Escreva um feedback construtivo
6. Marque como "Aprovado"
7. Salve o feedback
8. Verifique se o projeto avançou para Fase 2

**O que avaliar:**
- [ ] É fácil entender em qual fase o projeto está?
- [ ] Formulário de feedback é claro?
- [ ] Opção de aprovação está visível?
- [ ] Fluxo de aprovação e avanço é compreensível?

**Pontos de atenção:**
- Clareza do progresso visual (barra, badges)
- Facilidade de navegação entre fases
- Histórico de feedbacks visível

---

### 1.6 Avaliar Projeto Final

**Objetivo:** Testar avaliação conceitual final

**Passos:**
1. Encontre um projeto concluído (todas as 6 fases aprovadas)
2. Clique em "Avaliar Projeto"
3. Preencha:
   - Conceito Final: B
   - Notas por fase (0-10)
   - Comentários gerais
   - Pontos fortes
   - Pontos a melhorar
4. Salve a avaliação

**O que avaliar:**
- [ ] Formulário de avaliação é completo mas não confuso?
- [ ] Sistema de notas 0-10 é adequado?
- [ ] Conceitos (A, B, C, D) estão claros?
- [ ] Campos de texto têm espaço suficiente?

---

## CENÁRIO 2: FLUXO COMPLETO DO ESTUDANTE

### 2.1 Autenticação e Dashboard

**Objetivo:** Verificar experiência inicial do estudante

**Passos:**
1. Faça logout (se estiver logado)
2. Faça login como estudante (aluno1)
3. Observe o dashboard

**O que avaliar:**
- [ ] Dashboard do estudante é diferente do professor?
- [ ] Informações relevantes estão visíveis (turmas, grupos, projetos)?
- [ ] É fácil navegar para funcionalidades importantes?

---

### 2.2 Entrar em Turma

**Objetivo:** Testar o processo de inscrição em turma

**Passos:**
1. Clique em "Entrar em Turma"
2. Digite o código de acesso da turma (obtido no Cenário 1.2)
3. Confirme a inscrição
4. Verifique se a turma aparece no dashboard

**O que avaliar:**
- [ ] Campo de código é claro?
- [ ] Processo é rápido e simples?
- [ ] Mensagem de confirmação é clara?
- [ ] Turma aparece imediatamente no dashboard?

**Pontos de atenção:**
- O que acontece se o código estiver errado?
- Estudante consegue sair da turma se entrou por engano?

---

### 2.3 Visualizar Atividades da Turma

**Objetivo:** Testar visualização de atividades postadas pelo professor

**Passos:**
1. Entre na turma que você se inscreveu
2. Clique em "Ver Atividades"
3. Observe as atividades criadas pelo professor
4. Clique em uma atividade para ver detalhes
5. Se houver arquivo anexo, tente baixá-lo

**O que avaliar:**
- [ ] Atividades estão organizadas de forma clara?
- [ ] Atividades fixadas aparecem em destaque?
- [ ] Tipos de atividade (tarefa, aviso, material) são visualmente distintos?
- [ ] Datas de entrega estão destacadas?
- [ ] É fácil ler o conteúdo completo da atividade?
- [ ] Download de arquivo funciona corretamente?

**Pontos de atenção:**
- Estudante consegue diferenciar atividades antigas de novas?
- Informações importantes (prazo, anexos) estão visíveis?
- Estudante consegue voltar facilmente para a lista?

---

### 2.4 Entrar em Grupo

**Objetivo:** Avaliar o processo de juntar-se a um grupo

**Passos:**
1. Volte aos detalhes da turma
2. Visualize os grupos disponíveis
3. Clique em "Entrar" em um grupo com vaga
4. Confirme sua entrada

**O que avaliar:**
- [ ] Lista de grupos está clara?
- [ ] É fácil ver quais grupos têm vaga?
- [ ] Informações dos membros são visíveis?
- [ ] Processo de entrada é simples?

**Pontos de atenção:**
- O que acontece se o grupo estiver cheio?
- É possível sair do grupo depois?

---

### 2.5 Criar Projeto

**Objetivo:** Testar criação de projeto científico

**Passos:**
1. Entre no grupo que você entrou
2. Clique em "Criar Projeto"
3. Preencha:
   - Título: "Qualidade da água no rio local"
   - Área: Ciências Ambientais
   - Descrição breve: "Investigação sobre poluição na bacia hidrográfica"
4. Salve o projeto

**O que avaliar:**
- [ ] Formulário é claro?
- [ ] Áreas de ciência disponíveis fazem sentido?
- [ ] Estudante entende que isso é só o início?

---

### 2.6 Preencher Fase 1 (Problema de Pesquisa)

**Objetivo:** Testar preenchimento da primeira fase

**Passos:**
1. No projeto criado, clique em "Editar Fase 1"
2. Preencha:
   - Pergunta de Pesquisa: "Qual é o nível de poluição da água do rio?"
   - Justificativa: "O rio abastece a cidade e há relatos de poluição..."
   - Objetivos: "Analisar qualidade da água e identificar fontes de poluição"
3. Salve a fase

**O que avaliar:**
- [ ] Campos da fase são claros e ajudam a estruturar o pensamento?
- [ ] Help texts/placeholders são úteis?
- [ ] É possível voltar e editar depois?
- [ ] Indicador de fase atual está visível?

---

### 2.7 Adicionar Observações (Fase 4)

**Objetivo:** Testar coleta de dados

**Passos:**
1. Avance até a Fase 4 (Coleta de Dados)
2. Clique em "Adicionar Observação"
3. Preencha:
   - Título: "Medição 1 - Ponto A"
   - Descrição: "Coletada amostra de água no ponto próximo à fábrica"
   - Data/hora da coleta: (agora)
   - (Opcional) Anexe uma foto
4. Adicione mais 1-2 observações

**O que avaliar:**
- [ ] Formulário de observação é apropriado para dados científicos?
- [ ] Upload de fotos funciona bem?
- [ ] Observações são listadas de forma clara?
- [ ] É fácil editar/excluir observações?

---

### 2.8 Visualizar Feedback do Professor

**Objetivo:** Testar comunicação professor-aluno

**Passos:**
1. Volte ao projeto
2. Verifique se há feedbacks do professor
3. Leia os comentários
4. Verifique status de aprovação de cada fase

**O que avaliar:**
- [ ] Feedbacks são fáceis de encontrar?
- [ ] É claro quais fases foram aprovadas?
- [ ] Estudante sabe o que fazer com o feedback?
- [ ] Progresso visual do projeto é compreensível?

---

## CENÁRIO 3: TESTES DE INTERFACE E NAVEGAÇÃO

### 3.1 Responsividade

**Objetivo:** Testar em diferentes dispositivos

**Passos:**
1. Acesse a plataforma em:
   - Desktop/laptop (tela grande)
   - Tablet (se disponível)
   - Smartphone (redimensione o navegador)
2. Navegue pelas principais páginas

**O que avaliar:**
- [ ] Layout se adapta bem a diferentes tamanhos?
- [ ] Menus e botões são clicáveis em telas pequenas?
- [ ] Textos são legíveis em mobile?
- [ ] Formulários são utilizáveis em mobile?

---

### 3.2 Navegação e Breadcrumbs

**Objetivo:** Avaliar facilidade de navegação

**Passos:**
1. Navegue de Dashboard → Turma → Grupo → Projeto → Fase
2. Use o breadcrumb (migalha de pão) para voltar
3. Use o menu superior para ir direto a outras seções

**O que avaliar:**
- [ ] Breadcrumbs estão sempre visíveis?
- [ ] É fácil voltar à página anterior?
- [ ] Menu é consistente em todas as páginas?
- [ ] Botões "Voltar" funcionam corretamente?

---

### 3.3 Mensagens de Feedback

**Objetivo:** Verificar clareza das mensagens do sistema

**Passos:**
1. Realize ações que geram mensagens:
   - Criar algo novo (sucesso)
   - Excluir algo (confirmação)
   - Tentar ação não permitida (erro)
   - Salvar formulário com campos vazios (validação)

**O que avaliar:**
- [ ] Mensagens são claras e específicas?
- [ ] Cores (verde/vermelho/amarelo) fazem sentido?
- [ ] Mensagens aparecem em local visível?
- [ ] É possível fechar mensagens?

---

## CENÁRIO 4: TESTES DE CASOS EXTREMOS

### 4.1 Grupos Cheios

**Objetivo:** Testar comportamento com limite de membros

**Passos:**
1. Como professor, crie um grupo pequeno (máx 2 membros)
2. Como estudante, tente entrar quando já houver 2 membros

**O que avaliar:**
- [ ] Sistema impede a entrada?
- [ ] Mensagem de erro é clara?
- [ ] Botão "Entrar" fica desabilitado ou invisível?

---

### 4.2 Tentativa de Avanço de Fase Sem Aprovação

**Objetivo:** Verificar controle de fluxo

**Passos:**
1. Como estudante, tente editar Fase 2 antes da Fase 1 ser aprovada

**O que avaliar:**
- [ ] Sistema impede a ação?
- [ ] Estudante entende por que não pode avançar?
- [ ] Mensagem indica o que precisa ser feito?

---

### 4.3 Código de Turma Inválido

**Objetivo:** Testar validação de entrada em turma

**Passos:**
1. Como estudante, tente entrar em turma com código "ABC123XYZ"

**O que avaliar:**
- [ ] Mensagem de erro é clara?
- [ ] Estudante sabe o que fazer?
- [ ] Campo permite tentativa novamente?

---

## QUESTIONÁRIO DE SATISFAÇÃO

Após completar os cenários, peça aos testadores para avaliarem:

### Facilidade de Uso (1-5, sendo 5 muito fácil)
- [ ] Quão fácil foi realizar as tarefas principais?
- [ ] Quão intuitiva é a interface?
- [ ] Quão clara é a organização das informações?

### Design e Aparência (1-5, sendo 5 excelente)
- [ ] Como você avalia o design visual?
- [ ] As cores e ícones são apropriados?
- [ ] O layout é atraente e moderno?

### Utilidade (1-5, sendo 5 muito útil)
- [ ] A plataforma atende às necessidades de um projeto científico?
- [ ] As 6 fases do método científico estão bem representadas?
- [ ] A comunicação professor-aluno é eficiente?

### Perguntas Abertas

1. **O que você mais gostou na plataforma?**
   
   _________________________________________

2. **O que foi mais difícil ou confuso?**
   
   _________________________________________

3. **O que você mudaria ou melhoraria?**
   
   _________________________________________

4. **Você usaria esta plataforma em um curso real?**
   
   _________________________________________

---

## REGISTRO DE PROBLEMAS ENCONTRADOS

### Problema 1
- **Descrição:**
- **Severidade:** (Crítico / Alto / Médio / Baixo)
- **Como Reproduzir:**
- **Screenshot:** (se aplicável)

### Problema 2
- **Descrição:**
- **Severidade:**
- **Como Reproduzir:**
- **Screenshot:**

### Problema 3
- **Descrição:**
- **Severidade:**
- **Como Reproduzir:**
- **Screenshot:**

(Continue listando conforme necessário)

---

## SUGESTÕES DE MELHORIA

### Melhoria 1
- **Área:** (Exemplo: Dashboard, Formulários, Navegação)
- **Descrição:**
- **Justificativa:**

### Melhoria 2
- **Área:**
- **Descrição:**
- **Justificativa:**

### Melhoria 3
- **Área:**
- **Descrição:**
- **Justificativa:**

(Continue listando conforme necessário)

---

## CONCLUSÃO DO TESTE

**Data do teste:** __________________

**Nome do testador:** __________________

**Perfil testado:** 
- [ ] Professor  
- [ ] Estudante

**Tempo total do teste:** __________________

**Avaliação geral (1-5):**
- [ ] 1 - Muito Insatisfatório
- [ ] 2 - Insatisfatório
- [ ] 3 - Neutro
- [ ] 4 - Satisfatório
- [ ] 5 - Muito Satisfatório

**Comentários finais:**

_______________________________________________

_______________________________________________

_______________________________________________

_______________________________________________

---

## CONTATO PARA REPORTAR PROBLEMAS

Se você encontrar bugs críticos ou tiver sugestões importantes:

**Email:** seu-email@exemplo.com

**Repositório GitHub:** https://github.com/YanPedro00/CIENCIA-CIDADA

**Issues:** https://github.com/YanPedro00/CIENCIA-CIDADA/issues

---

## AGRADECIMENTOS

Agradecemos pela sua participação nos testes de usabilidade!

Seu feedback é essencial para melhorar a plataforma e proporcionar uma melhor experiência educacional para professores e estudantes.

A Plataforma Ciência Cidadã foi desenvolvida para promover o aprendizado do método científico de forma prática e colaborativa.

---

**Data de criação deste documento:** Novembro 2024

**Versão:** 1.0
