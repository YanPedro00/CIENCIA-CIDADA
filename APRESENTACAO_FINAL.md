# CIÊNCIA CIDADÃ
## Sistema de Gerenciamento de Projetos Científicos Educacionais

**Equipe:** Yan Pedro, Eduardo Nunes, Erllison Reis  
**Data:** Dezembro de 2025  
**Versão:** 1.0.0  
**Status:** Produção

---

## 1. ACESSO À PLATAFORMA

### 1.1 Informações de Acesso

**URL de Produção:** https://ciencia-cidada.up.railway.app

**Infraestrutura:**
- Plataforma: Railway (PaaS)
- Banco de Dados: PostgreSQL
- Armazenamento de Mídia: Cloudinary
- Status: Online - Ambiente de Produção

### 1.2 Credenciais de Teste

**Professor:**
- Usuário: `professor`
- Senha: `senha123`
- Turma de Demonstração: Código `A1B2C3D4`

**Estudante:**
- Usuário: `estudante`
- Senha: `senha123`

---

## 2. VISÃO GERAL DO SISTEMA

### 2.1 Propósito

A plataforma Ciência Cidadã é um sistema web educacional desenvolvido para permitir que professores gerenciem turmas e estudantes desenvolvam projetos científicos completos seguindo o método científico estruturado em 6 fases sequenciais.

### 2.2 Público-Alvo

- **Professores:** Ensino fundamental, médio e superior
- **Estudantes:** Todas as idades interessadas em desenvolvimento científico
- **Instituições:** Escolas, universidades e centros de pesquisa

### 2.3 Diferenciais

- Sistema completo que integra ensino, pesquisa, coleta de dados e gamificação
- Interface intuitiva e responsiva
- Visualização de dados científicos com mapas e gráficos interativos
- Gestão automatizada de aprovações e feedbacks
- Armazenamento permanente em nuvem
- Exportação de relatórios em múltiplos formatos

---

## 3. ARQUITETURA TÉCNICA

### 3.1 Stack Tecnológico

| Camada | Tecnologia | Versão | Finalidade |
|--------|-----------|--------|------------|
| Backend | Django | 4.2.7 | Framework web Python MVC |
| Frontend | Bootstrap | 5.3 | Interface responsiva |
| Banco de Dados | PostgreSQL | 15+ | Banco relacional em produção |
| Autenticação | Django Auth | 4.2.7 | Sistema de login e permissões |
| Armazenamento | Cloudinary | - | CDN para imagens e documentos |
| Visualização | Chart.js | 4.4.1 | Gráficos interativos |
| Mapas | Leaflet | 1.9+ | Visualização geográfica |
| Análise de Dados | Plotly | 5.18+ | Gráficos científicos avançados |
| Deploy | Railway | - | CI/CD automatizado |

### 3.2 Arquitetura do Banco de Dados

**Total de Tabelas:** 12

**Entidades Principais:**
1. `Usuario` - Professores e estudantes (custom user model)
2. `Turma` - Classes e disciplinas
3. `Grupo` - Equipes de trabalho colaborativo
4. `Projeto` - Projetos científicos com 6 fases
5. `Observacao` - Dados coletados durante pesquisa
6. `Feedback` - Comentários e orientações do professor
7. `Avaliacao` - Avaliação final com notas e conceitos
8. `EstudanteTurma` - Inscrições e matrículas
9. `Atividade` - Tarefas e materiais didáticos
10. `Badge` - Conquistas de gamificação
11. `UsuarioBadge` - Badges conquistadas pelos usuários
12. `PontuacaoGrupo` - Sistema de ranking por pontos

**Relacionamentos:**
- 3 relacionamentos 1:1
- 12 relacionamentos 1:N
- 3 relacionamentos M:N

---

## 4. FUNCIONALIDADES IMPLEMENTADAS

### 4.1 Módulo do Professor

#### 4.1.1 Gerenciamento de Turmas

**Funcionalidades:**
- Criar turmas com código de acesso único (8 caracteres)
- Configurar limites de grupos por turma
- Definir tamanho mínimo e máximo de grupos
- Visualizar lista completa de estudantes inscritos
- Ativar ou desativar turmas

**Controles Disponíveis:**
- Edição de informações da turma
- Acompanhamento de estatísticas (total de grupos, estudantes, projetos)
- Navegação para lista de atividades

#### 4.1.2 Gerenciamento de Grupos

**Funcionalidades:**
- Visualizar todos os grupos da turma
- Aprovar formação de novos grupos
- Monitorar composição e membros
- Acompanhar projetos vinculados a cada grupo
- Verificar status de cada projeto (fase atual)

#### 4.1.3 Acompanhamento de Projetos

**Visão Geral:**
- Dashboard com todos os projetos da turma
- Filtros por fase (1 a 6)
- Gráficos de distribuição de projetos por fase
- Gráficos de áreas científicas mais populares
- Indicadores visuais de status (aguardando revisão, em andamento, concluído)

**Detalhamento:**
- Visualização completa de todas as 6 fases
- Histórico de feedbacks dados
- Acesso a todos os anexos e observações
- Timeline de aprovações

#### 4.1.4 Sistema de Feedbacks e Avaliações

**Feedbacks por Fase:**
- Comentar em cada fase individualmente
- Aprovar ou solicitar revisões
- Sistema de notificações para estudantes
- Registro de data e hora de cada feedback

**Avaliação Final:**
- Notas de 0 a 10 para cada uma das 6 fases
- Cálculo automático de média final
- Atribuição de conceitos (A, B, C, D)
- Campos estruturados:
  - Pontos fortes identificados
  - Pontos a melhorar
  - Comentários gerais
  - Recomendações

#### 4.1.5 Gestão de Atividades

**Criação de Atividades:**
- Título e descrição detalhada
- Anexo de materiais (PDF, DOCX, CSV, etc.)
- Definição de prazo de entrega
- Tipos: Informação, Tarefa, Material, Aviso
- Opção de fixar atividades importantes

**Gerenciamento:**
- Editar atividades existentes
- Excluir atividades
- Visualizar lista de atividades por turma
- Controle de visibilidade (ativas/inativas)

#### 4.1.6 Visualização de Dados e Relatórios

**Exportações Disponíveis:**
- PDF completo do projeto (todas as fases + avaliação)
- CSV de observações para análise externa
- Relatórios de progresso da turma

**Dashboards:**
- Estatísticas gerais da turma
- Gráfico de distribuição de projetos por fase
- Top 5 áreas científicas
- Ranking de grupos por pontuação

### 4.2 Módulo do Estudante

#### 4.2.1 Participação em Turmas

