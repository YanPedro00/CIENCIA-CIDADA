# ENTREGA 7: APRESENTAÇÃO FINAL E PUBLICAÇÃO

**Equipe:** Equipe 2  
**Disciplina:** Interação Humano-Computador  
**Plataforma:** Ciência Cidadã - Sistema de Projetos Científicos  
**Data:** Dezembro 2024

---

## ACESSO À PLATAFORMA

### Link de Produção
**URL:** https://ciencia-cidada.up.railway.app

### Ambiente de Deploy
- **Plataforma:** Railway (PaaS)
- **Banco de Dados:** PostgreSQL
- **Armazenamento:** Cloudinary (imagens e documentos)
- **Status:** ONLINE - Produção

### Credenciais de Teste

#### Professor
- **Usuário:** `professor`
- **Senha:** `senha123`
- **Turma Demonstração:** Código `A1B2C3D4`

#### Estudante
- **Usuário:** `estudante`
- **Senha:** `senha123`

---

## RESUMO EXECUTIVO DA PLATAFORMA

### Propósito
A plataforma **Ciência Cidadã** é um sistema web educacional que permite professores gerenciarem turmas e estudantes desenvolverem projetos científicos completos seguindo o **método científico de 6 fases**.

### Público-Alvo
- **Professores:** Ensino fundamental, médio e superior
- **Estudantes:** De todas as idades interessados em ciência
- **Instituições:** Escolas, universidades, centros de pesquisa

### Diferencial
Sistema completo que integra **ensino**, **pesquisa**, **coleta de dados**, **gamificação** e **visualização**, tudo em uma única plataforma acessível via web.

---

## ARQUITETURA E TECNOLOGIAS

### Stack Tecnológico

| Camada | Tecnologia | Descrição |
|--------|------------|-----------|
| **Backend** | Django 4.2.7 | Framework web Python MVC |
| **Frontend** | Bootstrap 5 | Interface responsiva e moderna |
| **Banco de Dados** | PostgreSQL | Banco relacional em produção |
| **Autenticação** | Django Auth | Sistema completo de login/registro |
| **Armazenamento** | Cloudinary | CDN para imagens e documentos |
| **Visualização** | Chart.js + Leaflet + Plotly | Gráficos e mapas interativos |
| **Deploy** | Railway | Plataforma PaaS com CI/CD |

### Banco de Dados

**12 Tabelas Principais:**
1. Usuario (professores e estudantes)
2. Turma (classes/disciplinas)
3. Grupo (equipes de trabalho)
4. Projeto (projetos científicos)
5. Observacao (dados coletados)
6. Feedback (comentários do professor)
7. Avaliacao (avaliação final)
8. EstudanteTurma (inscrições)
9. Atividade (tarefas e materiais)
10. Badge (conquistas)
11. UsuarioBadge (gamificação)
12. PontuacaoGrupo (ranking)

**Relacionamentos:**
- 3 relacionamentos 1:1
- 12 relacionamentos 1:N
- 3 relacionamentos M:N

---

## FUNCIONALIDADES IMPLEMENTADAS

### Para Professores

#### Gerenciamento de Turmas
- Criar turmas com código de acesso único
- Configurar limites (grupos, membros)
- Visualizar estudantes inscritos
- Ativar/desativar turmas

#### Gerenciamento de Grupos
- Aprovar formação de grupos
- Monitorar composição
- Ver projetos de cada grupo

#### Acompanhamento de Projetos
- Dashboard com todos os projetos da turma
- Visualização por fase (1-6)
- Gráficos de progresso
- Status em tempo real

#### Feedbacks e Avaliações
- Comentar em cada fase
- Aprovar/reprovar fases
- Avaliação final com notas (0-10) para cada fase
- Conceitos: A, B, C, D
- Comentários estruturados (pontos fortes, a melhorar)

#### Atividades
- Criar atividades para turma
- Anexar materiais (PDF, DOCX, etc.)
- Definir prazos
- Fixar atividades importantes
- Tipos: informação, tarefa, material, aviso

### Para Estudantes

#### Participação em Turmas
- Entrar via código de acesso
- Visualizar informações da turma
- Acessar atividades postadas

#### Formação de Grupos
- Criar grupo (líder)
- Entrar em grupo existente
- Visualizar membros
- Sistema de pontuação

