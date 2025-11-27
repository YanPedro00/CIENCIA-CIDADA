# ANÁLISE COMPLETA DO SISTEMA - ENTREGA 5

**Data:** 27 de Novembro de 2025  
**Projeto:** Plataforma de Ciência Cidadã Educacional

---

## 1. RESUMO EXECUTIVO

### 1.1 Status Atual do Sistema

**Sistema Implementado:** Plataforma web Django completa para gerenciamento de projetos científicos educacionais.

**Funcionalidades Core (100% Implementadas):**
- Sistema de autenticação com 2 tipos de usuário (Professor/Estudante)
- Gerenciamento de turmas com código de acesso
- Criação e gerenciamento de grupos
- Desenvolvimento de projetos científicos em 6 fases do método científico
- Sistema de aprovação de fases pelo professor
- Feedback do professor para cada fase
- Coleta de dados (observações) com fotos
- Avaliação final com nota conceitual
- Sistema de atividades/avisos por turma
- Deploy em Railway com PostgreSQL

**Tecnologias Utilizadas:**
- Backend: Django 4.2.7
- Frontend: Bootstrap 5
- Banco de Dados: PostgreSQL (produção), SQLite (desenvolvimento)
- Deploy: Railway + Gunicorn + WhiteNoise
- Autenticação: Django Auth
- Upload de arquivos: Django FileField/ImageField

---

## 2. ANÁLISE DOS REQUISITOS DA ENTREGA 5

### Requisito 1: Integrar banco de dados, autenticação e envio de dados para órgãos públicos

#### 1.1 Banco de Dados
**STATUS:** ✅ COMPLETO

**Implementado:**
- PostgreSQL em produção (Railway)
- SQLite para desenvolvimento local
- Migrations completas
- 9 modelos principais: Usuario, Turma, Grupo, Projeto, Observacao, Feedback, Avaliacao, EstudanteTurma, Atividade
- Relacionamentos complexos (ManyToMany, ForeignKey, OneToOne)

**Qualidade:** Excelente. Estrutura bem normalizada e escalável.

#### 1.2 Autenticação
**STATUS:** ✅ COMPLETO

**Implementado:**
- Sistema de registro de usuários
- Login/Logout
- Permissões por tipo de usuário (Professor/Estudante)
- Proteção de rotas com @login_required
- User model customizado (AbstractUser)
- CSRF Protection
- Session management

**Qualidade:** Excelente. Segue as melhores práticas do Django.

#### 1.3 Envio de Dados para Órgãos Públicos
**STATUS:** ❌ NÃO IMPLEMENTADO

**Análise:**
- Não existe integração com APIs de órgãos públicos
- Não há exportação de dados em formatos oficiais
- Não há relatórios para submissão externa

**VIABILIDADE DE IMPLEMENTAÇÃO:**
⚠️ **MÉDIA** - Depende de:
1. Identificar quais órgãos públicos receberiam os dados
2. Verificar se esses órgãos possuem APIs abertas
3. Definir formato de dados requerido (JSON, XML, CSV)
4. Questões de privacidade/LGPD com dados de estudantes

**Tempo Estimado:** 2-3 semanas (se APIs existirem)

**Recomendação:** NÃO PRIORITÁRIO para um projeto educacional. Se necessário, implementar exportação CSV/PDF primeiro.

---

### Requisito 2: Implementar dashboards e relatórios para APAN e comunidades

#### 2.1 APAN
**STATUS:** ❌ NÃO APLICÁVEL

**Decisão do usuário:** Ignorar tópicos relacionados à APAN.

#### 2.2 Dashboards para Comunidades
**STATUS:** ⚠️ PARCIALMENTE IMPLEMENTADO

**Implementado:**
- Dashboard do Professor (visão geral de turmas e projetos pendentes)
- Dashboard do Estudante (turmas, grupos e projetos)
- Páginas de detalhes de projetos com progresso visual

**Faltando:**
- Relatórios exportáveis (PDF, Excel)
- Gráficos estatísticos (Chart.js, Plotly)
- Dashboard público com projetos concluídos
- Métricas consolidadas por turma/semestre

**VIABILIDADE DE IMPLEMENTAÇÃO:**
✅ **ALTA** - Tecnicamente simples de implementar.

**Funcionalidades Sugeridas:**