**Funcionalidades:**
- Entrar em turma via código de acesso (8 dígitos)
- Visualizar informações da turma
- Acessar atividades postadas pelo professor
- Download de materiais anexados
- Ver prazos e datas de entrega

#### 4.2.2 Formação de Grupos

**Criação de Grupo:**
- Líder cria o grupo com nome e descrição
- Sistema gera código de acesso único para o grupo
- Definição opcional de área de pesquisa

**Participação:**
- Entrar em grupo existente via código
- Visualizar membros do grupo
- Acompanhar pontuação acumulada
- Ver badges conquistadas pelo grupo

#### 4.2.3 Desenvolvimento de Projetos Científicos

O sistema estrutura projetos em 6 fases sequenciais baseadas no método científico:

**FASE 1: Problema de Pesquisa**

Campos obrigatórios:
- Pergunta científica clara e objetiva
- Justificativa da importância da pesquisa
- Objetivos gerais e específicos
- Contextualização do problema

Objetivo: Definir claramente o que será investigado.

**FASE 2: Hipótese**

Campos obrigatórios:
- Formulação da hipótese principal
- Fundamentação teórica
- Pesquisa bibliográfica prévia
- Expectativas de resultados

Objetivo: Propor explicação testável para o problema.

**FASE 3: Metodologia**

Campos obrigatórios:
- Método de coleta de dados
- Materiais e ferramentas necessários
- Cronograma de execução
- Local de realização da pesquisa
- Procedimentos detalhados

Objetivo: Planejar como a pesquisa será executada.

**FASE 4: Coleta de Dados**

Funcionalidades:
- Registrar múltiplas observações
- Cada observação contém:
  - Descrição detalhada
  - Data e hora
  - Até 3 fotos
  - Geolocalização (latitude/longitude) - opcional
  - Dados estruturados em formato JSON
  - Categoria da observação

Interface especial:
- Lista de todas as observações
- Edição e exclusão de observações
- Preview de fotos
- Indicador de quantidade de fotos por observação

Objetivo: Coletar e documentar dados da pesquisa.

**FASE 5: Análise de Dados**

Campos obrigatórios:
- Organização dos dados coletados
- Interpretação dos resultados
- Discussão científica
- Comparação com hipótese

Ferramentas disponíveis:
- Visualização das observações em mapa interativo (Leaflet)
- Gráficos de distribuição de dados (Plotly)
- Exportação de observações para CSV
- Estatísticas automáticas

Objetivo: Interpretar e discutir os dados coletados.

**FASE 6: Conclusão**

Campos obrigatórios:
- Resposta à pergunta inicial
- Confirmação ou refutação da hipótese
- Aprendizados obtidos
- Limitações do estudo
- Sugestões para pesquisas futuras

Objetivo: Sintetizar resultados e reflexões.

#### 4.2.4 Sistema de Anexos do Projeto

**Tipos de Anexos:**
- Relatório Final (PDF, DOCX)
- Apresentação (PPT, PDF)
- Foto da Equipe (JPG, PNG)
- Anexo Extra 1 (qualquer formato)
- Anexo Extra 2 (qualquer formato)
- Anexo Extra 3 (qualquer formato)

**Funcionalidades:**
- Upload múltiplo de arquivos
- Preview de imagens
- Links diretos para download
- Opção de deletar anexos individuais
- Armazenamento permanente no Cloudinary

#### 4.2.5 Sistema de Gamificação

**Badges Disponíveis (10 conquistas):**

1. **Primeira Observação** - Registrar primeira observação científica
2. **5 Observações** - Coletar 5 observações completas
3. **Explorador** - Adicionar geolocalização em observação
4. **Colaborador** - Tornar-se membro de um grupo
5. **Líder** - Criar e liderar um grupo
6. **Fase 1 Aprovada** - Ter problema de pesquisa aprovado
7. **Fase 3 Aprovada** - Ter metodologia aprovada
8. **Fase 6 Aprovada** - Ter conclusão aprovada
9. **Projeto Concluído** - Finalizar todas as 6 fases
10. **Primeira Foto** - Anexar primeira foto em observação

**Sistema de Pontuação:**
- Pontos acumulativos por grupo
- Ranking visível no dashboard
- Atribuição automática via Django Signals
- Notificações de conquistas

**Critérios de Pontuação:**
- Criar observação: +10 pontos
- Fase aprovada: +50 pontos
- Projeto concluído: +200 pontos
- Badge conquistada: +25 pontos

### 4.3 Dashboards e Visualizações

#### 4.3.1 Dashboard do Professor

**Métricas Exibidas:**
- Total de projetos na turma
- Projetos por fase (distribuição)
- Estudantes ativos
- Grupos formados
- Taxa de conclusão

**Gráficos Interativos:**
- Pizza: Distribuição de projetos por fase
- Barras: Top 5 áreas científicas mais pesquisadas
- Timeline: Aprovações recentes

#### 4.3.2 Dashboard do Estudante

**Informações Pessoais:**
- Badges conquistadas (com ícones)
- Pontuação do grupo
- Fase atual do projeto
- Próximas atividades

**Acesso Rápido:**
- Link para projeto do grupo
- Atividades pendentes
- Feedbacks recebidos

#### 4.3.3 Visualização de Dados Científicos

**Mapa Interativo (Leaflet):**
- Plotagem de todas as observações com geolocalização
- Marcadores clicáveis com informações
- Zoom e navegação
- Clustering para múltiplas observações próximas

**Gráficos (Plotly):**
- Distribuição temporal de observações
- Análise por categoria
- Gráficos personalizáveis
- Exportação de imagens

---

## 5. CASOS DE USO

### 5.1 Caso de Uso 1: Professor Cria Turma e Atividade

**Objetivo:** Professor cria uma nova turma e posta uma atividade

**Pré-condições:**
- Usuário autenticado como professor
- Credenciais: `professor` / `senha123`

**Fluxo Principal:**

1. Fazer login como professor
2. No dashboard, clicar em "Criar Nova Turma"
3. Preencher formulário:
   - Nome: "Biologia 2025"
   - Descrição: "Turma de projetos de biologia"
   - Máximo de grupos: 10
   - Mínimo de membros por grupo: 3
   - Máximo de membros por grupo: 5
4. Submeter formulário
5. Sistema gera código de acesso único (ex: `X7Y2K9M4`)
6. Anotar código para compartilhar com estudantes
7. Clicar em "Atividades" da turma criada
8. Clicar em "Criar Nova Atividade"
9. Preencher:
   - Título: "Leitura sobre Método Científico"
   - Descrição: "Ler material anexo até próxima aula"
   - Tipo: "Material"
   - Data de entrega: [data futura]
   - Anexar PDF (opcional)
   - Marcar como fixada: Sim
