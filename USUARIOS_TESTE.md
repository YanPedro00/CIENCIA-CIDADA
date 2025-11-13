# USUÁRIOS DE TESTE - PLATAFORMA CIÊNCIA CIDADÃ

## ACESSO AO SISTEMA

**URL do Sistema:** https://web-production-e06df.up.railway.app

**Painel Administrativo:** https://web-production-e06df.up.railway.app/admin

---

## CONTA ADMINISTRATIVA

### Administrador do Sistema
- **Usuário:** admin
- **Senha:** admin123456
- **Tipo:** Superusuário

**Permissões:**
- Acesso total ao sistema
- Gerenciamento de todos os usuários
- Acesso ao painel administrativo Django
- Criação e exclusão de turmas, grupos e projetos
- Visualização de todos os dados

---

## CONTA DE PROFESSOR

### Prof. Carlos Silva
- **Usuário:** prof_teste
- **Senha:** prof123456
- **Email:** prof.teste@escola.com
- **Nome Completo:** Carlos Silva
- **Instituição:** Escola Estadual Exemplo
- **Tipo:** Professor

**Ações permitidas:**
- Criar e gerenciar turmas
- Gerar códigos de acesso para turmas
- Criar e gerenciar grupos de estudantes
- Visualizar todos os projetos da turma
- Dar feedback nas fases dos projetos
- Aprovar ou reprovar cada fase do método científico
- Avaliar projetos finalizados com conceito (A, B, C, D)
- Atribuir notas de 0 a 10 para cada fase
- Criar, editar e excluir atividades da turma
- Fixar atividades importantes
- Anexar arquivos em atividades

---

## CONTAS DE ESTUDANTES

### 1. João Santos
- **Usuário:** aluno1
- **Senha:** aluno123456
- **Email:** joao.santos@email.com
- **Nome Completo:** João Santos
- **Instituição:** Escola Estadual Exemplo
- **Tipo:** Estudante

### 2. Ana Costa
- **Usuário:** aluno2
- **Senha:** aluno123456
- **Email:** ana.costa@email.com
- **Nome Completo:** Ana Costa
- **Instituição:** Escola Estadual Exemplo
- **Tipo:** Estudante

### 3. Pedro Oliveira
- **Usuário:** aluno3
- **Senha:** aluno123456
- **Email:** pedro.oliveira@email.com
- **Nome Completo:** Pedro Oliveira
- **Instituição:** Escola Estadual Exemplo
- **Tipo:** Estudante

### 4. Maria Souza
- **Usuário:** aluno4
- **Senha:** aluno123456
- **Email:** maria.souza@email.com
- **Nome Completo:** Maria Souza
- **Instituição:** Escola Estadual Exemplo
- **Tipo:** Estudante

**Ações permitidas:**
- Entrar em turmas usando código de acesso
- Criar grupos ou entrar em grupos existentes
- Criar projetos científicos para o grupo
- Preencher as 6 fases do método científico
- Adicionar observações com fotos e dados
- Visualizar feedbacks do professor
- Visualizar notas e avaliação final
- Visualizar atividades postadas pelo professor
- Baixar arquivos anexados em atividades

---

## SIMULAÇÃO COMPLETA DO SISTEMA

### ETAPA 1: LOGIN COMO PROFESSOR

1. Acesse: https://web-production-e06df.up.railway.app/login
2. Faça login com as credenciais:
   - Usuário: prof_teste
   - Senha: prof123456
3. Você será direcionado ao Dashboard do Professor

### ETAPA 2: CRIAR TURMA

1. No menu superior, clique em "Minhas Turmas"
2. Clique no botão "Criar Turma"
3. Preencha o formulário:
   - Nome da Turma: "Ciências 2024 - Turma A"
   - Descrição: "Turma de projetos científicos do 2º ano"
   - Ano/Semestre: "2024.2"
   - Máximo de Grupos: 10
   - Máximo de Membros por Grupo: 5
   - Turma Ativa: Sim
4. Clique em "Salvar"
5. **ANOTE O CÓDIGO DE ACESSO** gerado (exemplo: A1B2C3D4)

### ETAPA 3: CRIAR ATIVIDADE PARA TURMA