1. **Dashboard Público (Home)**
   - Estatísticas gerais (total de projetos, estudantes, áreas de ciência)
   - Mapa de calor de áreas científicas mais pesquisadas
   - Linha do tempo de projetos concluídos
   - Galeria de projetos destaque

2. **Dashboard do Professor - Melhorado**
   - Gráfico de progresso dos grupos
   - Taxa de aprovação por fase
   - Tempo médio para conclusão de projetos
   - Distribuição de notas conceituais
   - Exportar relatório de turma em PDF

3. **Dashboard do Estudante - Melhorado**
   - Gráfico de progresso do próprio grupo
   - Comparação com média da turma
   - Histórico de feedbacks
   - Certificado digital ao concluir projeto

4. **Relatórios Exportáveis**
   - PDF: Relatório completo do projeto (todas as 6 fases)
   - CSV: Dados de observações para análise em Excel
   - PDF: Certificado de conclusão do projeto
   - PDF: Boletim da turma (para o professor)

**Tempo Estimado:** 1-2 semanas

**Bibliotecas Necessárias:**
- `reportlab` ou `weasyprint` (geração de PDF)
- `openpyxl` ou `pandas` (exportação Excel)
- `Chart.js` ou `Plotly` (gráficos interativos)

**Recomendação:** ✅ IMPLEMENTAR - Alta prioridade e grande valor agregado.

---

### Requisito 3: Sincronizar módulos de planejamento e testes para turmas avançadas

**STATUS:** ⚠️ INTERPRETAÇÃO NECESSÁRIA

**Análise:**
O sistema atual não possui "módulos de planejamento" e "testes" como entidades separadas. No entanto:

**O que já existe:**
- Sistema de 6 fases do método científico (é um "módulo de planejamento")
- Aprovação sequencial de fases (garante sincronização)
- Avaliação final conceitual (A, B, C, D)

**Possíveis interpretações do requisito:**

**Interpretação 1: Módulos de Conteúdo/Currículo**
- Criar módulos teóricos (aulas, vídeos, materiais)
- Associar módulos às fases do projeto
- Estudantes devem completar módulos antes de cada fase
- **Viabilidade:** ✅ ALTA (estrutura semelhante ao modelo Atividade)
- **Tempo:** 1 semana

**Interpretação 2: Sistema de Quiz/Provas**
- Criar questões de múltipla escolha/dissertativas
- Provas para avaliar conhecimento teórico
- Nota mínima para liberar fases do projeto
- **Viabilidade:** ✅ ALTA
- **Tempo:** 2 semanas

**Interpretação 3: Turmas Avançadas com Recursos Extras**
- Definir níveis de turma (Básico, Intermediário, Avançado)
- Turmas avançadas têm requisitos extras (ex: revisão bibliográfica na Fase 2)
- Campos adicionais por nível
- **Viabilidade:** ✅ MÉDIA
- **Tempo:** 1 semana

**RECOMENDAÇÃO:**
Implementar **Interpretação 1 + 2** (Módulos de Conteúdo + Quiz):

1. **Módulo de Conteúdo**
   - Cada fase do projeto pode ter módulos teóricos associados
   - Módulos contêm: título, descrição, vídeos (links), arquivos PDF
   - Professor marca módulo como obrigatório ou opcional
   - Estudante marca módulo como "concluído"

2. **Sistema de Quiz**
   - Professor cria quiz com questões (múltipla escolha)
   - Quiz pode ser associado a uma fase
   - Estudante deve atingir nota mínima (ex: 70%) para avançar
   - Respostas armazenadas no banco
   - Gabarito automático

**Tempo Total:** 3 semanas

---

### Requisito 4: Criar e aplicar dinâmicas para ensino de computação em escolas públicas

**STATUS:** ❌ NÃO IMPLEMENTADO

**Análise:**
Este requisito parece estar fora do escopo do projeto atual (Ciência Cidadã). O sistema é focado em projetos científicos, não especificamente em ensino de computação.

**Possíveis Interpretações:**

**Interpretação 1: Gamificação**
- Sistema de pontos/badges para estudantes
- Conquistas ao completar fases
- Ranking de grupos mais ativos
- **Viabilidade:** ✅ ALTA
- **Tempo:** 1 semana