10. Submeter
11. Atividade aparece na lista para todos os estudantes da turma

**Resultado Esperado:**
- Turma criada com sucesso
- Código de acesso gerado
- Atividade visível para estudantes
- Professor pode gerenciar turma e atividades

### 5.2 Caso de Uso 2: Estudante Entra em Turma e Cria Grupo

**Objetivo:** Estudante se inscreve em turma e forma grupo de pesquisa

**Pré-condições:**
- Usuário autenticado como estudante
- Credenciais: `estudante` / `senha123`
- Código de turma disponível: `A1B2C3D4`

**Fluxo Principal:**

1. Fazer login como estudante
2. No menu, clicar em "Turmas"
3. Clicar em "Entrar em Turma"
4. Inserir código: `A1B2C3D4`
5. Clicar em "Entrar"
6. Sistema confirma inscrição
7. Turma aparece em "Minhas Turmas"
8. Acessar a turma
9. Clicar em "Criar Grupo"
10. Preencher formulário:
    - Nome do grupo: "Exploradores da Natureza"
    - Descrição: "Grupo focado em ecologia urbana"
    - Área de pesquisa: "Biologia"
11. Submeter
12. Sistema gera código do grupo (ex: `ABC123`)
13. Compartilhar código com colegas para entrarem no grupo

**Resultado Esperado:**
- Estudante inscrito na turma
- Grupo criado com sucesso
- Estudante é líder do grupo
- Código do grupo disponível para convites
- Badge "Líder" conquistada automaticamente

### 5.3 Caso de Uso 3: Desenvolvimento Completo de Projeto

**Objetivo:** Grupo desenvolve projeto científico completo através das 6 fases

**Pré-condições:**
- Grupo formado e aprovado
- Credenciais: `estudante` / `senha123`
- Grupo tem no mínimo 3 membros

**Fluxo Principal:**

**FASE 1: Problema de Pesquisa**

1. Login como estudante
2. Acessar "Meu Grupo"
3. Clicar em "Criar Novo Projeto"
4. Preencher Fase 1:
   - Título: "Qualidade da Água do Lago do Parque"
   - Pergunta: "A água do lago apresenta níveis seguros de pH e oxigênio dissolvido?"
   - Justificativa: "O lago é usado por animais e próximo a área residencial"
   - Objetivos: "Medir pH, temperatura e oxigênio dissolvido durante 2 semanas"
   - Área científica: "Ecologia"
5. Submeter
6. Aguardar revisão do professor
7. Professor analisa, dá feedback e aprova

**FASE 2: Hipótese**

8. Após aprovação da Fase 1, sistema libera Fase 2
9. Preencher:
   - Hipótese: "A água possui pH entre 6.5 e 8.5 e oxigênio acima de 5mg/L"
   - Fundamentação: "Segundo literatura, águas saudáveis apresentam estes valores"
   - Expectativas: "Valores dentro do esperado, com variações por temperatura"
10. Submeter
11. Aguardar aprovação do professor

**FASE 3: Metodologia**

12. Após aprovação da Fase 2, preencher Fase 3:
    - Método: "Coleta de amostras 2x por dia durante 14 dias"
    - Materiais: "Kit de teste de pH, termômetro, oxímetro"
    - Local: "Lago do Parque Municipal, coordenadas: -15.7801, -47.9292"
    - Cronograma: "Coletas às 8h e 18h, segunda a domingo"
13. Submeter
14. Aguardar aprovação do professor

**FASE 4: Coleta de Dados**

15. Após aprovação da Fase 3, ir para "Observações"
16. Para cada coleta, clicar em "Adicionar Observação":
    
    **Observação 1:**
    - Data: 01/12/2025 08:00
    - Descrição: "Primeira coleta. Dia ensolarado, sem chuvas recentes"
    - Dados estruturados (JSON):
      ```json
      {
        "ph": 7.2,
        "temperatura_agua": 24,
        "oxigenio_dissolvido": 6.8,
        "temperatura_ar": 26,
        "condicoes_clima": "ensolarado"
      }
      ```
    - Categoria: "Medição Matinal"
    - Latitude: -15.7801
    - Longitude: -47.9292
    - Anexar 2 fotos (lago + equipamento)

    **Observação 2:**
    - Data: 01/12/2025 18:00
    - Descrição: "Segunda coleta do dia. Temperatura mais alta"
    - Dados estruturados (JSON):
      ```json
      {
        "ph": 7.4,
        "temperatura_agua": 26,
        "oxigenio_dissolvido": 5.9,
        "temperatura_ar": 30,
        "condicoes_clima": "ensolarado"
      }
      ```
    - Categoria: "Medição Vespertina"
    - Latitude: -15.7801
    - Longitude: -47.9292
    - Anexar 1 foto

17. Repetir para todas as 28 coletas (14 dias x 2 coletas)
18. Sistema atribui badges automaticamente:
    - "Primeira Observação"
    - "5 Observações"
    - "Explorador" (por usar geolocalização)
    - "Primeira Foto"
19. Após completar coletas, submeter Fase 4

**FASE 5: Análise de Dados**

20. Após submissão da Fase 4, preencher Fase 5:
    - Organização: "28 amostras coletadas, dados tabulados em planilha"
    - Interpretação: "pH médio de 7.3 (dentro do esperado). Oxigênio médio de 6.2mg/L (saudável). Temperatura varia entre 22°C e 27°C"
    - Discussão: "Valores confirmam que a água está em condições adequadas. Variação de oxigênio é maior no período vespertino devido à temperatura"
21. Clicar em "Visualizar Dados"
22. Verificar mapa com todos os pontos de coleta
23. Analisar gráficos gerados automaticamente
24. Exportar observações para CSV se necessário
25. Submeter Fase 5

**FASE 6: Conclusão**

26. Após aprovação da Fase 5, preencher Fase 6:
    - Resposta: "Sim, a água do lago apresenta níveis seguros de pH e oxigênio dissolvido"
    - Confirmação de hipótese: "Hipótese confirmada. Valores dentro dos padrões esperados"
    - Aprendizados: "Importância do horário de coleta. Temperatura afeta oxigênio dissolvido"
    - Limitações: "Apenas 2 semanas de coleta. Não testamos outros parâmetros como coliformes"
    - Sugestões: "Estender para 1 mês. Incluir testes microbiológicos"
27. Submeter Fase 6
28. Ir para "Anexos do Projeto"
29. Fazer upload dos documentos:
    - Relatório Final (PDF): relatório completo com gráficos
    - Apresentação (PDF): slides para apresentação
    - Foto da Equipe (JPG): foto dos 3 membros
    - Anexo Extra 1 (CSV): planilha com todos os dados brutos