1. Na página da turma, clique em "Atividades"
2. Clique em "Nova Atividade"
3. Crie um aviso de boas-vindas:
   - Título: "Bem-vindos à disciplina de Ciências!"
   - Tipo: Aviso
   - Descrição: "Olá turma! Neste semestre trabalharemos com o método científico. Formem grupos de até 5 pessoas e escolham um tema para pesquisa."
   - Fixar no Topo: Sim
   - Ativo: Sim
4. Salve a atividade
5. Crie uma tarefa:
   - Título: "Definir tema do projeto científico"
   - Tipo: Tarefa
   - Descrição: "Em grupo, escolham um tema relacionado a meio ambiente, saúde ou tecnologia. Preparem uma pergunta de pesquisa."
   - Data de Entrega: (escolha uma data futura)
   - Ativo: Sim
6. Salve a tarefa

### ETAPA 4: LOGIN COMO ESTUDANTE

1. Abra uma janela anônima do navegador ou use outro navegador
2. Acesse: https://web-production-e06df.up.railway.app/login
3. Faça login com:
   - Usuário: aluno1
   - Senha: aluno123456

### ETAPA 5: ENTRAR NA TURMA

1. No menu superior, clique em "Entrar em Turma"
2. Digite o código de acesso anotado na Etapa 2
3. Clique em "Entrar"
4. Você verá a mensagem de confirmação
5. A turma aparecerá no seu dashboard

### ETAPA 6: VISUALIZAR ATIVIDADES DA TURMA

1. No dashboard, clique na turma que você entrou
2. Clique no botão "Ver Atividades"
3. Visualize as atividades criadas pelo professor
4. Clique em uma atividade para ver detalhes completos
5. Se houver arquivo anexo, você pode baixá-lo

### ETAPA 7: CRIAR GRUPO

1. Volte para a página da turma
2. Clique em "Criar Grupo"
3. Preencha:
   - Nome do Grupo: "Guardiões do Meio Ambiente"
   - Selecione os membros: aluno2, aluno3
   - Líder do Grupo: aluno1 (você)
4. Salve o grupo

### ETAPA 8: CRIAR PROJETO

1. Entre no grupo criado
2. Clique em "Criar Projeto"
3. Preencha:
   - Título: "Análise da Qualidade da Água do Rio Municipal"
   - Área da Ciência: Ciências Ambientais
   - Descrição Breve: "Investigação sobre possíveis fontes de poluição no rio que abastece a cidade"
4. Salve o projeto
5. Você será direcionado para a Fase 1

### ETAPA 9: PREENCHER FASE 1 - PROBLEMA DE PESQUISA

1. Clique em "Editar Fase 1"
2. Preencha:
   - **Pergunta de Pesquisa:** "A água do rio municipal está adequada para consumo humano?"
   - **Justificativa:** "O rio é a principal fonte de abastecimento da cidade. Há relatos de descarte irregular de resíduos próximo às margens. É fundamental verificar se a qualidade da água atende aos padrões estabelecidos pela legislação."
   - **Objetivos:** "Analisar a qualidade físico-química da água em diferentes pontos do rio; Identificar possíveis fontes de contaminação; Comparar os resultados com os padrões de potabilidade."
3. Salve a fase
4. Aguarde aprovação do professor

### ETAPA 10: PROFESSOR AVALIAR FASE 1

1. Volte ao navegador do professor (prof_teste)
2. No dashboard, você verá o projeto na lista de "Projetos Aguardando Aprovação"
3. Clique no projeto
4. Leia a Fase 1 preenchida
5. Clique em "Dar Feedback - Fase 1"
6. Escreva um feedback:
   - Comentário: "Excelente definição do problema! A pergunta está clara e os objetivos bem estruturados. Vocês podem avançar para a próxima fase."
   - Marque: Aprovado
7. Salve o feedback
8. Clique em "Aprovar Fase 1"
9. Confirme a aprovação

### ETAPA 11: PREENCHER FASE 2 - HIPÓTESE

1. Volte ao navegador do estudante
2. Atualize a página do projeto
3. Verifique que agora está na Fase 2
4. Clique em "Editar Fase 2"
5. Preencha:
   - **Hipótese Principal:** "A água do rio apresenta níveis de contaminação acima do permitido, especialmente nos pontos próximos à área industrial."
   - **Fundamentação Teórica:** "Estudos anteriores mostraram que descartes industriais afetam significativamente a qualidade da água. Parâmetros como pH, turbidez e presença de metais pesados costumam estar alterados próximo a fontes de poluição."
6. Salve e aguarde aprovação

