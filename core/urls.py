from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página inicial
    path('', views.home, name='home'),
    
    # Autenticação
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro_view, name='registro'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Professor - Turmas
    path('turmas/', views.turmas_lista, name='turmas_lista'),
    path('turmas/criar/', views.turma_criar, name='turma_criar'),
    path('turmas/<int:pk>/', views.turma_detalhe, name='turma_detalhe'),
    path('turmas/<int:pk>/editar/', views.turma_editar, name='turma_editar'),
    
    # Professor - Grupos
    path('turmas/<int:turma_pk>/grupos/criar/', views.grupo_criar, name='grupo_criar'),
    path('grupos/<int:pk>/', views.grupo_detalhe, name='grupo_detalhe'),
    path('grupos/<int:pk>/editar/', views.grupo_editar, name='grupo_editar'),
    
    # Estudante - Entrar em turma
    path('turmas/entrar/', views.turma_entrar, name='turma_entrar'),
    path('turmas/<int:turma_pk>/grupos/entrar/<int:grupo_pk>/', views.grupo_entrar, name='grupo_entrar'),
    
    # Projetos
    path('projetos/', views.projetos_lista, name='projetos_lista'),
    path('projetos/criar/<int:grupo_pk>/', views.projeto_criar, name='projeto_criar'),
    path('projetos/<slug:slug>/', views.projeto_detalhe, name='projeto_detalhe'),
    path('projetos/<slug:slug>/editar/', views.projeto_editar, name='projeto_editar'),
    path('projetos/<slug:slug>/fase/<int:fase>/', views.projeto_fase_editar, name='projeto_fase_editar'),
    
    # Observações (Fase 4)
    path('projetos/<slug:slug>/observacoes/adicionar/', views.observacao_criar, name='observacao_criar'),
    path('observacoes/<int:pk>/editar/', views.observacao_editar, name='observacao_editar'),
    path('observacoes/<int:pk>/excluir/', views.observacao_excluir, name='observacao_excluir'),
    
    # Professor - Feedback e Aprovação
    path('projetos/<slug:slug>/feedback/<int:fase>/', views.feedback_criar, name='feedback_criar'),
    path('projetos/<slug:slug>/aprovar-fase/<int:fase>/', views.aprovar_fase, name='aprovar_fase'),
    
    # Professor - Avaliação
    path('projetos/<slug:slug>/avaliar/', views.projeto_avaliar, name='projeto_avaliar'),
    
    # Atividades da Turma
    path('turmas/<int:pk>/atividades/', views.turma_atividades, name='turma_atividades'),
    path('turmas/<int:turma_pk>/atividades/criar/', views.atividade_criar, name='atividade_criar'),
    path('atividades/<int:pk>/', views.atividade_detalhe, name='atividade_detalhe'),
    path('atividades/<int:pk>/editar/', views.atividade_editar, name='atividade_editar'),
    path('atividades/<int:pk>/excluir/', views.atividade_excluir, name='atividade_excluir'),
]

