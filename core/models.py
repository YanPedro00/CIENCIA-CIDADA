from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.utils.text import slugify
import uuid
from .storage import DocumentStorage


class Usuario(AbstractUser):
    """
    Modelo customizado de usuário que estende AbstractUser.
    Pode ser Professor ou Estudante.
    """
    TIPO_USUARIO = (
        ('professor', 'Professor'),
        ('estudante', 'Estudante'),
    )
    
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_USUARIO,
        default='estudante',
        verbose_name='Tipo de Usuário'
    )
    instituicao = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Instituição de Ensino'
    )
    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Telefone'
    )
    foto_perfil = models.ImageField(
        upload_to='perfis/',
        blank=True,
        null=True,
        verbose_name='Foto de Perfil'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['first_name', 'last_name']
    
    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_tipo_display()})"
    
    def is_professor(self):
        return self.tipo == 'professor'
    
    def is_estudante(self):
        return self.tipo == 'estudante'


class Turma(models.Model):
    """
    Turma criada por um professor onde estudantes se inscrevem.
    """
    nome = models.CharField(max_length=200, verbose_name='Nome da Turma')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    professor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='turmas_criadas',
        limit_choices_to={'tipo': 'professor'},
        verbose_name='Professor Responsável'
    )
    codigo_acesso = models.CharField(
        max_length=10,
        unique=True,
        editable=False,
        verbose_name='Código de Acesso'
    )
    ano_semestre = models.CharField(
        max_length=20,
        help_text='Ex: 2024.1, 2024/2, 2024',
        verbose_name='Ano/Semestre'
    )
    max_grupos = models.IntegerField(
        default=10,
        validators=[MinValueValidator(1)],
        verbose_name='Máximo de Grupos'
    )
    max_membros_grupo = models.IntegerField(
        default=5,
        validators=[MinValueValidator(2), MaxValueValidator(10)],
        verbose_name='Máximo de Membros por Grupo'
    )
    ativa = models.BooleanField(default=True, verbose_name='Turma Ativa')
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['-criada_em']
    
    def __str__(self):
        return f"{self.nome} ({self.ano_semestre}) - {self.professor.get_full_name()}"
    
    def save(self, *args, **kwargs):
        if not self.codigo_acesso:
            # Gera código único de 8 caracteres
            self.codigo_acesso = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)
    
    def total_estudantes(self):
        return self.estudantes.count()
    
    def total_grupos(self):
        return self.grupos.count()
    
    def pode_criar_grupo(self):
        return self.grupos.count() < self.max_grupos


class Grupo(models.Model):
    """
    Grupo de estudantes que trabalham juntos em um projeto.
    """
    nome = models.CharField(max_length=200, verbose_name='Nome do Grupo')
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='grupos',
        verbose_name='Turma'
    )
    membros = models.ManyToManyField(
        Usuario,
        related_name='grupos',
        limit_choices_to={'tipo': 'estudante'},
        verbose_name='Membros'
    )
    lider = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='grupos_liderados',
        limit_choices_to={'tipo': 'estudante'},
        verbose_name='Líder do Grupo'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ['turma', 'nome']
        unique_together = ['turma', 'nome']
    
    def __str__(self):
        return f"{self.nome} - {self.turma.nome}"
    
    def total_membros(self):
        return self.membros.count()
    
    def pode_adicionar_membro(self):
        return self.membros.count() < self.turma.max_membros_grupo


