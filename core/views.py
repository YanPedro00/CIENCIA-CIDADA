from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count
from .models import (
    Usuario, Turma, Grupo, Projeto, Observacao, 
    Feedback, Avaliacao, EstudanteTurma
)
from .forms import (
    RegistroForm, LoginForm, TurmaForm, GrupoForm,
    ProjetoForm, ObservacaoForm, FeedbackForm, AvaliacaoForm,
    EntrarTurmaForm, Fase1Form, Fase2Form, Fase3Form,
    Fase5Form, Fase6Form
)


# ============== Helpers ==============

def is_professor(user):
    return user.is_authenticated and user.tipo == 'professor'

def is_estudante(user):
    return user.is_authenticated and user.tipo == 'estudante'


# ============== Páginas Públicas ==============

def home(request):
    """Página inicial pública"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    context = {
        'total_projetos': Projeto.objects.filter(status='concluido').count(),
        'total_estudantes': Usuario.objects.filter(tipo='estudante').count(),
        'projetos_destaque': Projeto.objects.filter(
            status='concluido'
        ).select_related('grupo', 'grupo__turma').order_by('-concluido_em')[:3]
    }
    return render(request, 'core/home.html', context)


# ============== Autenticação ==============

def login_view(request):
    """View de login"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo(a), {user.get_full_name() or user.username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()
    
    return render(request, 'core/login.html', {'form': form})