**Interpretação 2: Projetos de Computação como Área**
- Permitir área "Ciência da Computação" nos projetos
- Templates de projeto específicos para computação
- Exemplos de projetos: "App para coleta de dados", "Site de visualização"
- **Viabilidade:** ✅ ALTA (apenas configuração)
- **Tempo:** 2 dias

**Interpretação 3: Ferramentas de Programação Integradas**
- Editor de código no navegador (Monaco Editor)
- Estudantes escrevem scripts para análise de dados (Python)
- Execução de código em sandbox
- **Viabilidade:** ⚠️ BAIXA (complexo e segurança)
- **Tempo:** 4+ semanas

**RECOMENDAÇÃO:**
Implementar **Interpretação 1 + 2** (Gamificação + Projetos de Computação):

1. **Gamificação**
   ```python
   # Novo modelo
   class Badge(models.Model):
       nome = models.CharField(max_length=100)
       descricao = models.TextField()
       icone = models.ImageField()
       criterio = models.CharField()  # 'primeira_observacao', 'projeto_concluido', etc.
   
   class UsuarioBadge(models.Model):
       usuario = models.ForeignKey(Usuario)
       badge = models.ForeignKey(Badge)
       conquistado_em = models.DateTimeField(auto_now_add=True)
   ```

2. **Templates de Projeto por Área**
   - Adicionar campo `template_projeto` em Turma
   - Professor escolhe: "Projeto Livre", "Projeto de Computação", "Projeto Ambiental"
   - Sistema sugere campos/fases relevantes

**Tempo Total:** 1 semana

---

### Requisito 5: Realizar oficina de ferramentas de IA com foco em uso responsável e criativo

**STATUS:** ❌ NÃO IMPLEMENTADO

**Análise:**
Não há integração com ferramentas de IA no sistema atual.

**Possíveis Implementações:**

**Opção 1: Assistente IA para Projetos (Integração com ChatGPT/Claude)**
- Botão "Ajuda IA" em cada fase
- IA sugere melhorias na pergunta de pesquisa
- IA ajuda a formular hipóteses baseadas em literatura
- IA sugere métodos de análise de dados
- **Viabilidade:** ✅ ALTA (via API OpenAI/Anthropic)
- **Custo:** API paga (ou usar modelos locais)
- **Tempo:** 2 semanas

**Opção 2: Módulo Educacional sobre IA**
- Adicionar conteúdo teórico sobre IA
- Casos de uso responsável de IA na ciência
- Ética em IA (viés, privacidade, transparência)
- Exercícios práticos (ex: usar ChatGPT para brainstorm)
- **Viabilidade:** ✅ ALTA
- **Tempo:** 3 dias (criação de conteúdo)

**Opção 3: Ferramenta de Análise de Dados com IA**
- Upload de CSV com observações
- IA gera gráficos automaticamente
- IA identifica padrões e correlações
- IA sugere conclusões (Fase 6)
- **Viabilidade:** ⚠️ MÉDIA (requer processamento de dados)
- **Tempo:** 3 semanas

**RECOMENDAÇÃO:**
Implementar **Opção 1 (Assistente IA)** - Maior impacto educacional:

**Funcionalidades:**
1. **Assistente de Pergunta de Pesquisa (Fase 1)**
   - IA analisa pergunta e dá sugestões: "Seja mais específico", "Isso é mensurável?", "Considere reduzir o escopo"

2. **Assistente de Hipótese (Fase 2)**
   - IA busca literatura relacionada (via PubMed API, Semantic Scholar)
   - IA sugere hipóteses baseadas em estudos similares

3. **Assistente de Metodologia (Fase 3)**
   - IA sugere métodos de coleta baseados na área de ciência
   - IA alerta sobre vieses e limitações

4. **Assistente de Análise (Fase 5)**
   - IA analisa observações (se em formato estruturado)
   - IA gera estatísticas descritivas
   - IA sugere testes estatísticos apropriados

5. **Revisão de Texto**
   - IA corrige gramática e clareza
   - IA sugere melhorias na escrita científica

**Ética e Responsabilidade:**
- Aviso claro: "Esta é uma sugestão de IA. Use senso crítico."
- Watermark em textos revisados por IA
- Professor pode ver quando IA foi usada
- Limite de uso (ex: 10 consultas IA por projeto)

**Tecnologia:**
- API OpenAI (GPT-4o-mini) ou Anthropic (Claude 3.5 Sonnet)
- Custo: ~$0.01 por consulta
- Alternativa gratuita: Modelos locais (Ollama + Llama)