class Projeto(models.Model):
    """
    Projeto científico desenvolvido por um grupo seguindo as 6 fases do método científico.
    """
    FASES = (
        (1, 'Fase 1: Problema de Pesquisa'),
        (2, 'Fase 2: Hipótese'),
        (3, 'Fase 3: Metodologia'),
        (4, 'Fase 4: Coleta de Dados'),
        (5, 'Fase 5: Análise de Dados'),
        (6, 'Fase 6: Conclusão'),
    )
    
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('em_andamento', 'Em Andamento'),
        ('aguardando_aprovacao', 'Aguardando Aprovação'),
        ('concluido', 'Concluído'),
    )
    
    AREAS_CIENCIA = (
        ('biologia', 'Biologia'),
        ('fisica', 'Física'),
        ('quimica', 'Química'),
        ('matematica', 'Matemática'),
        ('ciencias_ambientais', 'Ciências Ambientais'),
        ('ciencias_sociais', 'Ciências Sociais'),
        ('astronomia', 'Astronomia'),
        ('geologia', 'Geologia'),
        ('saude', 'Saúde'),
        ('tecnologia', 'Tecnologia'),
        ('outro', 'Outro'),
    )
    
    # Informações básicas
    titulo = models.CharField(max_length=300, verbose_name='Título do Projeto')
    slug = models.SlugField(max_length=300, unique=True, editable=False)
    grupo = models.OneToOneField(
        Grupo,
        on_delete=models.CASCADE,
        related_name='projeto',
        verbose_name='Grupo'
    )
    area_ciencia = models.CharField(
        max_length=50,
        choices=AREAS_CIENCIA,
        verbose_name='Área da Ciência'
    )
    descricao_breve = models.TextField(
        max_length=500,
        help_text='Resumo do projeto em até 500 caracteres',
        verbose_name='Descrição Breve'
    )
    
    # Status e fase
    fase_atual = models.IntegerField(
        choices=FASES,
        default=1,
        verbose_name='Fase Atual'
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default='rascunho',
        verbose_name='Status'
    )
    
    # Fase 1: Problema de Pesquisa
    fase1_pergunta = models.TextField(
        blank=True,
        null=True,
        verbose_name='Pergunta de Pesquisa',
        help_text='Qual é a pergunta científica que vocês querem responder?'
    )
    fase1_justificativa = models.TextField(
        blank=True,
        null=True,
        verbose_name='Justificativa',
        help_text='Por que essa pesquisa é importante?'
    )
    fase1_objetivos = models.TextField(
        blank=True,
        null=True,
        verbose_name='Objetivos',
        help_text='O que vocês esperam alcançar com esta pesquisa?'
    )
    fase1_aprovada = models.BooleanField(default=False, verbose_name='Fase 1 Aprovada')
    fase1_aprovada_em = models.DateTimeField(blank=True, null=True)
    
    # Fase 2: Hipótese
    fase2_hipotese_principal = models.TextField(
        blank=True,
        null=True,
        verbose_name='Hipótese Principal',
        help_text='Qual é a resposta que vocês acreditam que vão encontrar?'
    )
    fase2_fundamentacao = models.TextField(
        blank=True,
        null=True,
        verbose_name='Fundamentação Teórica',
        help_text='Em que vocês basearam essa hipótese? Pesquisas anteriores, observações?'
    )
    fase2_aprovada = models.BooleanField(default=False, verbose_name='Fase 2 Aprovada')
    fase2_aprovada_em = models.DateTimeField(blank=True, null=True)
    
    # Fase 3: Metodologia
    fase3_metodo_coleta = models.TextField(
        blank=True,
        null=True,
        verbose_name='Método de Coleta de Dados',
        help_text='Como vocês vão coletar os dados? Observação, experimento, questionário?'
    )
    fase3_materiais = models.TextField(
        blank=True,
        null=True,
        verbose_name='Materiais e Ferramentas',
        help_text='Quais materiais, equipamentos ou ferramentas vocês vão usar?'
    )
    fase3_cronograma = models.TextField(
        blank=True,
        null=True,
        verbose_name='Cronograma',
        help_text='Quando e por quanto tempo vocês vão coletar dados?'
    )
    fase3_local = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name='Local da Pesquisa',
        help_text='Onde a pesquisa será realizada?'
    )
    fase3_aprovada = models.BooleanField(default=False, verbose_name='Fase 3 Aprovada')
    fase3_aprovada_em = models.DateTimeField(blank=True, null=True)
    
    # Fase 4: Coleta de Dados (observações são um modelo separado)
    fase4_aprovada = models.BooleanField(default=False, verbose_name='Fase 4 Aprovada')
    fase4_aprovada_em = models.DateTimeField(blank=True, null=True)
    
    # Fase 5: Análise de Dados
    fase5_organizacao_dados = models.TextField(
        blank=True,
        null=True,
        verbose_name='Organização dos Dados',
        help_text='Como vocês organizaram os dados coletados?'
    )
    fase5_interpretacao = models.TextField(
        blank=True,
        null=True,
        verbose_name='Interpretação dos Resultados',
        help_text='O que os dados mostram? Quais padrões vocês identificaram?'
    )
    fase5_discussao = models.TextField(
        blank=True,
        null=True,
        verbose_name='Discussão',
        help_text='O que esses resultados significam? Eles fazem sentido?'
    )
    fase5_aprovada = models.BooleanField(default=False, verbose_name='Fase 5 Aprovada')
    fase5_aprovada_em = models.DateTimeField(blank=True, null=True)
    
    # Fase 6: Conclusão
    fase6_hipotese_confirmada = models.CharField(
        max_length=20,
        choices=[
            ('sim', 'Sim, confirmada'),
            ('parcial', 'Parcialmente confirmada'),
            ('nao', 'Não confirmada'),
        ],
        blank=True,
        null=True,
        verbose_name='Hipótese Confirmada?'
    )
    fase6_conclusao = models.TextField(
        blank=True,
        null=True,
        verbose_name='Conclusão',
        help_text='Qual a resposta final para a pergunta de pesquisa?'
    )
    fase6_aprendizados = models.TextField(
        blank=True,
        null=True,
        verbose_name='Aprendizados',
        help_text='O que vocês aprenderam com este projeto?'
    )
    fase6_limitacoes = models.TextField(
        blank=True,
        null=True,
        verbose_name='Limitações do Estudo',
        help_text='Quais foram as dificuldades e limitações da pesquisa?'
    )
    fase6_aprovada = models.BooleanField(default=False, verbose_name='Fase 6 Aprovada')
    fase6_aprovada_em = models.DateTimeField(blank=True, null=True)
    
    # Anexos do Projeto (Documentos e Fotos Adicionais)
    relatorio_final = models.FileField(
        upload_to='relatorios/',
        blank=True,
        null=True,
        storage=DocumentStorage(),
        verbose_name='Relatório Final (PDF/DOCX)',
        help_text='Documento completo do projeto'
    )
    apresentacao = models.FileField(
        upload_to='apresentacoes/',
        blank=True,
        null=True,
        storage=DocumentStorage(),
        verbose_name='Apresentação (PPT/PDF)',
        help_text='Slides da apresentação do projeto'
    )
    foto_equipe = models.ImageField(
        upload_to='fotos_equipe/',
        blank=True,
        null=True,
        verbose_name='Foto da Equipe',
        help_text='Foto do grupo'
    )
    anexo_extra1 = models.FileField(
        upload_to='anexos/',
        blank=True,
        null=True,
        storage=DocumentStorage(),
        verbose_name='Anexo Extra 1'
    )
    anexo_extra2 = models.FileField(
        upload_to='anexos/',
        blank=True,
        null=True,
        storage=DocumentStorage(),
        verbose_name='Anexo Extra 2'
    )
    anexo_extra3 = models.FileField(
        upload_to='anexos/',
        blank=True,
        null=True,
        storage=DocumentStorage(),
        verbose_name='Anexo Extra 3'
    )
    
    # Metadados
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    concluido_em = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-criado_em']
    
    def __str__(self):
        return f"{self.titulo} - {self.grupo.nome}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titulo)
            slug = base_slug
            counter = 1
            while Projeto.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def pode_avancar_fase(self):
        """Verifica se pode avançar para a próxima fase"""
        if self.fase_atual == 1 and self.fase1_aprovada:
            return True
        elif self.fase_atual == 2 and self.fase2_aprovada:
            return True
        elif self.fase_atual == 3 and self.fase3_aprovada:
            return True
        elif self.fase_atual == 4 and self.fase4_aprovada:
            return True
        elif self.fase_atual == 5 and self.fase5_aprovada:
            return True
        return False
    
    def avancar_fase(self):
        """Avança para a próxima fase se possível"""
        if self.pode_avancar_fase() and self.fase_atual < 6:
            self.fase_atual += 1
            if self.fase_atual == 6:
                self.status = 'aguardando_aprovacao'
            self.save()
            return True
        return False
    
    def get_progresso_percentual(self):
        """Retorna o progresso em porcentagem"""
        fases_aprovadas = sum([
            self.fase1_aprovada,
            self.fase2_aprovada,
            self.fase3_aprovada,
            self.fase4_aprovada,
            self.fase5_aprovada,
            self.fase6_aprovada
        ])
        return (fases_aprovadas / 6) * 100
    
    def total_observacoes(self):
        return self.observacoes.count()


