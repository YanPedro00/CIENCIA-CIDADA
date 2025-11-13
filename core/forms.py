from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import (
    Usuario, Turma, Grupo, Projeto, Observacao,
    Feedback, Avaliacao, Atividade
)


class RegistroForm(UserCreationForm):
    """Formulário de registro de novo usuário"""
    email = forms.EmailField(required=True, label='E-mail')
    first_name = forms.CharField(max_length=150, required=True, label='Nome')
    last_name = forms.CharField(max_length=150, required=True, label='Sobrenome')
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'tipo', 'instituicao', 'password1', 'password2']
        labels = {
            'username': 'Nome de usuário',
            'tipo': 'Tipo de Conta',
            'instituicao': 'Instituição de Ensino',
        }
        help_texts = {
            'username': 'Letras, números e @/./+/-/_ apenas.',
        }


class LoginForm(forms.Form):
    """Formulário de login"""
    username = forms.CharField(
        max_length=150,
        label='Nome de usuário',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome de usuário'})
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Sua senha'})
    )


class TurmaForm(forms.ModelForm):
    """Formulário para criar/editar turma"""
    class Meta:
        model = Turma
        fields = ['nome', 'descricao', 'ano_semestre', 'max_grupos', 'max_membros_grupo', 'ativa']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'nome': 'Nome da Turma',
            'descricao': 'Descrição',
            'ano_semestre': 'Ano/Semestre',
            'max_grupos': 'Máximo de Grupos',
            'max_membros_grupo': 'Máximo de Membros por Grupo',
            'ativa': 'Turma Ativa',
        }


class EntrarTurmaForm(forms.Form):
    """Formulário para estudante entrar em turma"""
    codigo_acesso = forms.CharField(
        max_length=10,
        label='Código de Acesso da Turma',
        help_text='Digite o código fornecido pelo professor',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: ABC12345',
            'style': 'text-transform: uppercase;'
        })
    )


class GrupoForm(forms.ModelForm):
    """Formulário para criar/editar grupo"""
    def __init__(self, *args, **kwargs):
        self.turma = kwargs.pop('turma', None)
        super().__init__(*args, **kwargs)
        
        if self.turma:
            # Filtrar apenas estudantes da turma
            estudantes_turma = Usuario.objects.filter(
                turmas_estudante__turma=self.turma,
                tipo='estudante'
            )
            self.fields['membros'].queryset = estudantes_turma
            self.fields['lider'].queryset = estudantes_turma
    
    class Meta:
        model = Grupo
        fields = ['nome', 'membros', 'lider']
        widgets = {
            'membros': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'nome': 'Nome do Grupo',
            'membros': 'Membros do Grupo',
            'lider': 'Líder do Grupo (opcional)',
        }
        help_texts = {
            'membros': 'Selecione os estudantes que farão parte do grupo',
        }


class ProjetoForm(forms.ModelForm):
    """Formulário para criar/editar informações básicas do projeto"""
    class Meta:
        model = Projeto
        fields = ['titulo', 'area_ciencia', 'descricao_breve']
        widgets = {
            'descricao_breve': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'titulo': 'Título do Projeto',
            'area_ciencia': 'Área da Ciência',
            'descricao_breve': 'Descrição Breve do Projeto',
        }


class Fase1Form(forms.ModelForm):
    """Formulário para Fase 1: Problema de Pesquisa"""
    class Meta:
        model = Projeto
        fields = ['fase1_pergunta', 'fase1_justificativa', 'fase1_objetivos']
        widgets = {
            'fase1_pergunta': forms.Textarea(attrs={'rows': 3}),
            'fase1_justificativa': forms.Textarea(attrs={'rows': 4}),
            'fase1_objetivos': forms.Textarea(attrs={'rows': 4}),
        }


class Fase2Form(forms.ModelForm):
    """Formulário para Fase 2: Hipótese"""
    class Meta:
        model = Projeto
        fields = ['fase2_hipotese_principal', 'fase2_fundamentacao']
        widgets = {
            'fase2_hipotese_principal': forms.Textarea(attrs={'rows': 3}),
            'fase2_fundamentacao': forms.Textarea(attrs={'rows': 5}),
        }


class Fase3Form(forms.ModelForm):
    """Formulário para Fase 3: Metodologia"""
    class Meta:
        model = Projeto
        fields = ['fase3_metodo_coleta', 'fase3_materiais', 'fase3_cronograma', 'fase3_local']
        widgets = {
            'fase3_metodo_coleta': forms.Textarea(attrs={'rows': 4}),
            'fase3_materiais': forms.Textarea(attrs={'rows': 3}),
            'fase3_cronograma': forms.Textarea(attrs={'rows': 3}),
            'fase3_local': forms.TextInput(attrs={'placeholder': 'Ex: Laboratório da escola, Rio Municipal, etc.'}),
        }


class Fase5Form(forms.ModelForm):
    """Formulário para Fase 5: Análise de Dados"""
    class Meta:
        model = Projeto
        fields = ['fase5_organizacao_dados', 'fase5_interpretacao', 'fase5_discussao']
        widgets = {
            'fase5_organizacao_dados': forms.Textarea(attrs={'rows': 4}),
            'fase5_interpretacao': forms.Textarea(attrs={'rows': 5}),
            'fase5_discussao': forms.Textarea(attrs={'rows': 5}),
        }


