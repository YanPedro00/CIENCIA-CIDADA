from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count
from .models import (
    Usuario, Turma, Grupo, Projeto, Observacao, 
    Feedback, Avaliacao, EstudanteTurma, Atividade
)
from .forms import (
    RegistroForm, LoginForm, TurmaForm, GrupoForm,
    ProjetoForm, ObservacaoForm, FeedbackForm, AvaliacaoForm,
    EntrarTurmaForm, Fase1Form, Fase2Form, Fase3Form,
    Fase5Form, Fase6Form, AtividadeForm, AnexosProjetoForm
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


# ============== Atividades da Turma ==============

@login_required
def turma_atividades(request, pk):
    """Lista de atividades de uma turma"""
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
    
    # Listar atividades ativas (estudantes veem apenas ativas)
    if request.user.is_estudante():
        atividades = turma.atividades.filter(ativo=True).order_by('-fixado', '-criado_em')
    else:
        atividades = turma.atividades.all().order_by('-fixado', '-criado_em')
    
    context = {
        'turma': turma,
        'atividades': atividades,
    }
    return render(request, 'core/turma_atividades.html', context)


@login_required
@user_passes_test(is_professor)
def atividade_criar(request, turma_pk):
    """Professor cria atividade para turma"""
    turma = get_object_or_404(Turma, pk=turma_pk, professor=request.user)
    
    if request.method == 'POST':
        form = AtividadeForm(request.POST, request.FILES)
        if form.is_valid():
            atividade = form.save(commit=False)
            atividade.turma = turma
            atividade.autor = request.user
            atividade.save()
            messages.success(request, f'Atividade "{atividade.titulo}" criada com sucesso!')
            return redirect('turma_atividades', pk=turma.pk)
    else:
        form = AtividadeForm()
    
    context = {
        'form': form,
        'turma': turma,
        'titulo': 'Criar Atividade',
    }
    return render(request, 'core/atividade_form.html', context)


@login_required
def atividade_detalhe(request, pk):
    """Visualizar detalhes de uma atividade"""
    atividade = get_object_or_404(Atividade, pk=pk)
    turma = atividade.turma
    
    # Verificar permissão
    if request.user.is_professor():
        if turma.professor != request.user:
            messages.error(request, 'Você não tem permissão para acessar esta atividade.')
            return redirect('dashboard')
    else:
        # Verificar se o estudante está na turma
        if not EstudanteTurma.objects.filter(turma=turma, estudante=request.user).exists():
            messages.error(request, 'Você não está inscrito nesta turma.')
            return redirect('dashboard')
        # Estudantes só veem atividades ativas
        if not atividade.ativo:
            messages.error(request, 'Esta atividade não está disponível.')
            return redirect('dashboard')
    
    context = {
        'atividade': atividade,
        'turma': turma,
    }
    return render(request, 'core/atividade_detalhe.html', context)


@login_required
@user_passes_test(is_professor)
def atividade_editar(request, pk):
    """Professor edita atividade"""
    atividade = get_object_or_404(Atividade, pk=pk)
    turma = atividade.turma
    
    # Verificar se é o professor da turma
    if turma.professor != request.user:
        messages.error(request, 'Você não tem permissão para editar esta atividade.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = AtividadeForm(request.POST, request.FILES, instance=atividade)
        if form.is_valid():
            form.save()
            messages.success(request, 'Atividade atualizada com sucesso!')
            return redirect('atividade_detalhe', pk=atividade.pk)
    else:
        form = AtividadeForm(instance=atividade)
    
    context = {
        'form': form,
        'atividade': atividade,
        'turma': turma,
        'titulo': 'Editar Atividade',
    }
    return render(request, 'core/atividade_form.html', context)


@login_required
@user_passes_test(is_professor)
def atividade_excluir(request, pk):
    """Professor exclui atividade"""
    atividade = get_object_or_404(Atividade, pk=pk)
    turma = atividade.turma
    
    # Verificar se é o professor da turma
    if turma.professor != request.user:
        messages.error(request, 'Você não tem permissão para excluir esta atividade.')
        return redirect('dashboard')
    
    turma_pk = turma.pk
    if request.method == 'POST':
        atividade.delete()
        messages.success(request, 'Atividade excluída com sucesso.')
        return redirect('turma_atividades', pk=turma_pk)
    
    context = {
        'atividade': atividade,
        'turma': turma,
    }
    return render(request, 'core/atividade_confirmar_exclusao.html', context)


# ============== Anexos do Projeto ==============

@login_required
def projeto_anexos(request, slug):
    """Gerenciar anexos do projeto (relatório, apresentação, fotos)"""
    projeto = get_object_or_404(Projeto, slug=slug)
    
    # Verificar permissão (apenas membros do grupo ou professor)
    if request.user.is_estudante():
        if request.user not in projeto.grupo.membros.all():
            messages.error(request, 'Você não tem permissão para editar este projeto.')
            return redirect('projeto_detalhe', slug=slug)
    elif request.user.is_professor():
        if projeto.grupo.turma.professor != request.user:
            messages.error(request, 'Você não tem permissão para acessar este projeto.')
            return redirect('dashboard')
    
    if request.method == 'POST':
        form = AnexosProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Anexos atualizados com sucesso!')
            return redirect('projeto_detalhe', slug=slug)
    else:
        form = AnexosProjetoForm(instance=projeto)
    
    context = {
        'form': form,
        'projeto': projeto,
        'titulo': 'Anexar Documentos e Fotos',
    }
    return render(request, 'core/projeto_anexos_form.html', context)


# ============== Exportação de Relatórios ==============

@login_required
def exportar_projeto_pdf(request, slug):
    """Exportar projeto completo em PDF"""
    from django.http import HttpResponse
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
    import io
    
    projeto = get_object_or_404(Projeto, slug=slug)
    
    # Verificar permissão
    if request.user.is_professor():
        if projeto.grupo.turma.professor != request.user:
            messages.error(request, 'Você não tem permissão.')
            return redirect('dashboard')
    else:
        if request.user not in projeto.grupo.membros.all():
            messages.error(request, 'Você não tem permissão.')
            return redirect('dashboard')
    
    # Criar PDF
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    # Container para elementos
    elements = []
    
    # Estilos
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=30,
        alignment=TA_CENTER,
    )
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=12,
        spaceBefore=12,
    )
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['BodyText'],
        fontSize=11,
        alignment=TA_JUSTIFY,
    )
    
    # Título
    elements.append(Paragraph(projeto.titulo, title_style))
    elements.append(Spacer(1, 12))
    
    # Informações básicas
    info_data = [
        ['Grupo:', projeto.grupo.nome],
        ['Turma:', projeto.grupo.turma.nome],
        ['Área da Ciência:', projeto.get_area_ciencia_display()],
        ['Status:', projeto.get_status_display()],
        ['Progresso:', f"{projeto.get_progresso_percentual():.0f}%"],
    ]
    info_table = Table(info_data, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#ecf0f1')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2c3e50')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    elements.append(info_table)
    elements.append(Spacer(1, 20))
    
    # Descrição
    elements.append(Paragraph("Descrição do Projeto", heading_style))
    elements.append(Paragraph(projeto.descricao_breve or "Não informado", normal_style))
    elements.append(Spacer(1, 20))
    
    # Fase 1
    if projeto.fase1_pergunta:
        elements.append(Paragraph("FASE 1: PROBLEMA DE PESQUISA", heading_style))
        elements.append(Paragraph(f"<b>Pergunta:</b> {projeto.fase1_pergunta}", normal_style))
        elements.append(Spacer(1, 6))
        if projeto.fase1_justificativa:
            elements.append(Paragraph(f"<b>Justificativa:</b> {projeto.fase1_justificativa}", normal_style))
            elements.append(Spacer(1, 6))
        if projeto.fase1_objetivos:
            elements.append(Paragraph(f"<b>Objetivos:</b> {projeto.fase1_objetivos}", normal_style))
        elements.append(Spacer(1, 12))
    
    # Fase 2
    if projeto.fase2_hipotese_principal:
        elements.append(Paragraph("FASE 2: HIPÓTESE", heading_style))
        elements.append(Paragraph(f"<b>Hipótese:</b> {projeto.fase2_hipotese_principal}", normal_style))
        elements.append(Spacer(1, 6))
        if projeto.fase2_fundamentacao:
            elements.append(Paragraph(f"<b>Fundamentação:</b> {projeto.fase2_fundamentacao}", normal_style))
        elements.append(Spacer(1, 12))
    
    # Fase 3
    if projeto.fase3_metodo_coleta:
        elements.append(Paragraph("FASE 3: METODOLOGIA", heading_style))
        elements.append(Paragraph(f"<b>Método:</b> {projeto.fase3_metodo_coleta}", normal_style))
        elements.append(Spacer(1, 6))
        if projeto.fase3_materiais:
            elements.append(Paragraph(f"<b>Materiais:</b> {projeto.fase3_materiais}", normal_style))
            elements.append(Spacer(1, 6))
        if projeto.fase3_local:
            elements.append(Paragraph(f"<b>Local:</b> {projeto.fase3_local}", normal_style))
        elements.append(Spacer(1, 12))
    
    # Fase 4 - Observações
    observacoes = projeto.observacoes.all()
    if observacoes.exists():
        elements.append(Paragraph("FASE 4: COLETA DE DADOS", heading_style))
        elements.append(Paragraph(f"Total de observações coletadas: {observacoes.count()}", normal_style))
        elements.append(Spacer(1, 6))
        for obs in observacoes[:10]:  # Limitar a 10 observações
            elements.append(Paragraph(f"• <b>{obs.titulo}</b>: {obs.descricao[:200]}...", normal_style))
        if observacoes.count() > 10:
            elements.append(Paragraph(f"... e mais {observacoes.count() - 10} observações.", normal_style))
        elements.append(Spacer(1, 12))
    
    # Fase 5
    if projeto.fase5_interpretacao:
        elements.append(Paragraph("FASE 5: ANÁLISE DE DADOS", heading_style))
        elements.append(Paragraph(f"<b>Interpretação:</b> {projeto.fase5_interpretacao}", normal_style))
        elements.append(Spacer(1, 6))
        if projeto.fase5_discussao:
            elements.append(Paragraph(f"<b>Discussão:</b> {projeto.fase5_discussao}", normal_style))
        elements.append(Spacer(1, 12))
    
    # Fase 6
    if projeto.fase6_conclusao:
        elements.append(Paragraph("FASE 6: CONCLUSÃO", heading_style))
        if projeto.fase6_hipotese_confirmada:
            elements.append(Paragraph(f"<b>Hipótese:</b> {projeto.get_fase6_hipotese_confirmada_display()}", normal_style))
            elements.append(Spacer(1, 6))
        elements.append(Paragraph(f"<b>Conclusão:</b> {projeto.fase6_conclusao}", normal_style))
        elements.append(Spacer(1, 6))
        if projeto.fase6_aprendizados:
            elements.append(Paragraph(f"<b>Aprendizados:</b> {projeto.fase6_aprendizados}", normal_style))
        elements.append(Spacer(1, 12))
    
    # Avaliação (se existir)
    try:
        avaliacao = projeto.avaliacao
        elements.append(PageBreak())
        elements.append(Paragraph("AVALIAÇÃO DO PROFESSOR", heading_style))
        elements.append(Paragraph(f"<b>Conceito:</b> {avaliacao.get_conceito_display()}", normal_style))
        elements.append(Paragraph(f"<b>Média:</b> {avaliacao.media_notas():.1f}", normal_style))
        elements.append(Spacer(1, 12))
        if avaliacao.comentarios:
            elements.append(Paragraph(f"<b>Comentários:</b> {avaliacao.comentarios}", normal_style))
    except Avaliacao.DoesNotExist:
        pass
    
    # Build PDF
    doc.build(elements)
    
    # Retornar PDF
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="projeto_{projeto.slug}.pdf"'
    
    return response


@login_required
def exportar_observacoes_csv(request, slug):
    """Exportar observações do projeto em CSV"""
    import csv
    from django.http import HttpResponse
    
    projeto = get_object_or_404(Projeto, slug=slug)
    
    # Verificar permissão
    if request.user.is_professor():
        if projeto.grupo.turma.professor != request.user:
            messages.error(request, 'Você não tem permissão.')
            return redirect('dashboard')
    else:
        if request.user not in projeto.grupo.membros.all():
            messages.error(request, 'Você não tem permissão.')
            return redirect('dashboard')
    
    # Criar CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="observacoes_{projeto.slug}.csv"'
    response.write('\ufeff'.encode('utf8'))  # BOM para Excel reconhecer UTF-8
    
    writer = csv.writer(response, delimiter=';')
    writer.writerow(['Título', 'Descrição', 'Coletado por', 'Data e Hora', 'Local', 'Latitude', 'Longitude'])
    
    for obs in projeto.observacoes.all():
        writer.writerow([
            obs.titulo,
            obs.descricao,
            obs.usuario.get_full_name(),
            obs.data_hora_coleta.strftime('%d/%m/%Y %H:%M'),
            obs.local_descricao or '',
            obs.latitude or '',
            obs.longitude or '',
        ])
    
    return response