**Tempo:** 2 semanas

**Custo Estimado:** $50-100/mês (para 100 estudantes ativos)

---

### Requisito 6: Testar com atletas da APAN e ajustar conforme desempenho

**STATUS:** ❌ NÃO APLICÁVEL

**Decisão do usuário:** Ignorar tópicos relacionados à APAN.

---

## 3. FUNCIONALIDADES JÁ IMPLEMENTADAS (CHECKLIST)

### 3.1 Autenticação e Usuários
- [x] Registro de usuário (Professor/Estudante)
- [x] Login/Logout
- [x] Perfil customizado (foto, instituição, telefone)
- [x] Permissões por tipo de usuário
- [x] Proteção CSRF

### 3.2 Turmas
- [x] Professor cria turma
- [x] Código de acesso único
- [x] Estudante entra com código
- [x] Configuração de máximo de grupos
- [x] Configuração de máximo de membros por grupo
- [x] Listagem de estudantes da turma
- [x] Edição de turma

### 3.3 Grupos
- [x] Criação de grupo (professor ou estudante)
- [x] Seleção de membros
- [x] Definição de líder
- [x] Estudante entra em grupo
- [x] Validação de limite de membros
- [x] Um grupo = um projeto

### 3.4 Projetos (6 Fases do Método Científico)
- [x] Criação de projeto por grupo
- [x] Fase 1: Problema de Pesquisa (pergunta, justificativa, objetivos)
- [x] Fase 2: Hipótese (hipótese principal, fundamentação teórica)
- [x] Fase 3: Metodologia (método, materiais, cronograma, local)
- [x] Fase 4: Coleta de Dados (observações com fotos)
- [x] Fase 5: Análise de Dados (organização, interpretação, discussão)
- [x] Fase 6: Conclusão (hipótese confirmada?, conclusão, aprendizados, limitações)
- [x] Progresso visual (% de fases aprovadas)
- [x] Sistema de slug único
- [x] 11 áreas de ciência disponíveis

### 3.5 Observações (Coleta de Dados)
- [x] Adicionar observação com título e descrição
- [x] Upload de até 3 fotos
- [x] Localização (latitude, longitude, descrição do local)
- [x] Data e hora da coleta
- [x] Dados estruturados (JSON)
- [x] Edição de observação
- [x] Exclusão de observação

### 3.6 Feedback e Aprovação
- [x] Professor dá feedback em cada fase
- [x] Feedback com comentário e status de aprovação
- [x] Aprovação de fase pelo professor
- [x] Avanço automático para próxima fase após aprovação
- [x] Histórico de feedbacks visível para estudantes

### 3.7 Avaliação Final
- [x] Avaliação conceitual (A, B, C, D)
- [x] Notas por fase (0-10)
- [x] Comentários gerais
- [x] Pontos fortes
- [x] Pontos a melhorar
- [x] Cálculo de média automática

### 3.8 Atividades/Avisos
- [x] Professor cria atividade para turma
- [x] 4 tipos: Informação, Tarefa, Material de Apoio, Aviso
- [x] Fixar atividade no topo
- [x] Data de entrega (opcional)
- [x] Anexo de arquivo
- [x] Estudantes visualizam (apenas ativas)
- [x] Professor edita/exclui

### 3.9 Interface
- [x] Templates Bootstrap 5
- [x] Responsivo (mobile-friendly)
- [x] Dashboard diferenciado por tipo de usuário
- [x] Mensagens de feedback (sucesso, erro, aviso)
- [x] Breadcrumbs de navegação
- [x] Formulários com validação

### 3.10 Deploy e Infraestrutura
- [x] Deploy no Railway
- [x] PostgreSQL em produção
- [x] SQLite em desenvolvimento
- [x] Gunicorn como servidor WSGI
- [x] WhiteNoise para arquivos estáticos
- [x] Variáveis de ambiente (.env)
- [x] Migrations automatizadas
- [x] Script de criação de dados iniciais

### 3.11 Segurança
- [x] CSRF Protection
- [x] SQL Injection protection (ORM)
- [x] Validação de uploads
- [x] Permissões por rota
- [x] HTTPS (Railway)

---

## 4. FUNCIONALIDADES FALTANTES/MELHORIAS PRIORITÁRIAS

### 4.1 PRIORIDADE ALTA (Implementar Primeiro)