class Observacao(models.Model):
    """
    Dados coletados durante a Fase 4 do projeto.
    """
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name='observacoes',
        verbose_name='Projeto'
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='observacoes',
        verbose_name='Coletado por'
    )
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição')
    
    # Dados estruturados (podem ser customizados por projeto)
    dados_json = models.JSONField(
        blank=True,
        null=True,
        verbose_name='Dados Estruturados',
        help_text='Dados em formato JSON para flexibilidade'
    )
    
    # Fotos/evidências
    foto1 = models.ImageField(
        upload_to='observacoes/',
        blank=True,
        null=True,
        verbose_name='Foto 1'
    )
    foto2 = models.ImageField(
        upload_to='observacoes/',
        blank=True,
        null=True,
        verbose_name='Foto 2'
    )
    foto3 = models.ImageField(
        upload_to='observacoes/',
        blank=True,
        null=True,
        verbose_name='Foto 3'
    )
    
    # Localização (opcional)
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        verbose_name='Latitude'
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        verbose_name='Longitude'
    )
    local_descricao = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name='Descrição do Local'
    )
    
    # Data e hora da coleta
    data_hora_coleta = models.DateTimeField(
        default=timezone.now,
        verbose_name='Data e Hora da Coleta'
    )
    
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Observação'
        verbose_name_plural = 'Observações'
        ordering = ['-data_hora_coleta']
    
    def __str__(self):
        return f"{self.titulo} - {self.projeto.titulo}"


