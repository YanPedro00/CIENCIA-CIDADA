# 👥 Usuários de Teste - Plataforma Ciência Cidadã

## 🎯 Acesso ao Sistema

**URL**: http://localhost:8010
**Admin**: http://localhost:8010/admin

---

## 👨‍🏫 PROFESSOR

### Prof. Maria Silva
- **👤 Usuário**: `prof.silva`
- **🔑 Senha**: `prof123`
- **📧 Email**: silva@escola.com
- **🏫 Instituição**: Escola Estadual São Paulo
- **Tipo**: Professor
8733AEF2

**Ações que pode fazer:**
- ✅ Criar turmas
- ✅ Gerenciar grupos
- ✅ Acompanhar projetos
- ✅ Dar feedback
- ✅ Aprovar fases
- ✅ Avaliar projetos

---

## 👨‍🎓 ESTUDANTES

### 1. João Santos
- **👤 Usuário**: `joao.santos`
- **🔑 Senha**: `aluno123`
- **📧 Email**: joao@email.com
- **🏫 Instituição**: Escola Estadual São Paulo
- **Tipo**: Estudante

### 2. Ana Costa
- **👤 Usuário**: `ana.costa`
- **🔑 Senha**: `aluno123`
- **📧 Email**: ana@email.com
- **🏫 Instituição**: Escola Estadual São Paulo
- **Tipo**: Estudante

### 3. Pedro Oliveira
- **👤 Usuário**: `pedro.oliveira`
- **🔑 Senha**: `aluno123`
- **📧 Email**: pedro@email.com
- **🏫 Instituição**: Escola Estadual São Paulo
- **Tipo**: Estudante

### 4. Maria Souza
- **👤 Usuário**: `maria.souza`
- **🔑 Senha**: `aluno123`
- **📧 Email**: maria@email.com
- **🏫 Instituição**: Escola Estadual São Paulo
- **Tipo**: Estudante

**Ações que podem fazer:**
- ✅ Entrar em turmas (via código)
- ✅ Criar/participar de grupos
- ✅ Desenvolver projetos científicos
- ✅ Preencher as 6 fases
- ✅ Adicionar observações
- ✅ Ver feedback do professor
- ✅ Ver avaliação final

---

## 🎮 SIMULAÇÃO SUGERIDA

### Passo 1: Login como Professor
1. Acesse http://localhost:8010/login
2. Login: `prof.silva` / `prof123`
3. Criar uma turma chamada "Turma 2024 - 2º Ano"
4. **ANOTAR O CÓDIGO DA TURMA** (ex: ABC12345)

### Passo 2: Login como Estudante (João)
1. Abrir aba anônima ou outro navegador
2. Criar conta OU fazer login: `joao.santos` / `aluno123`
3. Entrar em turma com o código anotado
4. Criar um grupo "Grupo Água Limpa"
5. Adicionar membros: Ana, Pedro, Maria

### Passo 3: Desenvolver Projeto
1. Como João (ou qualquer membro do grupo)
2. Criar projeto "Qualidade da Água do Rio Local"
3. Preencher Fase 1 (Problema de Pesquisa)
4. Aguardar aprovação

### Passo 4: Professor Aprovar
1. Voltar como `prof.silva`
2. Ver projeto no dashboard
3. Dar feedback na Fase 1
4. Aprovar para avançar

### Passo 5: Continuar o Ciclo
- Estudante preenche Fase 2
- Professor aprova
- Repetir até Fase 6
- Professor avalia com conceito

---

## 🔐 RESUMO DAS SENHAS

**Todas as senhas são simples para testes:**

| Tipo | Senha |
|------|-------|
| **Professor** | `prof123` |
| **Estudantes** | `aluno123` |
| **Admin** (já existia) | `admin123` |

---

## 💡 DICAS

### Para testar em múltiplas contas:
1. **Chrome**: Use aba anônima (Cmd+Shift+N)
2. **Firefox**: Use janela privada
3. **Safari**: Use navegação privada
4. **Ou**: Use diferentes navegadores

### Para resetar testes:
Se quiser recomeçar, você pode:
1. Deletar a turma no admin
2. Ou deletar o banco `db.sqlite3` e recriar tudo

### Grupos sugeridos:
- **Grupo 1**: João (líder) + Ana + Pedro
- **Grupo 2**: Maria (líder) + outros estudantes que criar

---

## 📊 TEMAS DE PROJETO SUGERIDOS

Para tornar a simulação mais realista, use estes temas:

1. **Qualidade da Água**
   - Problema: A água do rio está poluída?
   - Hipótese: Sim, devido à fábrica próxima
   - Metodologia: Coletar amostras, medir pH

2. **Horta Escolar**
   - Problema: Qual o melhor adubo orgânico?
   - Hipótese: Húmus é mais eficiente
   - Metodologia: Plantar em 3 canteiros diferentes

3. **Consumo de Energia**
   - Problema: A escola gasta muita energia?
   - Hipótese: Luzes ficam acesas desnecessariamente
   - Metodologia: Medir consumo por período

4. **Lixo e Reciclagem**
   - Problema: Quanto lixo produzimos?
   - Hipótese: 70% poderia ser reciclado
   - Metodologia: Separar e pesar por 1 semana

---

## ✅ CHECKLIST DE TESTE

Use esta lista para validar o sistema:

- [ ] Professor cria turma e recebe código
- [ ] Estudante entra na turma com código
- [ ] Estudante cria grupo
- [ ] Grupo cria projeto
- [ ] Estudante preenche Fase 1
- [ ] Professor vê projeto pendente
- [ ] Professor dá feedback
- [ ] Professor aprova Fase 1
- [ ] Projeto avança para Fase 2
- [ ] Repetir para todas as 6 fases
- [ ] Na Fase 4, adicionar 3+ observações com fotos
- [ ] Após Fase 6, professor avalia
- [ ] Estudante vê conceito final (A, B, C ou D)

---

## 🎉 Bons Testes!

Agora você tem tudo pronto para simular o fluxo completo da plataforma!

**Divirta-se testando! 🚀**