### ETAPA 12: PREENCHER FASE 3 - METODOLOGIA

1. Após aprovação da Fase 2 pelo professor
2. Clique em "Editar Fase 3"
3. Preencha:
   - **Método de Coleta:** "Coleta de amostras de água em 5 pontos diferentes do rio (nascente, área residencial, área industrial, área rural e foz). Amostras serão coletadas em frascos esterilizados de 500ml."
   - **Materiais e Ferramentas:** "Frascos esterilizados, luvas, etiquetas, GPS para marcação de coordenadas, kit de análise de pH, termômetro, turbidímetro."
   - **Cronograma:** "Semana 1: Preparação e identificação dos pontos. Semana 2: Coleta das amostras. Semana 3: Análises laboratoriais. Semana 4: Compilação dos dados."
   - **Local da Pesquisa:** "Rio Municipal, desde a nascente (Zona Rural) até a foz (Centro da Cidade)"
4. Salve e aguarde aprovação

### ETAPA 13: FASE 4 - COLETA DE DADOS (OBSERVAÇÕES)

1. Após aprovação da Fase 3
2. Na página do projeto, clique em "Adicionar Observação"
3. Crie a primeira observação:
   - Título: "Ponto 1 - Nascente"
   - Descrição: "Amostra coletada na nascente do rio. Água cristalina, sem odor. Área preservada com vegetação nativa ao redor."
   - Dados Estruturados (JSON): {"ph": 7.2, "temperatura": 18, "turbidez": 2}
   - Local: "Nascente - Zona Rural"
   - Data e Hora: (selecione)
   - (Opcional) Anexe uma foto
4. Salve a observação
5. Repita para mais 3-4 observações em diferentes pontos

### ETAPA 14: PROFESSOR APROVAR FASE 4

1. Volte ao navegador do professor
2. Entre no projeto
3. Visualize as observações adicionadas
4. Dê feedback e aprove a Fase 4

### ETAPA 15: PREENCHER FASE 5 - ANÁLISE DE DADOS

1. Volte ao estudante
2. Clique em "Editar Fase 5"
3. Preencha:
   - **Organização dos Dados:** "Os dados foram organizados em uma tabela comparando os 5 pontos de coleta. Foram analisados pH, temperatura, turbidez e presença de resíduos sólidos."
   - **Interpretação dos Resultados:** "O ponto próximo à área industrial apresentou pH mais ácido (5.8) e maior turbidez (45 NTU). Os demais pontos mantiveram-se dentro dos padrões aceitáveis."
   - **Discussão:** "Os resultados confirmam que há contaminação significativa no ponto industrial. Isso pode estar relacionado ao descarte inadequado de efluentes. A qualidade da água se recupera parcialmente após esse ponto."
4. Salve e aguarde aprovação

### ETAPA 16: PREENCHER FASE 6 - CONCLUSÃO

1. Após aprovação da Fase 5
2. Clique em "Editar Fase 6"
3. Preencha:
   - **Hipótese Confirmada:** Parcialmente confirmada
   - **Conclusão:** "A pesquisa confirmou que há contaminação da água no ponto próximo à indústria, mas não em todos os pontos. A hipótese foi parcialmente confirmada pois a contaminação não está generalizada em todo o rio."
   - **Aprendizados:** "Aprendemos a importância do método científico para investigações ambientais. Também percebemos como atividades humanas impactam recursos naturais."
   - **Limitações do Estudo:** "Não foi possível realizar análises microbiológicas completas. O período de coleta foi curto (1 mês). Não houve recursos para análise de metais pesados."
4. Salve e aguarde aprovação

### ETAPA 17: PROFESSOR AVALIAR PROJETO FINAL

1. Volte ao professor
2. Após aprovar a Fase 6, clique em "Avaliar Projeto"
3. Preencha a avaliação:
   - **Conceito Final:** A (Excelente)
   - **Nota - Definição do Problema:** 9
   - **Nota - Hipótese:** 8
   - **Nota - Metodologia:** 9
   - **Nota - Coleta de Dados:** 10
   - **Nota - Análise:** 8
   - **Nota - Conclusão:** 9
   - **Comentários Gerais:** "Excelente trabalho! O grupo demonstrou compreensão profunda do método científico e realizou uma investigação bem estruturada."
   - **Pontos Fortes:** "Metodologia bem planejada, coleta de dados sistemática, análise crítica dos resultados."
   - **Pontos a Melhorar:** "Poderiam ter expandido o período de coleta para incluir diferentes estações do ano."
