from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import (
    Usuario, Turma, Grupo, Projeto, Observacao, 
    Feedback, Avaliacao, EstudanteTurma, Atividade,
    Badge, UsuarioBadge, PontuacaoGrupo
)


@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    """Admin customizado para o modelo Usuario"""
    list_display = ['username', 'email', 'first_name', 'last_name', 'tipo', 'instituicao', 'is_active']
    list_filter = ['tipo', 'is_active', 'is_staff', 'instituicao']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('tipo', 'instituicao', 'telefone', 'foto_perfil')
        }),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Informações Adicionais', {
            'fields': ('tipo', 'instituicao', 'telefone', 'email', 'first_name', 'last_name')
        }),
    )


class EstudanteTurmaInline(admin.TabularInline):
    """Inline para estudantes na turma"""
    model = EstudanteTurma
    extra = 0
    readonly_fields = ['data_entrada']
    autocomplete_fields = ['estudante']


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    """Admin para Turma"""
    list_display = ['nome', 'professor', 'codigo_acesso', 'ano_semestre', 'total_estudantes', 'total_grupos', 'ativa']
    list_filter = ['ativa', 'ano_semestre', 'professor']
    search_fields = ['nome', 'codigo_acesso', 'professor__username', 'professor__first_name']
    readonly_fields = ['codigo_acesso', 'criada_em', 'atualizada_em']
    inlines = [EstudanteTurmaInline]
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'descricao', 'professor', 'ano_semestre')
        }),
        ('Configurações', {
            'fields': ('max_grupos', 'max_membros_grupo', 'ativa')
        }),
        ('Acesso', {
            'fields': ('codigo_acesso',)
        }),
        ('Metadados', {
            'fields': ('criada_em', 'atualizada_em'),
            'classes': ('collapse',)
        }),
    )
    
    def total_estudantes(self, obj):
        return obj.total_estudantes()
    total_estudantes.short_description = 'Total de Estudantes'
    
    def total_grupos(self, obj):
        return obj.total_grupos()
    total_grupos.short_description = 'Total de Grupos'