#### Desenvolvimento de Projetos

**Fase 1: Problema de Pesquisa**
- Definir pergunta científica
- Justificar importância
- Estabelecer objetivos

**Fase 2: Hipótese**
- Formular hipótese principal
- Fundamentação teórica
- Pesquisa bibliográfica

**Fase 3: Metodologia**
- Método de coleta de dados
- Materiais e ferramentas
- Cronograma
- Local da pesquisa

**Fase 4: Coleta de Dados**
- Registrar observações
- Anexar até 3 fotos por observação
- Geolocalização (latitude/longitude)
- Dados estruturados (JSON)
- Descrição detalhada

**Fase 5: Análise de Dados**
- Organização dos dados
- Interpretação dos resultados
- Discussão científica
- Visualização em gráficos e mapas

**Fase 6: Conclusão**
- Responder à pergunta inicial
- Confirmar/refutar hipótese
- Aprendizados
- Limitações do estudo

#### Anexos do Projeto
- Relatório final (PDF/DOCX)
- Apresentação (PPT/PDF)
- Foto da equipe
- Até 3 anexos extras (qualquer formato)

#### Gamificação
**10 Badges disponíveis:**
- Primeira Observação
- 5 Observações Completas
- Explorador (com geolocalização)
- Colaborador (membro de grupo)
- Líder de Grupo
- Fases 1, 3 e 6 Aprovadas
- Projeto Concluído
- Primeira Foto Anexada

**Sistema de Pontos:**
- Pontuação acumulativa por grupo
- Ranking entre grupos da turma

---

## DASHBOARDS E VISUALIZAÇÕES

### Dashboard do Professor

**Gráficos:**
- Pizza: Status dos projetos (rascunho, andamento, concluído)
- Barras: Top 5 áreas científicas mais populares

**Estatísticas:**
- Total de turmas criadas
- Total de grupos formados
- Total de projetos em andamento
- Total de estudantes ativos

**Lista:**
- Projetos recentes com fase atual
- Progresso percentual
- Acesso rápido aos detalhes

### Dashboard do Estudante

**Informações do Grupo:**
- Nome do grupo e membros
- Líder destacado
- Pontuação total

**Progresso do Projeto:**
- Barra visual (0-100%)
- Fases concluídas (checkmarks)
- Fase atual em destaque

**Badges Conquistadas:**
- Lista com ícones e descrições
- Data de conquista
- Pontos ganhos

### Visualização de Dados Científicos

**Mapa Interativo (Leaflet):**
- Marcadores para cada observação
- Popup com título, data e local
- Navegação interativa
- Zoom e pan

**Gráficos (Plotly):**
- Linha temporal de coleta
- Distribuição de dados
- Análises customizadas por projeto

### Exportação de Relatórios

**PDF (ReportLab):**
- Relatório completo do projeto
- Todas as fases documentadas
- Lista de observações
- Formatação profissional

**CSV/Excel (Pandas):**
- Dados tabulares de observações
- Pronto para análise estatística
- Compatível com Excel e R

---

## EXEMPLOS PRÁTICOS

### Exemplo 1: Projeto de Qualidade da Água

**Turma:** Ciências Ambientais - 9º Ano  
**Grupo:** Os Cientistas  
**Área:** Ciências Ambientais

**Fase 1 - Problema:**
> "A água do rio local está contaminada?"

**Fase 2 - Hipótese:**
> "Acreditamos que a água apresenta níveis elevados de coliformes devido ao esgoto não tratado."

**Fase 3 - Metodologia:**
> Coleta de 10 amostras em pontos diferentes do rio, análise com kit de teste de pH e coliformes, durante 2 semanas.

**Fase 4 - Coleta:**
- 10 observações registradas
- Cada uma com: foto, localização GPS, medições de pH e temperatura
- Dados estruturados em JSON

**Fase 5 - Análise:**
> Mapa mostrando pontos críticos de contaminação, gráfico de pH ao longo do rio, correlação com proximidade de residências.

**Fase 6 - Conclusão:**
> Hipótese confirmada parcialmente. 60% dos pontos apresentaram contaminação. Aprendizado: importância do saneamento básico.

**Resultado:** Conceito A, projeto apresentado na feira de ciências da escola.