class Feedback(models.Model):
    """
    Feedback do professor sobre uma fase específica do projeto.
    """
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name='feedbacks',
        verbose_name='Projeto'
    )
    fase = models.IntegerField(
        choices=Projeto.FASES,
        verbose_name='Fase'
    )
    professor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='feedbacks_dados',
        limit_choices_to={'tipo': 'professor'},
        verbose_name='Professor'
    )
    comentario = models.TextField(verbose_name='Comentário')
    aprovado = models.BooleanField(
        default=False,
        verbose_name='Aprovado',
        help_text='Marque se a fase está aprovada para o grupo avançar'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        ordering = ['-criado_em']
    
    def __str__(self):
        return f"Feedback - {self.projeto.titulo} - Fase {self.fase}"


class Avaliacao(models.Model):
    """
    Avaliação final do projeto pelo professor.
    """
    CONCEITOS = (
        ('A', 'A - Excelente'),
        ('B', 'B - Bom'),
        ('C', 'C - Satisfatório'),
        ('D', 'D - Insuficiente'),
    )
    
    projeto = models.OneToOneField(
        Projeto,
        on_delete=models.CASCADE,
        related_name='avaliacao',
        verbose_name='Projeto'
    )
    professor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='avaliacoes_dadas',
        limit_choices_to={'tipo': 'professor'},
        verbose_name='Professor'
    )
    conceito = models.CharField(
        max_length=1,
        choices=CONCEITOS,
        verbose_name='Conceito'
    )
    
    # Critérios de avaliação
    nota_problema = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name='Nota - Definição do Problema',
        help_text='0 a 10'
    )
    nota_hipotese = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name='Nota - Hipótese',
        help_text='0 a 10'
    )
    nota_metodologia = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name='Nota - Metodologia',
        help_text='0 a 10'
    )
    nota_coleta = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name='Nota - Coleta de Dados',
        help_text='0 a 10'
    )
    nota_analise = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name='Nota - Análise',
        help_text='0 a 10'
    )
    nota_conclusao = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name='Nota - Conclusão',
        help_text='0 a 10'
    )
    
    comentarios = models.TextField(
        blank=True,
        null=True,
        verbose_name='Comentários Gerais'
    )
    pontos_fortes = models.TextField(
        blank=True,
        null=True,
        verbose_name='Pontos Fortes'
    )
    pontos_melhorar = models.TextField(
        blank=True,
        null=True,
        verbose_name='Pontos a Melhorar'
    )
    
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['-criada_em']
    
    def __str__(self):
        return f"Avaliação - {self.projeto.titulo} - Conceito {self.conceito}"
    
    def media_notas(self):
        """Calcula a média das 6 notas"""
        return (
            self.nota_problema +
            self.nota_hipotese +
            self.nota_metodologia +
            self.nota_coleta +
            self.nota_analise +
            self.nota_conclusao
        ) / 6


# Relacionamento Estudante-Turma (many-to-many)
class EstudanteTurma(models.Model):
    """
    Relacionamento entre estudante e turma.
    """
    estudante = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='turmas_estudante',
        limit_choices_to={'tipo': 'estudante'},
        verbose_name='Estudante'
    )
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='estudantes',
        verbose_name='Turma'
    )
    data_entrada = models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')
    
    class Meta:
        verbose_name = 'Estudante-Turma'
        verbose_name_plural = 'Estudantes-Turmas'
        unique_together = ['estudante', 'turma']
        ordering = ['turma', 'data_entrada']
    
    def __str__(self):
        return f"{self.estudante.get_full_name()} - {self.turma.nome}"