30. Professor avalia todas as fases
31. Professor preenche avaliação final:
    - Fase 1: 9.5
    - Fase 2: 9.0
    - Fase 3: 10.0
    - Fase 4: 9.5
    - Fase 5: 9.0
    - Fase 6: 9.5
    - Média: 9.4
    - Conceito: A
    - Pontos fortes: "Coleta sistemática, análise cuidadosa"
    - Pontos a melhorar: "Ampliar discussão teórica"
32. Sistema atribui badge "Projeto Concluído"
33. Grupo recebe +200 pontos

**Resultado Esperado:**
- Projeto completo com 6 fases desenvolvidas
- 28 observações registradas com fotos e geolocalização
- Todas as badges de fases conquistadas
- Anexos enviados com sucesso
- Avaliação final recebida com conceito A
- Grupo no topo do ranking

### 5.4 Caso de Uso 4: Professor Visualiza e Exporta Dados

**Objetivo:** Professor acompanha projeto, dá feedbacks e exporta relatórios

**Pré-condições:**
- Projeto em andamento ou concluído
- Credenciais: `professor` / `senha123`

**Fluxo Principal:**

1. Login como professor
2. Acessar "Minhas Turmas"
3. Selecionar turma "Biologia 2025"
4. Visualizar dashboard com estatísticas
5. Analisar gráfico de distribuição por fases
6. Clicar em projeto específico "Qualidade da Água do Lago"
7. Revisar todas as 6 fases
8. Verificar as 28 observações coletadas
9. Dar feedback na Fase 1:
   - "Excelente problematização. Pergunta clara e objetivos bem definidos."
   - Aprovar fase
10. Dar feedback na Fase 2:
    - "Hipótese bem fundamentada. Sugiro adicionar referências bibliográficas."
    - Aprovar fase
11. Continuar para outras fases
12. Clicar em "Visualizar Dados Científicos"
13. Analisar mapa com pontos de coleta
14. Verificar gráficos de distribuição
15. Clicar em "Exportar Projeto em PDF"
16. Sistema gera PDF com:
    - Capa com título e grupo
    - Todas as 6 fases
    - Lista de observações
    - Feedbacks dados
    - Avaliação final
17. Download automático do PDF
18. Clicar em "Exportar Observações (CSV)"
19. Sistema gera CSV com:
    - Data/hora de cada observação
    - Descrição
    - Dados estruturados
    - Coordenadas geográficas
    - Links para fotos
20. Download automático do CSV
21. Preencher avaliação final (notas 0-10 para cada fase)
22. Sistema calcula média automaticamente
23. Atribuir conceito (A, B, C, D)
24. Escrever pontos fortes e pontos a melhorar
25. Submeter avaliação
26. Estudantes são notificados

**Resultado Esperado:**
- Todos os feedbacks registrados
- Relatórios exportados com sucesso
- Avaliação final completa
- Dados disponíveis para análise externa (CSV)

### 5.5 Caso de Uso 5: Estudante Acessa Atividades e Materiais

**Objetivo:** Estudante visualiza atividades e baixa materiais

**Pré-condições:**
- Estudante inscrito em turma
- Professor postou atividades
- Credenciais: `estudante` / `senha123`

**Fluxo Principal:**

1. Login como estudante
2. Acessar "Minhas Turmas"
3. Selecionar turma inscrita
4. Clicar em "Atividades"
5. Visualizar lista de atividades:
   - Atividades fixadas aparecem no topo (com marcador)
   - Atividades normais abaixo
   - Ordenadas por data de entrega
6. Clicar em atividade "Leitura sobre Método Científico"
7. Visualizar detalhes:
   - Título e descrição completa
   - Tipo de atividade (Material)
   - Data de entrega
   - Professor autor
   - Data de publicação
8. Se houver arquivo anexado, clicar em "Download"
9. Arquivo PDF baixado com sucesso
10. Ler material
11. Voltar para lista de atividades
12. Verificar próximas atividades e prazos

**Resultado Esperado:**
- Todas as atividades visíveis
- Materiais baixados com sucesso
- Estudante informado sobre prazos

---

## 6. CASOS DE TESTE

### 6.1 Teste 1: Autenticação e Permissões

**Objetivo:** Validar sistema de autenticação e controle de acesso

**Dados de Teste:**
- Usuário Professor: `professor` / `senha123`
- Usuário Estudante: `estudante` / `senha123`

**Procedimento:**

1. **Teste de Login Válido:**
   - Acessar página de login
   - Inserir credenciais de professor
   - Clicar em "Entrar"
   - **Resultado Esperado:** Redirecionamento para dashboard do professor
   - **Status:** PASS/FAIL

2. **Teste de Login Inválido:**
   - Acessar página de login
   - Inserir usuário: `teste` / senha: `errada`
   - Clicar em "Entrar"
   - **Resultado Esperado:** Mensagem de erro "Credenciais inválidas"
   - **Status:** PASS/FAIL

3. **Teste de Permissões de Professor:**
   - Login como professor
   - Tentar acessar `/turmas/criar/`
   - **Resultado Esperado:** Página de criação de turma exibida
   - **Status:** PASS/FAIL

4. **Teste de Restrição de Estudante:**
   - Login como estudante
   - Tentar acessar diretamente `/turmas/criar/`
   - **Resultado Esperado:** Redirecionamento ou mensagem de "Acesso negado"
   - **Status:** PASS/FAIL

5. **Teste de Logout:**
   - Clicar em "Sair" no menu
   - Tentar acessar página protegida
   - **Resultado Esperado:** Redirecionamento para login
   - **Status:** PASS/FAIL

### 6.2 Teste 2: Criação e Gestão de Turmas

**Objetivo:** Validar funcionalidades de turma

**Dados de Teste:**
- Professor: `professor` / `senha123`

**Procedimento:**

1. **Criar Nova Turma:**
   - Login como professor
   - Acessar "Criar Nova Turma"
   - Preencher:
     - Nome: "Teste Turma QA"
     - Descrição: "Turma para testes"
     - Máximo de grupos: 5
     - Mínimo de membros: 2
     - Máximo de membros: 4
   - Submeter
   - **Resultado Esperado:** 
     - Turma criada com sucesso
     - Código de 8 caracteres gerado
     - Turma aparece em "Minhas Turmas"
   - **Status:** PASS/FAIL

2. **Validação de Código Único:**
   - Criar segunda turma
   - Verificar que código é diferente
   - **Resultado Esperado:** Cada turma tem código único
   - **Status:** PASS/FAIL

3. **Editar Turma:**
   - Acessar turma criada
   - Clicar em "Editar"
   - Alterar descrição
   - Salvar
   - **Resultado Esperado:** Alterações salvas e exibidas
   - **Status:** PASS/FAIL