class Fase6Form(forms.ModelForm):
    """Formulário para Fase 6: Conclusão"""
    class Meta:
        model = Projeto
        fields = [
            'fase6_hipotese_confirmada',
            'fase6_conclusao',
            'fase6_aprendizados',
            'fase6_limitacoes'
        ]
        widgets = {
            'fase6_conclusao': forms.Textarea(attrs={'rows': 5}),
            'fase6_aprendizados': forms.Textarea(attrs={'rows': 4}),
            'fase6_limitacoes': forms.Textarea(attrs={'rows': 4}),
        }


class ObservacaoForm(forms.ModelForm):
    """Formulário para adicionar/editar observação"""
    class Meta:
        model = Observacao
        fields = [
            'titulo',
            'descricao',
            'dados_json',
            'foto1',
            'foto2',
            'foto3',
            'latitude',
            'longitude',
            'local_descricao',
            'data_hora_coleta'
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'dados_json': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': '{"temperatura": 25, "ph": 7.5}'
            }),
            'data_hora_coleta': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'titulo': 'Título da Observação',
            'descricao': 'Descrição',
            'dados_json': 'Dados Estruturados (JSON - opcional)',
            'foto1': 'Foto 1',
            'foto2': 'Foto 2',
            'foto3': 'Foto 3',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
            'local_descricao': 'Descrição do Local',
            'data_hora_coleta': 'Data e Hora da Coleta',
        }
        help_texts = {
            'dados_json': 'Formato JSON para dados estruturados. Ex: {"temperatura": 25}',
            'latitude': 'Coordenada em decimal. Ex: -23.550520',
            'longitude': 'Coordenada em decimal. Ex: -46.633308',
        }


class FeedbackForm(forms.ModelForm):
    """Formulário para professor dar feedback"""
    class Meta:
        model = Feedback
        fields = ['comentario', 'aprovado']
        widgets = {
            'comentario': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Escreva seu feedback para o grupo...'
            }),
        }
        labels = {
            'comentario': 'Comentário',
            'aprovado': 'Aprovar esta fase',
        }
        help_texts = {
            'aprovado': 'Marque se o grupo pode avançar para a próxima fase',
        }


class AvaliacaoForm(forms.ModelForm):
    """Formulário para avaliação final do projeto"""
    class Meta:
        model = Avaliacao
        fields = [
            'conceito',
            'nota_problema',
            'nota_hipotese',
            'nota_metodologia',
            'nota_coleta',
            'nota_analise',
            'nota_conclusao',
            'comentarios',
            'pontos_fortes',
            'pontos_melhorar'
        ]
        widgets = {
            'nota_problema': forms.NumberInput(attrs={'min': 0, 'max': 10, 'step': 1}),
            'nota_hipotese': forms.NumberInput(attrs={'min': 0, 'max': 10, 'step': 1}),
            'nota_metodologia': forms.NumberInput(attrs={'min': 0, 'max': 10, 'step': 1}),
            'nota_coleta': forms.NumberInput(attrs={'min': 0, 'max': 10, 'step': 1}),
            'nota_analise': forms.NumberInput(attrs={'min': 0, 'max': 10, 'step': 1}),
            'nota_conclusao': forms.NumberInput(attrs={'min': 0, 'max': 10, 'step': 1}),
            'comentarios': forms.Textarea(attrs={'rows': 4}),
            'pontos_fortes': forms.Textarea(attrs={'rows': 3}),
            'pontos_melhorar': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'conceito': 'Conceito Final',
            'nota_problema': 'Nota - Definição do Problema (0-10)',
            'nota_hipotese': 'Nota - Hipótese (0-10)',
            'nota_metodologia': 'Nota - Metodologia (0-10)',
            'nota_coleta': 'Nota - Coleta de Dados (0-10)',
            'nota_analise': 'Nota - Análise (0-10)',
            'nota_conclusao': 'Nota - Conclusão (0-10)',
            'comentarios': 'Comentários Gerais',
            'pontos_fortes': 'Pontos Fortes do Projeto',
            'pontos_melhorar': 'Pontos a Melhorar',
        }


class AtividadeForm(forms.ModelForm):
    """Formulário para criar/editar atividade da turma"""
    class Meta:
        model = Atividade
        fields = [
            'titulo',
            'tipo',
            'descricao',
            'data_entrega',
            'arquivo',
            'fixado',
            'ativo'
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Descreva a atividade, tarefa ou informação...'
            }),
            'data_entrega': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }
        labels = {
            'titulo': 'Título',
            'tipo': 'Tipo de Atividade',
            'descricao': 'Descrição',
            'data_entrega': 'Data de Entrega (opcional)',
            'arquivo': 'Arquivo Anexo (opcional)',
            'fixado': 'Fixar no Topo',
            'ativo': 'Ativo (visível para os alunos)',
        }
        help_texts = {
            'data_entrega': 'Opcional - apenas para tarefas com prazo',
            'arquivo': 'PDF, imagem, documento, etc.',
            'fixado': 'Atividades fixadas aparecem no topo da lista',
        }