#### A) Dashboards e Relatórios Melhorados
**Impacto:** 🔥🔥🔥 MUITO ALTO  
**Dificuldade:** ⭐⭐ MÉDIA  
**Tempo:** 1-2 semanas

**Funcionalidades:**
1. Dashboard público com estatísticas
2. Gráficos de progresso (Chart.js)
3. Exportação de relatórios em PDF (projeto completo)
4. Exportação de observações em CSV
5. Certificado de conclusão em PDF

**Bibliotecas:**
```txt
reportlab==4.0.7          # Geração de PDF
openpyxl==3.1.2           # Exportação Excel
pandas==2.1.4             # Manipulação de dados
matplotlib==3.8.2         # Gráficos estáticos
```

#### B) Gamificação Básica
**Impacto:** 🔥🔥 ALTO  
**Dificuldade:** ⭐ FÁCIL  
**Tempo:** 3-5 dias

**Funcionalidades:**
1. Sistema de badges/conquistas
2. Pontos por ação (criar observação, concluir fase)
3. Ranking de grupos por turma
4. Página de perfil com badges conquistadas

**Modelos Novos:**
- `Badge` (conquista)
- `UsuarioBadge` (relação)
- `PontuacaoGrupo` (ranking)

#### C) Visualização de Dados das Observações
**Impacto:** 🔥🔥🔥 MUITO ALTO  
**Dificuldade:** ⭐⭐ MÉDIA  
**Tempo:** 1 semana

**Funcionalidades:**
1. Gráficos automáticos de observações (se dados estruturados)
2. Mapa com pins de localização das observações
3. Linha do tempo das coletas
4. Galeria de fotos do projeto

**Bibliotecas:**
```txt
plotly==5.18.0           # Gráficos interativos
folium==0.15.1           # Mapas
```

---

### 4.2 PRIORIDADE MÉDIA (Implementar Depois)

#### D) Assistente IA (se orçamento permitir)
**Impacto:** 🔥🔥🔥 MUITO ALTO  
**Dificuldade:** ⭐⭐⭐ ALTA  
**Tempo:** 2 semanas  
**Custo:** $50-100/mês

**Funcionalidades:**
1. Ajuda na formulação de perguntas de pesquisa
2. Sugestões de hipóteses baseadas em literatura
3. Revisão de texto científico
4. Análise automática de dados

**API:**
- OpenAI GPT-4o-mini ou Anthropic Claude 3.5 Haiku (mais barato)

#### E) Sistema de Quiz/Avaliações
**Impacto:** 🔥🔥 ALTO  
**Dificuldade:** ⭐⭐⭐ ALTA  
**Tempo:** 2 semanas

**Funcionalidades:**
1. Professor cria questões (múltipla escolha, V/F, dissertativa)
2. Quiz associado a fases do projeto
3. Nota mínima para liberar próxima fase
4. Correção automática
5. Feedback imediato

#### F) Módulos de Conteúdo
**Impacto:** 🔥🔥 ALTO  
**Dificuldade:** ⭐⭐ MÉDIA  
**Tempo:** 1 semana

**Funcionalidades:**
1. Professor cria módulos teóricos por fase
2. Módulo contém: vídeos (embeds), PDFs, links
3. Estudante marca como "concluído"
4. Professor vê progresso dos estudantes nos módulos

---

### 4.3 PRIORIDADE BAIXA (Opcional/Futuro)

#### G) API REST para Integração Externa
**Impacto:** 🔥 BAIXO (para uso atual)  
**Dificuldade:** ⭐⭐ MÉDIA  
**Tempo:** 1 semana

**Funcionalidades:**
- Django REST Framework
- Endpoints: `/api/projetos/`, `/api/observacoes/`
- Autenticação via token
- Exportação JSON para outros sistemas

#### H) App Mobile (Flutter/React Native)
**Impacto:** 🔥🔥 ALTO (experiência do usuário)  
**Dificuldade:** ⭐⭐⭐⭐ MUITO ALTA  
**Tempo:** 2+ meses

**Funcionalidades:**
- App para coleta de observações no campo
- Foto com geolocalização automática
- Sincronização offline
- Push notifications

---

## 5. ROADMAP PROPOSTO

### SPRINT 1 (Semana 1-2): Dashboards e Relatórios
**Objetivo:** Melhorar visualização e exportação de dados