class Atividade(models.Model):
    """
    Atividades e informações postadas pelo professor para uma turma específica.
    Professores podem criar, editar e excluir. Estudantes podem apenas visualizar.
    """
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='atividades',
        verbose_name='Turma'
    )
    autor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='atividades_criadas',
        limit_choices_to={'tipo': 'professor'},
        verbose_name='Professor'
    )
    titulo = models.CharField(max_length=300, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição')
    
    # Tipo de atividade
    TIPO_ATIVIDADE = (
        ('informacao', 'Informação'),
        ('tarefa', 'Tarefa'),
        ('material', 'Material de Apoio'),
        ('aviso', 'Aviso'),
    )
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_ATIVIDADE,
        default='informacao',
        verbose_name='Tipo'
    )
    
    # Datas importantes
    data_entrega = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Entrega',
        help_text='Opcional - para tarefas com prazo'
    )
    
    # Arquivos anexos (opcional)
    arquivo = models.FileField(
        upload_to='atividades/',
        blank=True,
        null=True,
        storage=DocumentStorage(),
        verbose_name='Arquivo Anexo'
    )
    
    # Controle
    fixado = models.BooleanField(
        default=False,
        verbose_name='Fixar no Topo',
        help_text='Atividades fixadas aparecem primeiro'
    )
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'
        ordering = ['-fixado', '-criado_em']
    
    def __str__(self):
        return f"{self.titulo} - {self.turma.nome}"


class Badge(models.Model):
    """
    Badge/Conquista que pode ser obtida por estudantes.
    """
    nome = models.CharField(max_length=100, verbose_name='Nome da Badge')
    descricao = models.TextField(verbose_name='Descrição')
    icone = models.CharField(
        max_length=50,
        default='🏆',
        verbose_name='Ícone (Emoji)',
        help_text='Emoji que representa a badge'
    )
    pontos = models.IntegerField(
        default=10,
        validators=[MinValueValidator(0)],
        verbose_name='Pontos',
        help_text='Pontos ganhos ao conquistar esta badge'
    )
    
    # Critério de conquista
    CRITERIOS = (
        ('primeira_observacao', 'Primeira Observação Criada'),
        ('cinco_observacoes', '5 Observações Criadas'),
        ('fase1_completa', 'Fase 1 Aprovada'),
        ('fase3_completa', 'Fase 3 Aprovada'),
        ('fase6_completa', 'Fase 6 Aprovada'),
        ('projeto_concluido', 'Projeto Concluído'),
        ('primeira_foto', 'Primeira Foto Anexada'),
        ('explorador', 'Observações com Geolocalização'),
        ('colaborador', 'Membro de Grupo'),
        ('lider', 'Líder de Grupo'),
    )
    criterio = models.CharField(
        max_length=50,
        choices=CRITERIOS,
        unique=True,
        verbose_name='Critério'
    )
    
    ativa = models.BooleanField(default=True, verbose_name='Ativa')
    criada_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Badge'
        verbose_name_plural = 'Badges'
        ordering = ['nome']
    
    def __str__(self):
        return f"{self.icone} {self.nome}"


class UsuarioBadge(models.Model):
    """
    Relação entre usuário e badges conquistadas.
    """
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='badges_conquistadas',
        verbose_name='Usuário'
    )
    badge = models.ForeignKey(
        Badge,
        on_delete=models.CASCADE,
        related_name='conquistadores',
        verbose_name='Badge'
    )
    conquistada_em = models.DateTimeField(auto_now_add=True, verbose_name='Conquistada em')
    
    class Meta:
        verbose_name = 'Badge do Usuário'
        verbose_name_plural = 'Badges dos Usuários'
        unique_together = ['usuario', 'badge']
        ordering = ['-conquistada_em']
    
    def __str__(self):
        return f"{self.usuario.username} - {self.badge.nome}"


class PontuacaoGrupo(models.Model):
    """
    Pontuação acumulada de um grupo.
    """
    grupo = models.OneToOneField(
        Grupo,
        on_delete=models.CASCADE,
        related_name='pontuacao',
        verbose_name='Grupo'
    )
    pontos_totais = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name='Pontos Totais'
    )
    atualizada_em = models.DateTimeField(auto_now=True, verbose_name='Atualizada em')
    
    class Meta:
        verbose_name = 'Pontuação do Grupo'
        verbose_name_plural = 'Pontuações dos Grupos'
        ordering = ['-pontos_totais']
    
    def __str__(self):
        return f"{self.grupo.nome} - {self.pontos_totais} pontos"