4. **Desativar Turma:**
   - Editar turma
   - Marcar como "Inativa"
   - Salvar
   - **Resultado Esperado:** Turma não aceita novas inscrições
   - **Status:** PASS/FAIL

### 6.3 Teste 3: Fluxo Completo de Projeto

**Objetivo:** Validar desenvolvimento de projeto do início ao fim

**Dados de Teste:**
- Estudante: `estudante` / `senha123`
- Turma: `A1B2C3D4`

**Procedimento:**

1. **Inscrição em Turma:**
   - Login como estudante
   - Entrar em turma com código `A1B2C3D4`
   - **Resultado Esperado:** Inscrição confirmada
   - **Status:** PASS/FAIL

2. **Criação de Grupo:**
   - Criar grupo "Grupo Teste QA"
   - Verificar geração de código
   - **Resultado Esperado:** Grupo criado e código gerado
   - **Status:** PASS/FAIL

3. **Aguardar Aprovação (Manual):**
   - Professor deve aprovar o grupo
   - Verificar status do grupo
   - **Resultado Esperado:** Grupo aprovado aparece como "Ativo"
   - **Status:** PASS/FAIL

4. **Criar Projeto - Fase 1:**
   - Criar novo projeto
   - Preencher todos os campos obrigatórios da Fase 1
   - Submeter
   - **Resultado Esperado:** Fase 1 salva e aguardando revisão
   - **Status:** PASS/FAIL

5. **Validação de Bloqueio Sequencial:**
   - Tentar acessar Fase 2 antes de aprovação da Fase 1
   - **Resultado Esperado:** Fase 2 bloqueada/desabilitada
   - **Status:** PASS/FAIL

6. **Aprovação pelo Professor (Manual):**
   - Professor dá feedback e aprova Fase 1
   - **Resultado Esperado:** Notificação de aprovação
   - **Status:** PASS/FAIL

7. **Acesso à Fase 2:**
   - Após aprovação, acessar Fase 2
   - **Resultado Esperado:** Fase 2 desbloqueada para edição
   - **Status:** PASS/FAIL

8. **Repetir para Fases 2-6:**
   - Preencher cada fase
   - Aguardar aprovação
   - Avançar para próxima
   - **Resultado Esperado:** Todas as fases completadas sequencialmente
   - **Status:** PASS/FAIL

9. **Adicionar Observações:**
   - Na Fase 4, adicionar 5 observações
   - Incluir fotos em 3 delas
   - Incluir geolocalização em 2 delas
   - **Resultado Esperado:** Observações salvas com todos os dados
   - **Status:** PASS/FAIL

10. **Verificar Badges:**
    - Conferir badges conquistadas:
      - Primeira Observação
      - 5 Observações
      - Explorador
      - Primeira Foto
      - Colaborador
      - Fases aprovadas
    - **Resultado Esperado:** Badges atribuídas automaticamente
    - **Status:** PASS/FAIL

11. **Upload de Anexos:**
    - Acessar "Anexos do Projeto"
    - Fazer upload de:
      - Relatório Final (PDF)
      - Apresentação (PDF)
      - Foto da Equipe (JPG)
      - Anexo Extra (CSV)
    - **Resultado Esperado:** Todos os arquivos salvos no Cloudinary
    - **Status:** PASS/FAIL

12. **Verificar Links de Download:**
    - Clicar em cada anexo
    - **Resultado Esperado:** Arquivos abrem/baixam corretamente
    - **Status:** PASS/FAIL

13. **Avaliação Final:**
    - Professor preenche avaliação
    - Verificar cálculo de média
    - Verificar conceito atribuído
    - **Resultado Esperado:** Avaliação visível para estudante
    - **Status:** PASS/FAIL

### 6.4 Teste 4: Sistema de Gamificação

**Objetivo:** Validar atribuição automática de badges e pontos

**Dados de Teste:**
- Estudante: `estudante` / `senha123`

**Procedimento:**

1. **Badge "Primeira Observação":**
   - Criar primeira observação em projeto
   - Verificar badge no perfil
   - **Resultado Esperado:** Badge atribuída imediatamente
   - **Status:** PASS/FAIL

2. **Badge "5 Observações":**
   - Criar 5 observações
   - Verificar badge
   - **Resultado Esperado:** Badge atribuída após 5ª observação
   - **Status:** PASS/FAIL

3. **Badge "Explorador":**
   - Criar observação com latitude e longitude
   - Verificar badge
   - **Resultado Esperado:** Badge atribuída ao adicionar geolocalização
   - **Status:** PASS/FAIL

4. **Badge "Primeira Foto":**
   - Anexar foto em observação
   - Verificar badge
   - **Resultado Esperado:** Badge atribuída ao upload da foto
   - **Status:** PASS/FAIL

5. **Badge "Colaborador":**
   - Entrar em um grupo
   - Verificar badge
   - **Resultado Esperado:** Badge atribuída ao entrar no grupo
   - **Status:** PASS/FAIL

6. **Badge "Líder":**
   - Criar um grupo
   - Verificar badge
   - **Resultado Esperado:** Badge atribuída ao criar grupo
   - **Status:** PASS/FAIL

7. **Badges de Fases:**
   - Ter Fase 1 aprovada
   - Ter Fase 3 aprovada
   - Ter Fase 6 aprovada
   - Verificar 3 badges correspondentes
   - **Resultado Esperado:** Badge atribuída após cada aprovação
   - **Status:** PASS/FAIL

8. **Badge "Projeto Concluído":**
   - Completar todas as 6 fases
   - Verificar badge
   - **Resultado Esperado:** Badge atribuída ao finalizar projeto
   - **Status:** PASS/FAIL

9. **Pontuação do Grupo:**
   - Verificar pontos após cada ação:
     - Criar observação: +10
     - Fase aprovada: +50
     - Projeto concluído: +200
   - **Resultado Esperado:** Pontos somados corretamente
   - **Status:** PASS/FAIL

10. **Ranking:**
    - Verificar posição do grupo no ranking
    - **Resultado Esperado:** Grupos ordenados por pontuação
    - **Status:** PASS/FAIL

### 6.5 Teste 5: Upload e Download de Arquivos

**Objetivo:** Validar armazenamento no Cloudinary

**Dados de Teste:**
- Estudante: `estudante` / `senha123`
- Professor: `professor` / `senha123`

**Procedimento:**

1. **Upload de PDF (Estudante):**
   - Acessar "Anexos do Projeto"
   - Fazer upload de relatório PDF
   - **Resultado Esperado:** 
     - Upload bem-sucedido
     - URL com `/raw/upload/` para PDFs
   - **Status:** PASS/FAIL