**Tarefas:**
1. Instalar bibliotecas (reportlab, openpyxl, plotly)
2. Criar view de dashboard público com estatísticas
3. Adicionar gráficos de progresso no dashboard do professor
4. Implementar exportação de projeto em PDF
5. Implementar exportação de observações em CSV
6. Criar certificado de conclusão em PDF
7. Testes e ajustes

**Entregáveis:**
- Dashboard público interativo
- Botão "Exportar Relatório" na página do projeto
- Botão "Baixar Certificado" para projetos concluídos
- Gráficos de pizza (distribuição de áreas de ciência)
- Gráficos de barras (progresso dos grupos)

---

### SPRINT 2 (Semana 3): Visualização de Dados e Mapas
**Objetivo:** Melhorar visualização de observações

**Tarefas:**
1. Instalar plotly e folium
2. Criar página de visualização de dados do projeto
3. Gráficos automáticos (se dados_json tiver estrutura)
4. Mapa com pins das observações (latitude/longitude)
5. Linha do tempo das coletas
6. Galeria de fotos em grid
7. Testes

**Entregáveis:**
- Página "Visualizar Dados" no menu do projeto
- Mapa interativo com observações
- Gráficos de análise de dados

---

### SPRINT 3 (Semana 4): Gamificação
**Objetivo:** Aumentar engajamento dos estudantes

**Tarefas:**
1. Criar modelos Badge, UsuarioBadge, PontuacaoGrupo
2. Definir badges (Primeira Observação, Explorador, Projeto Concluído, etc.)
3. Sistema de pontos (criar observação = 10 pts, concluir fase = 50 pts)
4. Página de perfil com badges
5. Ranking de grupos por turma
6. Notificações de conquistas
7. Testes

**Entregáveis:**
- 10 badges implementadas
- Sistema de pontos funcionando
- Página de ranking
- Notificação ao conquistar badge

---

### SPRINT 4 (Semana 5-6): Módulos de Conteúdo
**Objetivo:** Adicionar conteúdo teórico às fases

**Tarefas:**
1. Criar modelo ModuloConteudo
2. Professor cria módulos por fase
3. Módulos contêm: título, descrição, vídeo (embed YouTube), arquivos
4. Estudante marca módulo como concluído
5. Dashboard de progresso nos módulos
6. Módulos obrigatórios vs opcionais
7. Testes

**Entregáveis:**
- CRUD de módulos para professor
- Visualização de módulos para estudante
- Checkbox "Concluído"
- Progresso no dashboard

---

### SPRINT 5 (Semana 7-8): Sistema de Quiz (Opcional)
**Objetivo:** Avaliações de conhecimento

**Tarefas:**
1. Criar modelos Quiz, Questao, Resposta, RespostaEstudante
2. Professor cria quiz com questões
3. Tipos: múltipla escolha, verdadeiro/falso
4. Estudante responde quiz
5. Correção automática
6. Nota mínima para liberar fase
7. Feedback imediato
8. Testes

**Entregáveis:**
- CRUD de quiz para professor
- Interface de resposta para estudante
- Sistema de correção automática
- Bloqueio de fase se nota insuficiente

---

### SPRINT 6 (Semana 9-10): Assistente IA (Opcional - se orçamento)
**Objetivo:** Ajuda inteligente nos projetos

**Tarefas:**
1. Criar conta OpenAI/Anthropic
2. Integrar API
3. Criar view "Ajuda IA" por fase
4. Prompts específicos por fase
5. Sistema de créditos/limite de uso
6. Watermark em textos revisados por IA
7. Dashboard para professor ver uso de IA
8. Avisos de ética e responsabilidade
9. Testes

**Entregáveis:**
- Botão "Ajuda IA" em cada fase
- Sugestões contextualizadas
- Limite de 10 consultas por projeto
- Aviso de uso responsável

---

## 6. REQUISITOS TÉCNICOS PARA NOVAS FUNCIONALIDADES

### 6.1 Bibliotecas Python Adicionais

```txt
# Relatórios e Exportação
reportlab==4.0.7
openpyxl==3.1.2
pandas==2.1.4
matplotlib==3.8.2

# Visualização de Dados
plotly==5.18.0
folium==0.15.1

# IA (Opcional)
openai==1.6.1
anthropic==0.7.8

# API REST (Opcional)
djangorestframework==3.14.0
djangorestframework-simplejwt==5.3.1

# Celery para tarefas assíncronas (se necessário)
celery==5.3.4
redis==5.0.1
```