4. Salve a avaliação

### ETAPA 18: ESTUDANTE VISUALIZAR AVALIAÇÃO

1. Volte ao navegador do estudante
2. Entre no projeto
3. Visualize a avaliação final
4. Veja o conceito, as notas e os comentários do professor

---

## RESUMO DAS CREDENCIAIS

| Tipo | Usuário | Senha |
|------|---------|-------|
| Administrador | admin | admin123456 |
| Professor | prof_teste | prof123456 |
| Estudante 1 | aluno1 | aluno123456 |
| Estudante 2 | aluno2 | aluno123456 |
| Estudante 3 | aluno3 | aluno123456 |
| Estudante 4 | aluno4 | aluno123456 |

---

## DICAS PARA TESTES

### Testar com Múltiplas Contas Simultaneamente

**Opção 1: Navegadores Diferentes**
- Use Chrome para o professor
- Use Firefox para um estudante
- Use Safari para outro estudante

**Opção 2: Janelas Anônimas/Privadas**
- Chrome: Ctrl+Shift+N (Windows) ou Cmd+Shift+N (Mac)
- Firefox: Ctrl+Shift+P (Windows) ou Cmd+Shift+P (Mac)
- Safari: Cmd+Shift+N (Mac)
- Edge: Ctrl+Shift+N (Windows)

**Opção 3: Perfis do Navegador**
- Crie diferentes perfis no Chrome
- Cada perfil mantém sessões independentes

### Sugestões de Temas para Projetos

**1. Qualidade da Água**
- Problema: A água do rio está contaminada?
- Hipótese: Sim, devido a descartes industriais
- Área: Ciências Ambientais

**2. Horta Escolar Sustentável**
- Problema: Qual o melhor tipo de adubo orgânico?
- Hipótese: Húmus de minhoca é mais eficiente
- Área: Biologia

**3. Consumo de Energia na Escola**
- Problema: Quanto energia é desperdiçada?
- Hipótese: 30% do consumo é desnecessário
- Área: Tecnologia

**4. Reciclagem de Resíduos Sólidos**
- Problema: Quanto lixo poderia ser reciclado?
- Hipótese: 60% do lixo escolar é reciclável
- Área: Ciências Ambientais

**5. Plantas Medicinais Locais**
- Problema: Quais plantas locais têm propriedades medicinais?
- Hipótese: Plantas nativas têm mais compostos bioativos
- Área: Biologia

---

## CHECKLIST DE VALIDAÇÃO DO SISTEMA

### Funcionalidades do Professor
- [ ] Login bem-sucedido
- [ ] Criar turma
- [ ] Gerar código de acesso
- [ ] Visualizar turmas criadas
- [ ] Editar turma
- [ ] Criar atividade (Informação)
- [ ] Criar atividade (Tarefa com prazo)
- [ ] Criar atividade (Material com anexo)
- [ ] Criar atividade (Aviso)
- [ ] Fixar atividade no topo
- [ ] Editar atividade
- [ ] Excluir atividade
- [ ] Criar grupo para turma
- [ ] Visualizar todos os grupos
- [ ] Ver projetos pendentes no dashboard
- [ ] Acessar projeto de estudante
- [ ] Dar feedback em fase
- [ ] Aprovar fase
- [ ] Reprovar fase (testar também)
- [ ] Avançar projeto para próxima fase
- [ ] Avaliar projeto concluído
- [ ] Atribuir conceito (A, B, C, D)
- [ ] Atribuir notas (0-10) por fase
- [ ] Escrever comentários detalhados

### Funcionalidades do Estudante
- [ ] Login bem-sucedido
- [ ] Entrar em turma com código
- [ ] Visualizar turmas inscritas
- [ ] Visualizar atividades da turma
- [ ] Ver detalhes de atividade
- [ ] Baixar arquivo anexado em atividade
- [ ] Filtrar atividades (ativas/fixadas)
- [ ] Criar grupo
- [ ] Entrar em grupo existente
- [ ] Visualizar membros do grupo
- [ ] Criar projeto para grupo
- [ ] Preencher Fase 1
- [ ] Preencher Fase 2
- [ ] Preencher Fase 3
- [ ] Adicionar observação (Fase 4)
- [ ] Adicionar foto em observação
- [ ] Adicionar dados JSON em observação
- [ ] Preencher Fase 5
- [ ] Preencher Fase 6
- [ ] Visualizar feedback do professor
- [ ] Ver status de aprovação de cada fase
- [ ] Visualizar progresso do projeto (%)
- [ ] Visualizar avaliação final
- [ ] Ver conceito recebido
- [ ] Ver notas por fase
- [ ] Editar fases antes da aprovação