2. **Upload de Imagem (Estudante):**
   - Fazer upload de foto da equipe (JPG)
   - **Resultado Esperado:**
     - Upload bem-sucedido
     - URL com `/image/upload/` para imagens
   - **Status:** PASS/FAIL

3. **Upload de CSV (Estudante):**
   - Fazer upload de dados em CSV
   - **Resultado Esperado:**
     - Upload bem-sucedido
     - URL com `/raw/upload/` para CSV
   - **Status:** PASS/FAIL

4. **Download de PDF:**
   - Clicar no link do PDF
   - **Resultado Esperado:** PDF abre no navegador ou baixa
   - **Status:** PASS/FAIL

5. **Preview de Imagem:**
   - Verificar thumbnail da foto
   - Clicar para ampliar
   - **Resultado Esperado:** Imagem exibida corretamente
   - **Status:** PASS/FAIL

6. **Deletar Anexo:**
   - Clicar no botão de deletar anexo
   - Confirmar exclusão
   - **Resultado Esperado:**
     - Anexo removido da lista
     - Link não funciona mais
   - **Status:** PASS/FAIL

7. **Substituir Arquivo:**
   - Deletar anexo antigo
   - Fazer novo upload no mesmo campo
   - **Resultado Esperado:** Novo arquivo substituiu o antigo
   - **Status:** PASS/FAIL

8. **Upload de Material (Professor):**
   - Login como professor
   - Criar atividade
   - Anexar PDF
   - **Resultado Esperado:** PDF disponível para download pelos estudantes
   - **Status:** PASS/FAIL

9. **Múltiplas Fotos em Observação:**
   - Criar observação
   - Anexar 3 fotos
   - **Resultado Esperado:** 3 fotos visíveis com thumbnails
   - **Status:** PASS/FAIL

10. **Persistência Após Deploy:**
    - Verificar que arquivos antigos continuam acessíveis após redeploy
    - **Resultado Esperado:** URLs permanentes funcionando
    - **Status:** PASS/FAIL

### 6.6 Teste 6: Exportação de Relatórios

**Objetivo:** Validar geração de PDF e CSV

**Dados de Teste:**
- Professor: `professor` / `senha123`
- Projeto com dados completos

**Procedimento:**

1. **Exportar Projeto em PDF:**
   - Login como professor
   - Acessar projeto completo
   - Clicar em "Exportar em PDF"
   - **Resultado Esperado:**
     - PDF gerado com todas as 6 fases
     - Feedbacks incluídos
     - Formatação legível
     - Download automático
   - **Status:** PASS/FAIL

2. **Verificar Conteúdo do PDF:**
   - Abrir PDF baixado
   - Confirmar presença de:
     - Capa com título e grupo
     - Todas as fases
     - Lista de observações
     - Avaliação final (se disponível)
   - **Resultado Esperado:** Todos os elementos presentes
   - **Status:** PASS/FAIL

3. **Exportar Observações em CSV:**
   - Clicar em "Exportar Observações (CSV)"
   - **Resultado Esperado:**
     - CSV gerado
     - Download automático
   - **Status:** PASS/FAIL

4. **Verificar Estrutura do CSV:**
   - Abrir CSV em Excel/Google Sheets
   - Confirmar colunas:
     - ID
     - Data/Hora
     - Descrição
     - Dados estruturados
     - Categoria
     - Latitude/Longitude
     - URLs das fotos
   - **Resultado Esperado:** Estrutura correta e dados íntegros
   - **Status:** PASS/FAIL

5. **CSV com Caracteres Especiais:**
   - Criar observação com acentuação
   - Exportar CSV
   - Verificar encoding (UTF-8)
   - **Resultado Esperado:** Acentos preservados
   - **Status:** PASS/FAIL

### 6.7 Teste 7: Dashboards e Visualizações

**Objetivo:** Validar gráficos e mapas interativos

**Dados de Teste:**
- Professor: `professor` / `senha123`
- Turma com múltiplos projetos em diferentes fases

**Procedimento:**

1. **Dashboard do Professor:**
   - Login como professor
   - Acessar dashboard
   - Verificar métricas:
     - Total de projetos
     - Distribuição por fase
     - Top 5 áreas científicas
   - **Resultado Esperado:** Dados corretos e atualizados
   - **Status:** PASS/FAIL

2. **Gráfico de Pizza (Fases):**
   - Verificar gráfico de distribuição
   - Passar mouse sobre fatias
   - **Resultado Esperado:**
     - Gráfico renderizado (Chart.js)
     - Tooltips funcionando
     - Cores distintas
   - **Status:** PASS/FAIL

3. **Gráfico de Barras (Áreas Científicas):**
   - Verificar gráfico de áreas
   - **Resultado Esperado:**
     - Top 5 áreas listadas
     - Contagem correta
   - **Status:** PASS/FAIL

4. **Mapa de Observações:**
   - Acessar "Visualizar Dados" de um projeto
   - Verificar mapa Leaflet
   - Verificar marcadores de observações
   - **Resultado Esperado:**
     - Mapa carregado
     - Marcadores nos locais corretos
     - Popup com informações ao clicar
   - **Status:** PASS/FAIL

5. **Gráficos Plotly:**
   - Verificar gráficos de análise de dados
   - Testar interatividade (zoom, pan)
   - **Resultado Esperado:**
     - Gráficos renderizados
     - Interações funcionando
   - **Status:** PASS/FAIL

6. **Responsividade:**
   - Testar dashboards em diferentes resoluções
   - Testar em dispositivo móvel
   - **Resultado Esperado:**
     - Layout adapta corretamente
     - Gráficos redimensionam
   - **Status:** PASS/FAIL

### 6.8 Teste 8: Gestão de Atividades

**Objetivo:** Validar sistema de atividades

**Dados de Teste:**
- Professor: `professor` / `senha123`
- Estudante: `estudante` / `senha123`
- Turma: `A1B2C3D4`

**Procedimento:**

1. **Criar Atividade (Professor):**
   - Login como professor
   - Acessar turma
   - Criar nova atividade:
     - Título: "Atividade Teste"
     - Descrição: "Descrição detalhada"
     - Tipo: "Tarefa"
     - Data de entrega: [futura]
     - Fixada: Sim
     - Anexar PDF
   - Submeter
   - **Resultado Esperado:** Atividade criada com sucesso
   - **Status:** PASS/FAIL

2. **Visualizar Lista de Atividades (Professor):**
   - Acessar "Atividades" da turma
   - Verificar atividades fixadas no topo
   - **Resultado Esperado:** Ordem correta (fixadas primeiro)
   - **Status:** PASS/FAIL

3. **Editar Atividade:**
   - Clicar em "Editar"
   - Alterar descrição
   - Salvar
   - **Resultado Esperado:** Alterações salvas
   - **Status:** PASS/FAIL