---

### Exemplo 2: Projeto de Astronomia

**Turma:** Física - 2º Ano  
**Grupo:** Star Gazers  
**Área:** Astronomia

**Fase 1 - Problema:**
> "Quantas estrelas são visíveis a olho nu em nossa cidade?"

**Fase 2 - Hipótese:**
> "Devido à poluição luminosa, esperamos ver menos de 100 estrelas em uma noite clara."

**Fase 3 - Metodologia:**
> Observação em 5 locais diferentes da cidade, contagem manual, registro fotográfico com câmera de longa exposição.

**Fase 4 - Coleta:**
- 5 observações em locais distintos
- Fotos de longa exposição
- Geolocalização de cada ponto
- Contagem de estrelas visíveis

**Fase 5 - Análise:**
> Mapa da cidade mostrando variação de estrelas visíveis. Gráfico correlacionando distância do centro urbano com quantidade de estrelas.

**Fase 6 - Conclusão:**
> Hipótese refutada. Foram visíveis entre 50-200 estrelas dependendo da localização. Áreas periféricas permitem melhor observação.

**Resultado:** Conceito B, dados usados em campanha de conscientização sobre poluição luminosa.

---

### Exemplo 3: Projeto de Biologia

**Turma:** Biologia - 1º Ano  
**Grupo:** Eco Warriors  
**Área:** Biologia

**Fase 1 - Problema:**
> "Quais espécies de pássaros habitam o parque da escola?"

**Fase 2 - Hipótese:**
> "Acreditamos encontrar pelo menos 10 espécies diferentes, com predominância de pardais e pombos."

**Fase 3 - Metodologia:**
> Observação diária durante 1 mês, identificação por guia de campo, registro fotográfico, horários variados (manhã, tarde).

**Fase 4 - Coleta:**
- 30 observações ao longo de 1 mês
- Fotos de cada espécie avistada
- Localização dos avistamentos
- Horário e comportamento observado

**Fase 5 - Análise:**
> Identificadas 15 espécies. Mapa de calor mostrando locais de maior avistamento. Gráfico de espécies por horário.

**Fase 6 - Conclusão:**
> Hipótese confirmada. Biodiversidade maior que esperada. Aprendizado: importância de áreas verdes urbanas para preservação.

**Resultado:** Conceito A, projeto gerou proposta de ampliação do parque.

---

## IMPACTO SOCIAL E TÉCNICO

### Impacto Social

**Educação:**
- Democratiza acesso ao método científico
- Professores de qualquer área podem usar
- Estudantes aprendem fazendo (learning by doing)

**Ciência Cidadã:**
- Dados reais coletados por estudantes
- Contribuição para pesquisas locais
- Conscientização ambiental e social

**Engajamento:**
- Gamificação motiva participação
- Trabalho em equipe desenvolve soft skills
- Autonomia no processo de pesquisa

**Acessibilidade:**
- 100% web (qualquer dispositivo)
- Interface intuitiva (Bootstrap)
- Documentação completa disponível

### Impacto Técnico

**Inovação:**
- Primeira plataforma integrada para projetos científicos escolares
- Combina educação + pesquisa + gamificação + visualização
- Código aberto (pode ser adaptado)

**Escalabilidade:**
- Arquitetura preparada para milhares de usuários
- PostgreSQL otimizado
- Cloudinary para armazenamento ilimitado
- Deploy automático (CI/CD)

**Qualidade de Código:**
- Django (framework robusto)
- 12 tabelas bem relacionadas
- Migrations versionadas
- Documentação técnica completa

**Segurança:**
- Autenticação robusta
- CSRF protection
- Permissões granulares (professor vs estudante)
- HTTPS em produção

---

## PROCESSOS E APRENDIZADOS

### Metodologia de Desenvolvimento

**Ferramentas Utilizadas:**
- **Git/GitHub:** Controle de versão
- **Railway:** Deploy contínuo
- **VS Code/Cursor:** Desenvolvimento
- **PostgreSQL:** Banco de dados
- **Cloudinary:** Armazenamento de mídia