### 6.2 Bibliotecas JavaScript (CDN)

```html
<!-- Gráficos -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>

<!-- Mapas -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<!-- Animações -->
<link href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>
```

---

## 7. ESTIMATIVA DE CUSTOS

### 7.1 Hospedagem (Atual)
- **Railway:** $5-20/mês (depende do uso)
- **Domínio .me (GitHub Education):** Grátis por 1 ano

### 7.2 APIs de IA (se implementar)
- **OpenAI GPT-4o-mini:** $0.150/1M tokens input, $0.600/1M tokens output
  - Estimativa: 100 consultas/dia × 500 tokens = 1.5M tokens/mês = ~$1.50/mês
- **Anthropic Claude 3.5 Haiku:** $0.25/MTok input, $1.25/MTok output
  - Estimativa similar: ~$2/mês

### 7.3 Armazenamento de Mídia (se volume aumentar)
- **Cloudinary (free tier):** 25 GB grátis
- **AWS S3:** ~$0.023/GB

### 7.4 Total Estimado
- **Sem IA:** $5-20/mês (apenas hosting)
- **Com IA:** $10-30/mês

---

## 8. RECOMENDAÇÕES FINAIS

### 8.1 Para a Entrega 5

**O que já está pronto:**
✅ Banco de dados integrado (PostgreSQL)  
✅ Sistema de autenticação completo  
✅ Dashboards básicos para professor e estudante  

**O que RECOMENDO implementar para a Entrega 5:**

1. **Dashboards e Relatórios Melhorados** (ESSENCIAL)
   - Adiciona grande valor sem alterar estrutura
   - Professores podem gerar relatórios das turmas
   - Estudantes têm visão clara do progresso

2. **Visualização de Dados das Observações** (ESSENCIAL)
   - Mapa com pins
   - Gráficos automáticos
   - Enriquece a Fase 5 (Análise de Dados)

3. **Gamificação Básica** (RECOMENDADO)
   - Aumenta engajamento
   - Implementação rápida
   - Não quebra funcionalidades existentes

4. **Módulos de Conteúdo** (RECOMENDADO)
   - Atende ao requisito "sincronizar módulos de planejamento"
   - Professores podem adicionar material teórico
   - Estrutura similar à já existente (Atividades)

**O que NÃO recomendo para a Entrega 5:**

❌ Envio de dados para órgãos públicos (sem APIs disponíveis)  
❌ Integração com IA (custo e complexidade)  
❌ App mobile (tempo insuficiente)  
❌ API REST (sem necessidade imediata)  

### 8.2 Próximos Passos Imediatos

**Se tiver 1 semana:**
→ Implementar Dashboards + Relatórios PDF

**Se tiver 2 semanas:**
→ Dashboards + Relatórios + Visualização de Dados (mapas/gráficos)

**Se tiver 3 semanas:**
→ Dashboards + Visualização + Gamificação

**Se tiver 4 semanas:**
→ Dashboards + Visualização + Gamificação + Módulos de Conteúdo

---

## 9. CONCLUSÃO

O sistema atual está **SÓLIDO** e **FUNCIONAL**. A arquitetura é boa e escalável.

Para atender aos requisitos da Entrega 5, recomendo focar em:
1. **Melhorar visualização e exportação de dados** (dashboards + relatórios)
2. **Adicionar camada de gamificação** (badges + pontos)
3. **Enriquecer análise de dados** (gráficos + mapas)
4. **Opcionalmente adicionar módulos de conteúdo** (material teórico)

Isso atenderia parcialmente aos requisitos:
- ✅ Banco de dados integrado
- ✅ Autenticação funcionando
- ✅ Dashboards e relatórios (melhorados)
- ⚠️ "Sincronizar módulos de planejamento" (via Módulos de Conteúdo)
- ⚠️ "Dinâmicas para ensino" (via Gamificação)

**Viabilidade:** ALTA  
**Tempo necessário:** 2-4 semanas (dependendo do escopo)  
**Complexidade:** MÉDIA  
**Custo adicional:** Mínimo ($0-5/mês)

---

**Documento gerado em:** 27 de Novembro de 2025  
**Próxima revisão:** Após discussão com o usuário