4. **Visualizar Atividade (Estudante):**
   - Login como estudante
   - Acessar turma
   - Clicar em "Atividades"
   - Verificar atividade criada
   - **Resultado Esperado:** Atividade visível com todos os detalhes
   - **Status:** PASS/FAIL

5. **Download de Material (Estudante):**
   - Clicar no anexo da atividade
   - **Resultado Esperado:** Arquivo baixado corretamente
   - **Status:** PASS/FAIL

6. **Excluir Atividade (Professor):**
   - Acessar atividade
   - Clicar em "Excluir"
   - Confirmar
   - **Resultado Esperado:**
     - Atividade removida
     - Não aparece mais para estudantes
   - **Status:** PASS/FAIL

7. **Atividade Inativa:**
   - Editar atividade
   - Marcar como "Inativa"
   - Verificar visibilidade
   - **Resultado Esperado:** Atividade não aparece para estudantes
   - **Status:** PASS/FAIL

---

## 7. IMPACTO E RESULTADOS

### 7.1 Impacto Social

**Democratização da Ciência:**
- Torna o método científico acessível a estudantes de todas as idades
- Remove barreiras tecnológicas com interface intuitiva
- Permite pesquisas de baixo custo

**Engajamento Educacional:**
- Gamificação aumenta motivação dos estudantes
- Trabalho em grupo desenvolve habilidades colaborativas
- Feedback estruturado melhora aprendizado

**Documentação de Pesquisas:**
- Preserva projetos desenvolvidos ao longo do tempo
- Cria portfólio científico para estudantes
- Facilita compartilhamento de resultados

### 7.2 Impacto Técnico

**Escalabilidade:**
- Arquitetura preparada para milhares de usuários
- Armazenamento em nuvem (Cloudinary)
- Deploy automatizado (Railway)

**Manutenibilidade:**
- Código bem estruturado seguindo padrões Django
- Documentação completa e atualizada
- Versionamento com Git

**Segurança:**
- Autenticação robusta com Django Auth
- Controle de permissões granular
- Validação de dados em múltiplas camadas

**Performance:**
- Queries otimizadas com ORM Django
- CDN para entrega rápida de mídia
- Cache de assets estáticos

---

## 8. ARQUITETURA E DESENVOLVIMENTO

### 8.1 Metodologia de Desenvolvimento

**Ferramentas e Processos:**
- Controle de Versão: Git/GitHub
- IDE: VS Code / Cursor
- Deploy Contínuo: Railway (CI/CD automático)
- Banco de Dados: PostgreSQL (produção) / SQLite (desenvolvimento)
- Armazenamento: Cloudinary

**Processo de Desenvolvimento:**
1. Levantamento de requisitos e análise de necessidades
2. Modelagem do banco de dados (Diagrama ER)
3. Desenvolvimento incremental (7 entregas progressivas)
4. Testes de funcionalidade após cada entrega
5. Deploy em produção
6. Documentação técnica e de usuário

### 8.2 Principais Desafios e Soluções

**Desafio 1: Armazenamento Efêmero**

*Problema:* Railway utiliza sistema de arquivos efêmero (arquivos são perdidos após deploy).

*Solução:*
- Integração com Cloudinary para armazenamento permanente
- Criação de `DocumentStorage` customizado para PDFs/CSVs
- `MediaCloudinaryStorage` para imagens
- URLs permanentes via CDN

**Desafio 2: Migrações de Banco de Dados**

*Problema:* Migrações não eram aplicadas automaticamente no Railway.

*Solução:*
- Script `start.sh` executa `makemigrations` e `migrate` antes de iniciar servidor
- Migrations versionadas no repositório Git
- Processo de build separado do processo de start

**Desafio 3: Complexidade do Método Científico**

*Problema:* 6 fases sequenciais com sistema de aprovação é complexo.

*Solução:*
- Sistema de estados no model `Projeto`
- Métodos `pode_avancar_fase()` e `avancar_fase()`
- Feedbacks do professor vinculados a cada fase
- Interface com indicadores visuais de progresso

**Desafio 4: Gamificação Automática**

*Problema:* Atribuir badges manualmente seria trabalhoso e sujeito a erros.

*Solução:*
- Django Signals com decorador `@receiver`
- Detecção automática de eventos (criar observação, aprovar fase)
- Atribuição instantânea de badges
- Sistema de pontuação acumulativa por grupo

**Desafio 5: Visualização de Dados Científicos**

*Problema:* Dados brutos em tabela são difíceis de interpretar.

*Solução:*
- Mapas interativos com Leaflet.js para geolocalização
- Gráficos com Plotly para análises visuais
- Exportação para CSV para análises externas
- Dashboard com estatísticas visuais (Chart.js)

**Desafio 6: Permissões Diferenciadas**

*Problema:* Professores e estudantes têm acessos diferentes.

*Solução:*
- Custom user model com campo `is_professor`
- Decoradores `@login_required` e `@user_passes_test`
- Validações em views e templates
- Testes unitários de permissões

### 8.3 Lições Aprendidas

**Técnicas:**
- Django ORM facilita significativamente operações de banco de dados
- PostgreSQL é essencial para ambientes de produção
- Cloudinary resolve problemas de armazenamento efêmero
- Migrations devem ser versionadas e testadas rigorosamente
- Signals automatizam processos complexos de forma eficiente

**Gestão de Projeto:**
- Documentação desde o início facilita manutenção
- Entregas incrementais reduzem riscos
- Feedback de usuários reais revela problemas não previstos
- CI/CD economiza tempo e reduz erros humanos
- Git é fundamental para trabalho em equipe

**Design e UX:**
- Modelagem do banco de dados primeiro evita refatorações custosas
- Separação clara de permissões desde o início
- Gamificação aumenta engajamento real dos usuários
- Bootstrap acelera desenvolvimento de UI
- Responsividade é obrigatória em 2025

---

## 9. DOCUMENTAÇÃO TÉCNICA

### 9.1 Repositório e Código-Fonte

**Repositório GitHub:**
https://github.com/YanPedro00/CIENCIA-CIDADA

**Estrutura do Projeto:**
```
ciencia-cidada/
├── core/                    # App principal Django
│   ├── models.py           # 12 modelos do sistema
│   ├── views.py            # Lógica de negócio
│   ├── forms.py            # Formulários
│   ├── admin.py            # Interface administrativa
│   ├── signals.py          # Gamificação automática
│   ├── storage.py          # Cloudinary storage customizado
│   ├── templates/          # Templates HTML
│   └── migrations/         # Migrations do banco
├── config/                  # Configurações Django
│   ├── settings.py         # Settings de produção/dev
│   ├── urls.py             # URLs principais
│   └── wsgi.py             # WSGI para deploy
├── staticfiles/            # Arquivos estáticos coletados
├── requirements.txt        # Dependências Python
├── build.sh                # Script de build (Railway)
├── start.sh                # Script de start (Railway)
└── manage.py               # Django management
```