@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    """Admin para Grupo"""
    list_display = ['nome', 'turma', 'lider', 'total_membros', 'criado_em']
    list_filter = ['turma', 'criado_em']
    search_fields = ['nome', 'turma__nome', 'lider__username']
    filter_horizontal = ['membros']
    autocomplete_fields = ['turma', 'lider']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'turma', 'lider')
        }),
        ('Membros', {
            'fields': ('membros',)
        }),
        ('Metadados', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['criado_em', 'atualizado_em']
    
    def total_membros(self, obj):
        return obj.total_membros()
    total_membros.short_description = 'Total de Membros'


class ObservacaoInline(admin.TabularInline):
    """Inline para observações do projeto"""
    model = Observacao
    extra = 0
    fields = ['titulo', 'usuario', 'data_hora_coleta']
    readonly_fields = ['usuario', 'data_hora_coleta']


class FeedbackInline(admin.TabularInline):
    """Inline para feedbacks do projeto"""
    model = Feedback
    extra = 0
    fields = ['fase', 'professor', 'aprovado', 'comentario']
    readonly_fields = ['professor', 'criado_em']


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    """Admin para Projeto"""
    list_display = ['titulo', 'grupo', 'area_ciencia', 'fase_atual_display', 'status', 'progresso', 'criado_em']
    list_filter = ['status', 'fase_atual', 'area_ciencia', 'grupo__turma']
    search_fields = ['titulo', 'grupo__nome', 'descricao_breve']
    readonly_fields = ['slug', 'criado_em', 'atualizado_em', 'concluido_em', 'progresso']
    inlines = [ObservacaoInline, FeedbackInline]
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'slug', 'grupo', 'area_ciencia', 'descricao_breve')
        }),
        ('Status', {
            'fields': ('fase_atual', 'status', 'progresso')
        }),
        ('Fase 1: Problema de Pesquisa', {
            'fields': ('fase1_pergunta', 'fase1_justificativa', 'fase1_objetivos', 'fase1_aprovada', 'fase1_aprovada_em'),
            'classes': ('collapse',)
        }),
        ('Fase 2: Hipótese', {
            'fields': ('fase2_hipotese_principal', 'fase2_fundamentacao', 'fase2_aprovada', 'fase2_aprovada_em'),
            'classes': ('collapse',)
        }),
        ('Fase 3: Metodologia', {
            'fields': ('fase3_metodo_coleta', 'fase3_materiais', 'fase3_cronograma', 'fase3_local', 'fase3_aprovada', 'fase3_aprovada_em'),
            'classes': ('collapse',)
        }),
        ('Fase 4: Coleta de Dados', {
            'fields': ('fase4_aprovada', 'fase4_aprovada_em'),
            'classes': ('collapse',)
        }),
        ('Fase 5: Análise de Dados', {
            'fields': ('fase5_organizacao_dados', 'fase5_interpretacao', 'fase5_discussao', 'fase5_aprovada', 'fase5_aprovada_em'),
            'classes': ('collapse',)
        }),
        ('Fase 6: Conclusão', {
            'fields': ('fase6_hipotese_confirmada', 'fase6_conclusao', 'fase6_aprendizados', 'fase6_limitacoes', 'fase6_aprovada', 'fase6_aprovada_em'),
            'classes': ('collapse',)
        }),
        ('Metadados', {
            'fields': ('criado_em', 'atualizado_em', 'concluido_em'),
            'classes': ('collapse',)
        }),
    )
    
    def fase_atual_display(self, obj):
        return obj.get_fase_atual_display()
    fase_atual_display.short_description = 'Fase Atual'
    
    def progresso(self, obj):
        percentual = obj.get_progresso_percentual()
        cor = 'green' if percentual == 100 else 'orange' if percentual >= 50 else 'red'
        return format_html(
            '<span style="color: {};">{:.0f}%</span>',
            cor, percentual
        )
    progresso.short_description = 'Progresso'


