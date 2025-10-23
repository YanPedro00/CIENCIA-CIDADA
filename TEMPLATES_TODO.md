# Templates Restantes para Criar

Os templates principais já foram criados. Esta lista contém os templates adicionais necessários para completar todas as funcionalidades.

## ✅ Templates Já Criados

- ✅ `base.html` - Template base
- ✅ `core/home.html` - Página inicial
- ✅ `core/login.html` - Login
- ✅ `core/registro.html` - Cadastro
- ✅ `core/dashboard_professor.html` - Dashboard do professor
- ✅ `core/dashboard_estudante.html` - Dashboard do estudante
- ✅ `core/turma_form.html` - Criar/editar turma
- ✅ `core/turma_entrar.html` - Estudante entra em turma
- ✅ `core/projetos_lista.html` - Lista de projetos
- ✅ `core/projeto_detalhe.html` - Detalhes do projeto (todas as 6 fases)
- ✅ `core/projeto_fase_form.html` - Editar fases do projeto

## 📝 Templates a Criar (Opcionais/Complementares)

### Turmas
```
core/templates/core/turma_detalhe.html
```
- Mostrar detalhes da turma
- Lista de estudantes
- Lista de grupos
- Projetos dos grupos

### Grupos
```
core/templates/core/grupo_form.html
core/templates/core/grupo_detalhe.html
```
- Criar/editar grupo
- Ver detalhes do grupo e membros

### Projeto
```
core/templates/core/projeto_form.html
```
- Criar projeto (informações básicas)

### Observações (Fase 4)
```
core/templates/core/observacao_form.html
core/templates/core/observacao_confirmar_exclusao.html
```
- Adicionar/editar observação
- Confirmar exclusão

### Feedback (Professor)
```
core/templates/core/feedback_form.html
core/templates/core/aprovar_fase_confirmar.html
```
- Professor dá feedback
- Confirmar aprovação de fase

### Avaliação (Professor)
```
core/templates/core/avaliacao_form.html
```
- Professor avalia projeto final

## 🎨 Estrutura Padrão para Novos Templates

Todos os templates devem seguir esta estrutura:

```html
{% extends 'base.html' %}

{% block title %}Título da Página - Ciência Cidadã{% endblock %}

{% block content %}
<div class="container">
    <!-- Breadcrumb (opcional) -->
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="{% url 'home' %}">Home</a></li>
            <li class="breadcrumb-item active">Página Atual</li>
        </ol>
    </nav>

    <!-- Conteúdo principal -->
    <div class="card">
        <div class="card-header">
            <h4>Título do Card</h4>
        </div>
        <div class="card-body">
            <!-- Conteúdo -->
        </div>
    </div>
</div>
{% endblock %}
```

## 🚀 Como Criar Templates Rapidamente

### 1. Template de Formulário Padrão
Use como base o `turma_form.html` e adapte os campos.

### 2. Template de Listagem
Use como base o `projetos_lista.html`.

### 3. Template de Detalhes
Use como base o `projeto_detalhe.html`.

### 4. Template de Confirmação
```html
{% extends 'base.html' %}

{% block content %}
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header bg-warning">
                    <h5>Confirmar Ação</h5>
                </div>
                <div class="card-body">
                    <p>Tem certeza que deseja realizar esta ação?</p>
                    <form method="post">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-danger">Confirmar</button>
                        <a href="..." class="btn btn-secondary">Cancelar</a>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## 📚 Classes Bootstrap Úteis

- **Cards**: `card`, `card-header`, `card-body`, `card-footer`
- **Botões**: `btn btn-primary`, `btn btn-success`, `btn btn-warning`, `btn btn-danger`
- **Badges**: `badge bg-primary`, `badge bg-success`, `badge bg-warning`
- **Alertas**: `alert alert-info`, `alert alert-success`, `alert alert-warning`
- **Formulários**: `form-control`, `form-select`, `form-label`
- **Ícones**: Use Bootstrap Icons com `<i class="bi bi-nome-icone"></i>`

## 🎯 Prioridades

1. **Alta Prioridade**: Templates de formulário simples que seguem o padrão já estabelecido
2. **Média Prioridade**: Templates de detalhes e listagem
3. **Baixa Prioridade**: Templates de confirmação (podem usar confirmação JavaScript)

## 💡 Dica

A maioria dos templates faltantes são variações dos templates já criados. Use copiar e colar, depois adapte!