### 9.2 Documentação Disponível

**Para Usuários:**
- `USUARIOS_TESTE.md` - Credenciais e dados de teste
- `GUIA_TESTES_USABILIDADE.md` - Manual de testes

**Para Desenvolvedores:**
- `DIAGRAMA_BANCO_DADOS.md` - Diagrama ER completo
- `VARIAVEIS_AMBIENTE.md` - Configuração de ambiente
- `RAILWAY_CLOUDINARY_SETUP.md` - Setup de deploy
- `ARMAZENAMENTO_MIDIA.md` - Explicação sobre arquivos

**Para Gestão:**
- `ENTREGA5_COMPLETA.md` - Detalhamento de funcionalidades
- `RELATORIO_ENTREGA5.txt` - Relatório executivo
- `APRESENTACAO_FINAL.md` - Este documento

### 9.3 Tecnologias e Referências

**Framework e Linguagens:**
- Django 4.2.7: https://www.djangoproject.com
- Python 3.10+: https://www.python.org
- Bootstrap 5.3: https://getbootstrap.com

**Bibliotecas Python:**
- psycopg2: Adaptador PostgreSQL
- Pillow: Processamento de imagens
- reportlab: Geração de PDF
- openpyxl/pandas: Exportação CSV/Excel
- plotly: Gráficos científicos
- django-cloudinary-storage: Integração Cloudinary

**Bibliotecas JavaScript:**
- Chart.js 4.4.1: https://www.chartjs.org
- Leaflet.js: https://leafletjs.com
- Plotly.js: https://plotly.com/javascript

**Infraestrutura:**
- Railway: https://railway.app
- Cloudinary: https://cloudinary.com
- PostgreSQL: https://www.postgresql.org

---

## 10. MÉTRICAS E CONQUISTAS

### 10.1 Métricas do Projeto

**Desenvolvimento:**
- Linhas de Código: ~8.000 (5.000 Python + 3.000 HTML/CSS/JS)
- Commits: 50+ commits versionados
- Tempo de Desenvolvimento: 4 meses
- Entregas: 7 entregas progressivas

**Banco de Dados:**
- Tabelas: 12 tabelas relacionadas
- Relacionamentos: 18 relacionamentos (1:1, 1:N, M:N)
- Migrations: 4+ migrations aplicadas

**Funcionalidades:**
- Funcionalidades Implementadas: 30+ features
- Badges de Gamificação: 10 conquistas
- Tipos de Usuário: 2 (professor e estudante)
- Fases de Projeto: 6 fases sequenciais

**Documentação:**
- Arquivos de Documentação: 10+ arquivos Markdown
- Linhas de Documentação: 4.000+ linhas
- Casos de Uso: 5 casos detalhados
- Casos de Teste: 8 suítes completas

### 10.2 Resultados Alcançados

- Plataforma 100% funcional em produção
- Todos os requisitos implementados
- Documentação completa técnica e de usuário
- Deploy automatizado com CI/CD
- Código aberto disponível no GitHub
- Testes de funcionalidade realizados
- Interface responsiva e acessível

### 10.3 Diferenciais Técnicos

- Arquitetura escalável para milhares de usuários
- Armazenamento permanente em nuvem
- Sistema de gamificação automático
- Visualização científica avançada (mapas e gráficos)
- Exportação em múltiplos formatos (PDF, CSV)
- Controle granular de permissões
- Interface moderna e intuitiva

---

## 11. LINKS E RECURSOS

### 11.1 Acesso à Plataforma

**URL de Produção:**  
https://ciencia-cidada.up.railway.app

**Credenciais de Demonstração:**
- Professor: `professor` / `senha123`
- Estudante: `estudante` / `senha123`
- Código de Turma: `A1B2C3D4`

### 11.2 Repositório e Código

**GitHub:**  
https://github.com/YanPedro00/CIENCIA-CIDADA

### 11.3 Infraestrutura

**Plataforma de Deploy:**  
Railway - https://railway.app

**Banco de Dados:**  
PostgreSQL (gerenciado pelo Railway)

**CDN e Armazenamento:**  
Cloudinary - https://cloudinary.com

### 11.4 Documentação Técnica

**Django Documentation:**  
https://docs.djangoproject.com/en/4.2/

**PostgreSQL Documentation:**  
https://www.postgresql.org/docs/

**Cloudinary Django Integration:**  
https://cloudinary.com/documentation/django_integration

**Bootstrap Documentation:**  
https://getbootstrap.com/docs/5.3/

---

## 12. CONTATO E SUPORTE

### 12.1 Equipe de Desenvolvimento

**Yan Pedro**  
**Eduardo Nunes**  
**Erllison Reis**

### 12.2 Reportar Problemas

Para reportar bugs ou sugerir melhorias:
- Abrir issue no repositório GitHub
- Contatar via seção "Sobre" na plataforma

### 12.3 Contribuições

Contribuições são bem-vindas:
1. Fork do repositório
2. Criar branch para feature (`git checkout -b feature/nova-feature`)
3. Commit das mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para o branch (`git push origin feature/nova-feature`)
5. Abrir Pull Request

---

## 13. CONCLUSÃO

A plataforma Ciência Cidadã representa um avanço significativo na democratização do acesso ao método científico no contexto educacional brasileiro. Através da integração de tecnologias modernas e design centrado no usuário, desenvolvemos uma ferramenta completa que:

1. **Empodera professores** com ferramentas eficientes para gerenciar turmas, acompanhar projetos e fornecer feedbacks estruturados

2. **Engaja estudantes** através de gamificação, autonomia no desenvolvimento de projetos e visualização clara de progresso

3. **Facilita a pesquisa** com ferramentas integradas de coleta, análise e visualização de dados científicos

4. **Escala facilmente** para atender centenas de turmas e milhares de usuários simultaneamente

5. **Documenta conhecimento** preservando projetos e criando portfólio científico para estudantes

O projeto vai além de atender requisitos técnicos: cria impacto social real ao preparar uma nova geração de cientistas cidadãos, tornando a ciência mais acessível, engajadora e relevante para a educação brasileira.

---

**Status:** Produção - 100% Funcional  
**Última Atualização:** Dezembro 2025  
**Versão:** 1.0.0  
**Licença:** Open Source

---

**Equipe:** Yan Pedro, Eduardo Nunes, Erllison Reis  
**Data de Entrega:** Dezembro 2025