@admin.register(Observacao)
class ObservacaoAdmin(admin.ModelAdmin):
    """Admin para Observacao"""
    list_display = ['titulo', 'projeto', 'usuario', 'data_hora_coleta', 'tem_localizacao', 'criada_em']
    list_filter = ['data_hora_coleta', 'criada_em', 'projeto__grupo__turma']
    search_fields = ['titulo', 'descricao', 'projeto__titulo', 'usuario__username']
    readonly_fields = ['criada_em', 'atualizada_em']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('projeto', 'usuario', 'titulo', 'descricao')
        }),
        ('Dados', {
            'fields': ('dados_json',)
        }),
        ('Evidências', {
            'fields': ('foto1', 'foto2', 'foto3')
        }),
        ('Localização', {
            'fields': ('latitude', 'longitude', 'local_descricao'),
            'classes': ('collapse',)
        }),
        ('Data e Hora', {
            'fields': ('data_hora_coleta',)
        }),
        ('Metadados', {
            'fields': ('criada_em', 'atualizada_em'),
            'classes': ('collapse',)
        }),
    )
    
    def tem_localizacao(self, obj):
        return bool(obj.latitude and obj.longitude)
    tem_localizacao.boolean = True
    tem_localizacao.short_description = 'Tem Localização'


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Admin para Feedback"""
    list_display = ['projeto', 'fase_display', 'professor', 'aprovado', 'criado_em']
    list_filter = ['fase', 'aprovado', 'criado_em', 'projeto__grupo__turma']
    search_fields = ['projeto__titulo', 'professor__username', 'comentario']
    readonly_fields = ['criado_em']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('projeto', 'fase', 'professor')
        }),
        ('Feedback', {
            'fields': ('comentario', 'aprovado')
        }),
        ('Metadados', {
            'fields': ('criado_em',),
            'classes': ('collapse',)
        }),
    )
    
    def fase_display(self, obj):
        return obj.get_fase_display()
    fase_display.short_description = 'Fase'


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    """Admin para Avaliacao"""
    list_display = ['projeto', 'professor', 'conceito', 'media', 'criada_em']
    list_filter = ['conceito', 'criada_em', 'projeto__grupo__turma']
    search_fields = ['projeto__titulo', 'professor__username']
    readonly_fields = ['criada_em', 'atualizada_em', 'media']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('projeto', 'professor', 'conceito')
        }),
        ('Notas por Fase', {
            'fields': ('nota_problema', 'nota_hipotese', 'nota_metodologia', 'nota_coleta', 'nota_analise', 'nota_conclusao', 'media')
        }),
        ('Comentários', {
            'fields': ('comentarios', 'pontos_fortes', 'pontos_melhorar')
        }),
        ('Metadados', {
            'fields': ('criada_em', 'atualizada_em'),
            'classes': ('collapse',)
        }),
    )
    
    def media(self, obj):
        media_val = obj.media_notas()
        cor = 'green' if media_val >= 7 else 'orange' if media_val >= 5 else 'red'
        return format_html(
            '<span style="color: {}; font-weight: bold;">{:.1f}</span>',
            cor, media_val
        )
    media.short_description = 'Média das Notas'


@admin.register(EstudanteTurma)
class EstudanteTurmaAdmin(admin.ModelAdmin):
    """Admin para EstudanteTurma"""
    list_display = ['estudante_nome', 'turma', 'data_entrada']
    list_filter = ['turma', 'data_entrada']
    search_fields = ['estudante__username', 'estudante__first_name', 'turma__nome']
    readonly_fields = ['data_entrada']
    
    def estudante_nome(self, obj):
        return obj.estudante.get_full_name() or obj.estudante.username
    estudante_nome.short_description = 'Estudante'


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    """Admin para Atividade"""
    list_display = ['titulo', 'turma', 'tipo', 'autor', 'fixado', 'ativo', 'data_entrega', 'criado_em']
    list_filter = ['tipo', 'fixado', 'ativo', 'turma', 'criado_em']
    search_fields = ['titulo', 'descricao', 'turma__nome', 'autor__username']
    readonly_fields = ['criado_em', 'atualizado_em']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('turma', 'autor', 'titulo', 'descricao', 'tipo')
        }),
        ('Anexo', {
            'fields': ('arquivo',),
            'classes': ('collapse',)
        }),
        ('Data e Controle', {
            'fields': ('data_entrega', 'fixado', 'ativo')
        }),
        ('Metadados', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    """Admin para Badge (Gamificação - Entrega 5)"""
    list_display = ['icone', 'nome', 'criterio', 'pontos', 'ativa', 'criada_em']
    list_filter = ['ativa', 'criterio']
    search_fields = ['nome', 'descricao']
    list_editable = ['ativa']
    readonly_fields = ['criada_em']
    
    fieldsets = (
        ('Informações da Badge', {
            'fields': ('nome', 'descricao', 'icone', 'pontos')
        }),
        ('Critério de Conquista', {
            'fields': ('criterio', 'ativa')
        }),
        ('Metadados', {
            'fields': ('criada_em',),
            'classes': ('collapse',)
        }),
    )


@admin.register(UsuarioBadge)
class UsuarioBadgeAdmin(admin.ModelAdmin):
    """Admin para UsuarioBadge (Gamificação - Entrega 5)"""
    list_display = ['usuario', 'badge', 'conquistada_em']
    list_filter = ['badge', 'conquistada_em']
    search_fields = ['usuario__username', 'badge__nome']
    readonly_fields = ['conquistada_em']
    date_hierarchy = 'conquistada_em'


@admin.register(PontuacaoGrupo)
class PontuacaoGrupoAdmin(admin.ModelAdmin):
    """Admin para PontuacaoGrupo (Gamificação - Entrega 5)"""
    list_display = ['grupo', 'pontos_totais', 'atualizada_em']
    list_filter = ['grupo__turma']
    search_fields = ['grupo__nome']
    readonly_fields = ['atualizada_em']
    ordering = ['-pontos_totais']