### Interface e Usabilidade
- [ ] Layout responsivo (desktop)
- [ ] Layout responsivo (tablet)
- [ ] Layout responsivo (mobile)
- [ ] Navegação clara e intuitiva
- [ ] Breadcrumbs funcionando
- [ ] Mensagens de sucesso visíveis
- [ ] Mensagens de erro claras
- [ ] Botões e links bem posicionados
- [ ] Cores e ícones adequados
- [ ] Formulários intuitivos
- [ ] Validação de campos funciona
- [ ] Upload de arquivos funciona
- [ ] Download de arquivos funciona
- [ ] Imagens carregam corretamente

### Regras de Negócio
- [ ] Estudante não pode editar fase aprovada
- [ ] Estudante não pode pular fases
- [ ] Estudante não vê atividades inativas
- [ ] Professor vê todas as atividades
- [ ] Grupo não pode ter mais que máximo de membros
- [ ] Turma não pode ter mais que máximo de grupos
- [ ] Código de turma inválido é rejeitado
- [ ] Projeto só avança após aprovação
- [ ] Todas as 6 fases devem ser aprovadas
- [ ] Avaliação só é possível com projeto concluído
- [ ] Progresso é calculado corretamente

---

## CENÁRIOS DE TESTE AVANÇADOS

### Cenário 1: Grupo Colaborativo
1. Crie um grupo com 4 estudantes (aluno1, aluno2, aluno3, aluno4)
2. Cada estudante adiciona 2 observações diferentes
3. Verifique se todas as observações aparecem no projeto
4. Teste se todos os membros podem editar as fases

### Cenário 2: Múltiplos Projetos
1. Crie 3 grupos diferentes na mesma turma
2. Cada grupo cria um projeto com tema diferente
3. Professor gerencia os 3 projetos simultaneamente
4. Verifique organização no dashboard

### Cenário 3: Feedback Detalhado
1. Professor reprova uma fase
2. Estudante lê o feedback
3. Estudante corrige e reenvia
4. Professor aprova após correção
5. Projeto avança normalmente

### Cenário 4: Atividades Diversas
1. Crie 10 atividades de tipos diferentes
2. Fixe 2 atividades importantes
3. Desative 1 atividade antiga
4. Verifique visualização do estudante
5. Teste filtros e ordenação

---

## PROBLEMAS CONHECIDOS E SOLUÇÕES

### Problema: "CSRF verification failed"
**Solução:** Limpe os cookies do navegador ou use janela anônima

### Problema: Não consigo fazer upload de imagens
**Solução:** Verifique se o arquivo não ultrapassa 5MB. Use formatos JPG ou PNG.

### Problema: Projeto não avança após aprovação
**Solução:** Certifique-se de que clicou em "Aprovar Fase" após dar o feedback.

### Problema: Não vejo as atividades criadas
**Solução:** Estudantes só veem atividades marcadas como "Ativo". Verifique se professor ativou a atividade.

### Problema: Código de turma não funciona
**Solução:** O código é case-sensitive. Digite exatamente como foi gerado, em letras maiúsculas.

---

## CONTATO E SUPORTE

Para reportar bugs ou solicitar funcionalidades:
- Repositório GitHub: https://github.com/YanPedro00/CIENCIA-CIDADA
- Issues: https://github.com/YanPedro00/CIENCIA-CIDADA/issues

---

## OBSERVAÇÕES FINAIS

Este documento foi criado para facilitar os testes e validação da Plataforma Ciência Cidadã. Todos os usuários listados são ficcionais e criados especificamente para fins de teste.

O sistema implementa as 6 fases do método científico:
1. Problema de Pesquisa
2. Hipótese
3. Metodologia
4. Coleta de Dados (Observações)
5. Análise de Dados
6. Conclusão

A plataforma foi desenvolvida para uso educacional em cursos de extensão e disciplinas de ciências, promovendo o aprendizado ativo através da prática do método científico.

Data de atualização deste documento: Novembro de 2024
Versão da plataforma: 1.0