**Processo:**
1. **Levantamento de Requisitos** - Análise do problema e usuários
2. **Design do Banco de Dados** - Modelagem ER
3. **Desenvolvimento Incremental** - 7 entregas progressivas
4. **Testes de Usabilidade** - Feedback real de usuários
5. **Deploy em Produção** - Railway com CI/CD
6. **Documentação** - Guias completos para uso e desenvolvimento

### Principais Desafios e Soluções

#### Desafio 1: Armazenamento de Arquivos
**Problema:** Railway usa armazenamento efêmero (arquivos são perdidos).

**Solução:** 
- Integração com Cloudinary
- `DocumentStorage` customizado para PDFs/CSVs
- `MediaCloudinaryStorage` para imagens
- URLs permanentes via CDN

#### Desafio 2: Migrações de Banco de Dados
**Problema:** Migrações não aplicadas automaticamente no deploy.

**Solução:**
- Script `start.sh` executando `migrate` antes do servidor
- `makemigrations` no build para detectar mudanças
- Migrations versionadas no Git

#### Desafio 3: Complexidade do Método Científico
**Problema:** 6 fases com aprovação sequencial é complexo.

**Solução:**
- Sistema de estados no model `Projeto`
- Métodos `pode_avancar_fase()` e `avancar_fase()`
- Feedbacks do professor por fase
- Interface clara mostrando progresso

#### Desafio 4: Gamificação
**Problema:** Atribuir badges manualmente é trabalhoso.

**Solução:**
- Django Signals (automático)
- `@receiver` detecta eventos (criar observação, aprovar fase)
- Badges atribuídas instantaneamente
- Notificação visual para usuário

#### Desafio 5: Visualização de Dados Científicos
**Problema:** Dados brutos são difíceis de interpretar.

**Solução:**
- Mapas Leaflet para geolocalização
- Gráficos Plotly para análises
- Exportação CSV para análises externas
- Dashboard com estatísticas visuais

### Lições Aprendidas

**Técnicas:**
1. **Django é poderoso:** ORM facilita muito o desenvolvimento
2. **PostgreSQL vs SQLite:** Produção exige banco robusto
3. **Cloudinary é essencial:** Armazenamento efêmero não funciona para produção
4. **Migrations são críticas:** Sempre versionar e testar
5. **Signals são úteis:** Automatizam processos complexos

**Gestão de Projeto:**
1. **Documentação é fundamental:** Facilita manutenção e colaboração
2. **Entregas incrementais:** Melhor que big bang
3. **Feedback real é valioso:** Testes de usabilidade revelam problemas
4. **CI/CD economiza tempo:** Deploy automático evita erros manuais
5. **Git é inegociável:** Controle de versão salva o projeto

**Design de Sistema:**
1. **Modelagem do banco primeiro:** Base sólida evita refatorações
2. **Separar permissões:** Professor vs Estudante desde o início
3. **Gamificação funciona:** Usuários realmente se engajam
4. **Interface simples:** Bootstrap reduz tempo de desenvolvimento
5. **Responsividade:** Mobile-first é obrigatório hoje

---

## DOCUMENTAÇÃO DISPONÍVEL

### Para Usuários
1. **USUARIOS_TESTE.md** - Credenciais e dados de teste
2. **GUIA_TESTES_USABILIDADE.md** - Como testar a plataforma

### Para Desenvolvedores
1. **DIAGRAMA_BANCO_DADOS.md** - Diagrama ER e descrição de tabelas
2. **VARIAVEIS_AMBIENTE.md** - Configuração de ambiente
3. **RAILWAY_CLOUDINARY_SETUP.md** - Configuração de deploy
4. **ARMAZENAMENTO_MIDIA.md** - Explicação sobre arquivos

### Para Apresentação
1. **ENTREGA5_COMPLETA.md** - Detalhamento de funcionalidades
2. **RELATORIO_ENTREGA5.txt** - Relatório executivo
3. **ENTREGA7_APRESENTACAO_FINAL.md** - Este documento

---

## RETROSPECTIVA E CONQUISTAS

### Retrospectiva do Projeto

#### O que funcionou bem?
- **Arquitetura modular:** Django facilita manutenção
- **Entregas incrementais:** Feedback contínuo melhorou o produto
- **Documentação detalhada:** Facilita onboarding e apresentação
- **Deploy automático:** Railway simplifica infraestrutura
- **Gamificação:** Engajamento real dos usuários