def registro_view(request):
    """View de registro de novo usuário"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('dashboard')
    else:
        form = RegistroForm()
    
    return render(request, 'core/registro.html', {'form': form})


# ============== Dashboard ==============

@login_required
def dashboard(request):
    """Dashboard principal - diferente para professor e estudante"""
    user = request.user
    
    if user.is_professor():
        # Dashboard do Professor
        turmas = Turma.objects.filter(professor=user).annotate(
            num_estudantes=Count('estudantes'),
            num_grupos=Count('grupos')
        ).order_by('-criada_em')
        
        # Projetos aguardando aprovação
        projetos_pendentes = Projeto.objects.filter(
            grupo__turma__professor=user,
            status='aguardando_aprovacao'
        ).select_related('grupo', 'grupo__turma')[:5]
        
        context = {
            'turmas': turmas,
            'projetos_pendentes': projetos_pendentes,
            'total_turmas': turmas.count(),
        }
        return render(request, 'core/dashboard_professor.html', context)
    
    else:
        # Dashboard do Estudante
        # Turmas do estudante
        turmas_estudante = EstudanteTurma.objects.filter(
            estudante=user
        ).select_related('turma', 'turma__professor')
        
        # Grupos do estudante
        grupos = user.grupos.all().select_related('turma').prefetch_related('membros')
        
        # Projetos dos grupos do estudante
        projetos = Projeto.objects.filter(
            grupo__in=grupos
        ).select_related('grupo', 'grupo__turma')
        
        context = {
            'turmas': turmas_estudante,
            'grupos': grupos,
            'projetos': projetos,
        }
        return render(request, 'core/dashboard_estudante.html', context)


# ============== Turmas ==============

@login_required
@user_passes_test(is_professor)
def turmas_lista(request):
    """Lista de turmas do professor"""
    turmas = Turma.objects.filter(
        professor=request.user
    ).annotate(
        num_estudantes=Count('estudantes'),
        num_grupos=Count('grupos')
    ).order_by('-criada_em')
    
    return render(request, 'core/turmas_lista.html', {'turmas': turmas})


@login_required
@user_passes_test(is_professor)
def turma_criar(request):
    """Criar nova turma (somente professor)"""
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            turma = form.save(commit=False)
            turma.professor = request.user
            turma.save()
            messages.success(request, f'Turma "{turma.nome}" criada com sucesso! Código: {turma.codigo_acesso}')
            return redirect('turma_detalhe', pk=turma.pk)
    else:
        form = TurmaForm()
    
    return render(request, 'core/turma_form.html', {'form': form, 'titulo': 'Criar Turma'})


@login_required
def turma_detalhe(request, pk):
    """Detalhes da turma"""
    turma = get_object_or_404(Turma, pk=pk)
    
    # Verificar permissão
    if request.user.is_professor():
        if turma.professor != request.user:
            messages.error(request, 'Você não tem permissão para acessar esta turma.')
            return redirect('dashboard')
    else:
        # Verificar se o estudante está na turma
        if not EstudanteTurma.objects.filter(turma=turma, estudante=request.user).exists():
            messages.error(request, 'Você não está inscrito nesta turma.')
            return redirect('dashboard')
    
    estudantes = EstudanteTurma.objects.filter(turma=turma).select_related('estudante')
    grupos = turma.grupos.all().prefetch_related('membros')
    
    context = {
        'turma': turma,
        'estudantes': estudantes,
        'grupos': grupos,
    }
    return render(request, 'core/turma_detalhe.html', context)


@login_required
@user_passes_test(is_professor)
def turma_editar(request, pk):
    """Editar turma"""
    turma = get_object_or_404(Turma, pk=pk, professor=request.user)
    
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Turma atualizada com sucesso!')
            return redirect('turma_detalhe', pk=turma.pk)
    else:
        form = TurmaForm(instance=turma)
    
    return render(request, 'core/turma_form.html', {'form': form, 'titulo': 'Editar Turma', 'turma': turma})


@login_required
@user_passes_test(is_estudante)
def turma_entrar(request):
    """Estudante entra em uma turma usando código"""
    if request.method == 'POST':
        form = EntrarTurmaForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo_acesso'].upper()
            try:
                turma = Turma.objects.get(codigo_acesso=codigo, ativa=True)
                
                # Verificar se já está na turma
                if EstudanteTurma.objects.filter(turma=turma, estudante=request.user).exists():
                    messages.warning(request, 'Você já está inscrito nesta turma.')
                else:
                    EstudanteTurma.objects.create(turma=turma, estudante=request.user)
                    messages.success(request, f'Você entrou na turma "{turma.nome}" com sucesso!')
                
                return redirect('turma_detalhe', pk=turma.pk)
            except Turma.DoesNotExist:
                messages.error(request, 'Código inválido ou turma inativa.')
    else:
        form = EntrarTurmaForm()
    
    return render(request, 'core/turma_entrar.html', {'form': form})


# ============== Grupos ==============

@login_required
def grupo_criar(request, turma_pk):
    """Criar grupo em uma turma"""
    turma = get_object_or_404(Turma, pk=turma_pk)
    
    # Professor pode criar qualquer grupo
    # Estudante só pode criar se estiver na turma
    if request.user.is_estudante():
        if not EstudanteTurma.objects.filter(turma=turma, estudante=request.user).exists():
            messages.error(request, 'Você não está inscrito nesta turma.')
            return redirect('dashboard')
    
    # Verificar se pode criar mais grupos
    if not turma.pode_criar_grupo():
        messages.error(request, f'Esta turma já atingiu o limite de {turma.max_grupos} grupos.')
        return redirect('turma_detalhe', pk=turma.pk)
    
    if request.method == 'POST':
        form = GrupoForm(request.POST, turma=turma)
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.turma = turma
            grupo.save()
            form.save_m2m()
            
            # Se estudante criou, adicionar ele ao grupo
            if request.user.is_estudante() and request.user not in grupo.membros.all():
                grupo.membros.add(request.user)
                if not grupo.lider:
                    grupo.lider = request.user
                    grupo.save()
            
            messages.success(request, f'Grupo "{grupo.nome}" criado com sucesso!')
            return redirect('grupo_detalhe', pk=grupo.pk)
    else:
        form = GrupoForm(turma=turma)
    
    return render(request, 'core/grupo_form.html', {
        'form': form,
        'titulo': 'Criar Grupo',
        'turma': turma
    })


@login_required
def grupo_detalhe(request, pk):
    """Detalhes do grupo"""
    grupo = get_object_or_404(Grupo, pk=pk)
    
    # Verificar permissão
    if request.user.is_professor():
        if grupo.turma.professor != request.user:
            messages.error(request, 'Você não tem permissão para acessar este grupo.')
            return redirect('dashboard')
    else:
        if request.user not in grupo.membros.all():
            messages.error(request, 'Você não é membro deste grupo.')
            return redirect('dashboard')
    
    try:
        projeto = grupo.projeto
    except Projeto.DoesNotExist:
        projeto = None
    
    context = {
        'grupo': grupo,
        'projeto': projeto,
    }
    return render(request, 'core/grupo_detalhe.html', context)


@login_required
def grupo_editar(request, pk):
    """Editar grupo"""
    grupo = get_object_or_404(Grupo, pk=pk)
    
    # Verificar permissão
    if request.user.is_professor():
        if grupo.turma.professor != request.user:
            messages.error(request, 'Você não tem permissão para editar este grupo.')
            return redirect('dashboard')
    else:
        if grupo.lider != request.user:
            messages.error(request, 'Apenas o líder pode editar o grupo.')
            return redirect('grupo_detalhe', pk=grupo.pk)
    
    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=grupo, turma=grupo.turma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Grupo atualizado com sucesso!')
            return redirect('grupo_detalhe', pk=grupo.pk)
    else:
        form = GrupoForm(instance=grupo, turma=grupo.turma)
    
    return render(request, 'core/grupo_form.html', {
        'form': form,
        'titulo': 'Editar Grupo',
        'grupo': grupo,
        'turma': grupo.turma
    })


@login_required
@user_passes_test(is_estudante)
def grupo_entrar(request, turma_pk, grupo_pk):
    """Estudante entra em um grupo"""
    grupo = get_object_or_404(Grupo, pk=grupo_pk, turma_id=turma_pk)
    
    # Verificar se está na turma
    if not EstudanteTurma.objects.filter(turma=grupo.turma, estudante=request.user).exists():
        messages.error(request, 'Você precisa estar inscrito na turma primeiro.')
        return redirect('dashboard')
    
    # Verificar se já está em algum grupo desta turma
    if request.user.grupos.filter(turma=grupo.turma).exists():
        messages.warning(request, 'Você já está em um grupo desta turma.')
        return redirect('dashboard')
    
    # Verificar se o grupo está cheio
    if not grupo.pode_adicionar_membro():
        messages.error(request, 'Este grupo já está cheio.')
        return redirect('turma_detalhe', pk=turma_pk)
    
    grupo.membros.add(request.user)
    messages.success(request, f'Você entrou no grupo "{grupo.nome}"!')
    return redirect('grupo_detalhe', pk=grupo.pk)


# ============== Projetos ==============

@login_required
def projetos_lista(request):
    """Lista de projetos"""
    if request.user.is_professor():
        projetos = Projeto.objects.filter(
            grupo__turma__professor=request.user
        ).select_related('grupo', 'grupo__turma').order_by('-criado_em')
    else:
        projetos = Projeto.objects.filter(
            grupo__membros=request.user
        ).select_related('grupo', 'grupo__turma').order_by('-criado_em')
    
    return render(request, 'core/projetos_lista.html', {'projetos': projetos})


@login_required
def projeto_criar(request, grupo_pk):
    """Criar projeto para um grupo"""
    grupo = get_object_or_404(Grupo, pk=grupo_pk)
    
    # Verificar se é membro do grupo
    if request.user.is_estudante() and request.user not in grupo.membros.all():
        messages.error(request, 'Você não é membro deste grupo.')
        return redirect('dashboard')
    
    # Verificar se já existe projeto
    if hasattr(grupo, 'projeto'):
        messages.warning(request, 'Este grupo já possui um projeto.')
        return redirect('projeto_detalhe', slug=grupo.projeto.slug)
    
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.grupo = grupo
            projeto.status = 'em_andamento'
            projeto.save()
            messages.success(request, f'Projeto "{projeto.titulo}" criado! Comece pela Fase 1.')
            return redirect('projeto_fase_editar', slug=projeto.slug, fase=1)
    else:
        form = ProjetoForm()
    
    return render(request, 'core/projeto_form.html', {
        'form': form,
        'titulo': 'Criar Projeto',
        'grupo': grupo
    })


@login_required
def projeto_detalhe(request, slug):
    """Detalhes do projeto"""
    projeto = get_object_or_404(Projeto, slug=slug)
    
    # Verificar permissão
    if request.user.is_professor():
        if projeto.grupo.turma.professor != request.user:
            messages.error(request, 'Você não tem permissão para acessar este projeto.')
            return redirect('dashboard')
    else:
        if request.user not in projeto.grupo.membros.all():
            messages.error(request, 'Você não tem permissão para acessar este projeto.')
            return redirect('dashboard')
    
    observacoes = projeto.observacoes.all().select_related('usuario').order_by('-data_hora_coleta')
    feedbacks = projeto.feedbacks.all().select_related('professor').order_by('fase', '-criado_em')
    
    try:
        avaliacao = projeto.avaliacao
    except Avaliacao.DoesNotExist:
        avaliacao = None
    
    context = {
        'projeto': projeto,
        'observacoes': observacoes,
        'feedbacks': feedbacks,
        'avaliacao': avaliacao,
    }
    return render(request, 'core/projeto_detalhe.html', context)


@login_required
def projeto_editar(request, slug):
    """Editar informações básicas do projeto"""
    projeto = get_object_or_404(Projeto, slug=slug)
    
    # Apenas membros do grupo podem editar
    if request.user.is_estudante() and request.user not in projeto.grupo.membros.all():
        messages.error(request, 'Você não tem permissão para editar este projeto.')
        return redirect('projeto_detalhe', slug=slug)
    
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado!')
            return redirect('projeto_detalhe', slug=projeto.slug)
    else:
        form = ProjetoForm(instance=projeto)
    
    return render(request, 'core/projeto_form.html', {
        'form': form,
        'titulo': 'Editar Projeto',
        'projeto': projeto
    })


@login_required
def projeto_fase_editar(request, slug, fase):
    """Editar uma fase específica do projeto"""
    projeto = get_object_or_404(Projeto, slug=slug)
    
    # Verificar permissão
    if request.user.is_estudante() and request.user not in projeto.grupo.membros.all():
        messages.error(request, 'Você não tem permissão para editar este projeto.')
        return redirect('dashboard')
    
    # Selecionar formulário correto para a fase
    forms_map = {
        1: Fase1Form,
        2: Fase2Form,
        3: Fase3Form,
        # Fase 4 não tem formulário (observações)
        5: Fase5Form,
        6: Fase6Form,
    }
    
    if fase not in forms_map and fase != 4:
        messages.error(request, 'Fase inválida.')
        return redirect('projeto_detalhe', slug=slug)
    
    # Fase 4 é especial (observações)
    if fase == 4:
        return redirect('projeto_detalhe', slug=slug)
    
    FormClass = forms_map[fase]
    
    if request.method == 'POST':
        form = FormClass(request.POST, instance=projeto)
        if form.is_valid():
            projeto = form.save()
            messages.success(request, f'Fase {fase} salva! Aguarde aprovação do professor para avançar.')
            return redirect('projeto_detalhe', slug=slug)
    else:
        form = FormClass(instance=projeto)
    
    context = {
        'form': form,
        'projeto': projeto,
        'fase': fase,
        'titulo': dict(Projeto.FASES)[fase],
    }
    return render(request, 'core/projeto_fase_form.html', context)


# ============== Observações (Fase 4) ==============

@login_required
def observacao_criar(request, slug):
    """Adicionar observação ao projeto (Fase 4)"""
    projeto = get_object_or_404(Projeto, slug=slug)
    
    # Verificar se é membro do grupo
    if request.user.is_estudante() and request.user not in projeto.grupo.membros.all():
        messages.error(request, 'Você não tem permissão.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = ObservacaoForm(request.POST, request.FILES)
        if form.is_valid():
            observacao = form.save(commit=False)
            observacao.projeto = projeto
            observacao.usuario = request.user
            observacao.save()
            messages.success(request, 'Observação adicionada com sucesso!')
            return redirect('projeto_detalhe', slug=slug)
    else:
        form = ObservacaoForm()
    
    return render(request, 'core/observacao_form.html', {
        'form': form,
        'projeto': projeto,
        'titulo': 'Adicionar Observação'
    })


@login_required
def observacao_editar(request, pk):
    """Editar observação"""
    observacao = get_object_or_404(Observacao, pk=pk)
    
    # Apenas quem criou ou professor pode editar
    if request.user != observacao.usuario and not request.user.is_professor():
        messages.error(request, 'Você não tem permissão para editar esta observação.')
        return redirect('projeto_detalhe', slug=observacao.projeto.slug)
    
    if request.method == 'POST':
        form = ObservacaoForm(request.POST, request.FILES, instance=observacao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Observação atualizada!')
            return redirect('projeto_detalhe', slug=observacao.projeto.slug)
    else:
        form = ObservacaoForm(instance=observacao)
    
    return render(request, 'core/observacao_form.html', {
        'form': form,
        'observacao': observacao,
        'projeto': observacao.projeto,
        'titulo': 'Editar Observação'
    })


@login_required
def observacao_excluir(request, pk):
    """Excluir observação"""
    observacao = get_object_or_404(Observacao, pk=pk)
    
    # Apenas quem criou pode excluir
    if request.user != observacao.usuario:
        messages.error(request, 'Você não tem permissão para excluir esta observação.')
        return redirect('projeto_detalhe', slug=observacao.projeto.slug)
    
    slug = observacao.projeto.slug
    if request.method == 'POST':
        observacao.delete()
        messages.success(request, 'Observação excluída.')
        return redirect('projeto_detalhe', slug=slug)
    
    return render(request, 'core/observacao_confirmar_exclusao.html', {
        'observacao': observacao
    })


# ============== Feedback e Aprovação (Professor) ==============

@login_required
@user_passes_test(is_professor)
def feedback_criar(request, slug, fase):
    """Professor dá feedback em uma fase"""
    projeto = get_object_or_404(Projeto, slug=slug)
    
    # Verificar se é o professor da turma
    if projeto.grupo.turma.professor != request.user:
        messages.error(request, 'Você não tem permissão.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.projeto = projeto
            feedback.fase = fase
            feedback.professor = request.user
            feedback.save()
            messages.success(request, 'Feedback enviado!')
            return redirect('projeto_detalhe', slug=slug)
    else:
        form = FeedbackForm()
    
    context = {
        'form': form,
        'projeto': projeto,
        'fase': fase,
        'titulo': f'Feedback - {dict(Projeto.FASES)[fase]}'
    }
    return render(request, 'core/feedback_form.html', context)


@login_required
@user_passes_test(is_professor)
def aprovar_fase(request, slug, fase):
    """Professor aprova uma fase do projeto"""
    projeto = get_object_or_404(Projeto, slug=slug)
    
    # Verificar se é o professor da turma
    if projeto.grupo.turma.professor != request.user:
        messages.error(request, 'Você não tem permissão.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        # Aprovar a fase correspondente
        if fase == 1:
            projeto.fase1_aprovada = True
            projeto.fase1_aprovada_em = timezone.now()
        elif fase == 2:
            projeto.fase2_aprovada = True
            projeto.fase2_aprovada_em = timezone.now()
        elif fase == 3:
            projeto.fase3_aprovada = True
            projeto.fase3_aprovada_em = timezone.now()
        elif fase == 4:
            projeto.fase4_aprovada = True
            projeto.fase4_aprovada_em = timezone.now()
        elif fase == 5:
            projeto.fase5_aprovada = True
            projeto.fase5_aprovada_em = timezone.now()
        elif fase == 6:
            projeto.fase6_aprovada = True
            projeto.fase6_aprovada_em = timezone.now()
            projeto.status = 'concluido'
            projeto.concluido_em = timezone.now()
        
        projeto.save()
        
        # Avançar automaticamente para próxima fase se possível
        if fase < 6 and projeto.pode_avancar_fase():
            projeto.avancar_fase()
        
        messages.success(request, f'Fase {fase} aprovada! O grupo pode avançar.')
        return redirect('projeto_detalhe', slug=slug)
    
    context = {
        'projeto': projeto,
        'fase': fase,
    }
    return render(request, 'core/aprovar_fase_confirmar.html', context)


# ============== Avaliação (Professor) ==============

@login_required
@user_passes_test(is_professor)
def projeto_avaliar(request, slug):
    """Professor avalia o projeto finalizado"""
    projeto = get_object_or_404(Projeto, slug=slug)
    
    # Verificar se é o professor da turma
    if projeto.grupo.turma.professor != request.user:
        messages.error(request, 'Você não tem permissão.')
        return redirect('dashboard')
    
    # Verificar se projeto está concluído
    if projeto.status != 'concluido':
        messages.warning(request, 'O projeto precisa estar concluído para ser avaliado.')
        return redirect('projeto_detalhe', slug=slug)
    
    # Verificar se já existe avaliação
    try:
        avaliacao = projeto.avaliacao
        instance = avaliacao
    except Avaliacao.DoesNotExist:
        instance = None
    
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=instance)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            if not instance:
                avaliacao.projeto = projeto
                avaliacao.professor = request.user
            avaliacao.save()
            messages.success(request, 'Avaliação salva com sucesso!')
            return redirect('projeto_detalhe', slug=slug)
    else:
        form = AvaliacaoForm(instance=instance)
    
    context = {
        'form': form,
        'projeto': projeto,
        'titulo': 'Avaliar Projeto'
    }
    return render(request, 'core/avaliacao_form.html', context)