#### O que pode melhorar?
- **Testes automatizados:** Faltam testes unitários e de integração
- **Interface mobile:** Pode ser mais otimizada para celular
- **Notificações:** Implementar sistema de alertas (email/push)
- **API REST:** Permitir integrações externas
- **Internacionalização:** Suporte a múltiplos idiomas

#### Próximos Passos (Roadmap)
1. **Curto Prazo (1-3 meses):**
   - Implementar testes automatizados
   - Melhorar interface mobile
   - Sistema de notificações por email
   
2. **Médio Prazo (3-6 meses):**
   - API REST para integrações
   - Aplicativo mobile nativo
   - Chat entre membros do grupo
   
3. **Longo Prazo (6-12 meses):**
   - Inteligência Artificial para sugestões de projetos
   - Rede social científica
   - Integração com plataformas educacionais (Moodle, Canvas)

### Conquistas da Equipe

#### Métricas do Projeto
- **Linhas de Código:** ~5.000 linhas Python + 3.000 linhas HTML/CSS/JS
- **Commits Git:** 50+ commits
- **Tabelas no Banco:** 12 tabelas relacionadas
- **Funcionalidades:** 30+ funcionalidades implementadas
- **Documentação:** 10+ arquivos MD totalizando 4.000+ linhas
- **Tempo de Desenvolvimento:** 4 meses
- **Entregas:** 7 entregas progressivas

#### Resultados Alcançados
- **Plataforma 100% funcional** em produção
- **Todos os requisitos** da disciplina implementados
- **Documentação completa** técnica e de usuário
- **Testes de usabilidade** realizados com feedback positivo
- **Deploy automatizado** com CI/CD
- **Código aberto** disponível no GitHub

#### Reconhecimentos
- **Inovação:** Primeira plataforma do tipo no contexto educacional brasileiro
- **Qualidade:** Código limpo e bem documentado
- **Impacto:** Potencial real de uso em escolas
- **Técnico:** Stack moderno e escalável

---

## LINKS E RECURSOS

### Plataforma
- **URL de Produção:** https://ciencia-cidada.up.railway.app
- **Repositório GitHub:** https://github.com/YanPedro00/CIENCIA-CIDADA

### Ambiente de Deploy
- **Plataforma:** Railway (https://railway.app)
- **Banco de Dados:** PostgreSQL (Railway)
- **CDN:** Cloudinary (https://cloudinary.com)

### Tecnologias
- **Django:** https://www.djangoproject.com
- **Bootstrap:** https://getbootstrap.com
- **Chart.js:** https://www.chartjs.org
- **Leaflet:** https://leafletjs.com
- **Plotly:** https://plotly.com/python

### Documentação Técnica
- **Django Models:** https://docs.djangoproject.com/en/4.2/topics/db/models/
- **PostgreSQL:** https://www.postgresql.org/docs/
- **Cloudinary Django:** https://cloudinary.com/documentation/django_integration

---

## CONTATO E SUPORTE

### Equipe de Desenvolvimento
**Equipe 2 - Interação Humano-Computador**

### Reportar Problemas
- Abrir issue no repositório GitHub
- Contato via plataforma (menu Sobre)

### Contribuições
- Fork do repositório
- Pull requests são bem-vindos
- Seguir guia de contribuição (CONTRIBUTING.md)

---

## CONCLUSÃO

A plataforma **Ciência Cidadã** representa um marco na democratização do acesso ao método científico no contexto educacional brasileiro. Através de tecnologias modernas e design centrado no usuário, conseguimos criar uma ferramenta que:

1. **Empodera professores** a gerenciar turmas e projetos de forma eficiente
2. **Engaja estudantes** através de gamificação e autonomia
3. **Facilita a pesquisa** com ferramentas de coleta e análise de dados
4. **Visualiza conhecimento** através de dashboards e mapas interativos
5. **Escala facilmente** para centenas de turmas e milhares de usuários

O projeto não só atende todos os requisitos técnicos da disciplina, mas vai além ao criar impacto social real, preparando uma nova geração de cientistas cidadãos.

**Status:** Produção - 100% Funcional  
**Última Atualização:** Dezembro 2024  
**Versão:** 1.0.0

---

*Documento preparado para a Entrega 7 da disciplina de Interação Humano-Computador*

