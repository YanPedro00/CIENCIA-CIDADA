"""
Sinais para gamificação automática (ENTREGA 5)
Badges são conquistadas automaticamente quando o usuário realiza determinadas ações
"""
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import (
    Observacao, Projeto, Grupo, Badge, UsuarioBadge, 
    PontuacaoGrupo
)


def atribuir_badge(usuario, criterio):
    """
    Atribui uma badge ao usuário se ele ainda não a possui
    """
    try:
        badge = Badge.objects.get(criterio=criterio, ativa=True)
        usuario_badge, created = UsuarioBadge.objects.get_or_create(
            usuario=usuario,
            badge=badge
        )
        
        if created:
            # Adicionar pontos ao grupo (se o usuário estiver em algum)
            grupos = usuario.grupos.all()
            for grupo in grupos:
                pontuacao, _ = PontuacaoGrupo.objects.get_or_create(grupo=grupo)
                pontuacao.pontos_totais += badge.pontos
                pontuacao.save()
            
            return True
    except Badge.DoesNotExist:
        pass
    return False


@receiver(post_save, sender=Observacao)
def badge_observacoes(sender, instance, created, **kwargs):
    """
    Badges relacionadas à criação de observações
    """
    if created:
        usuario = instance.usuario
        
        # Badge: Primeira Observação
        total_obs = Observacao.objects.filter(usuario=usuario).count()
        if total_obs == 1:
            atribuir_badge(usuario, 'primeira_observacao')
        
        # Badge: Explorador (5 observações)
        if total_obs == 5:
            atribuir_badge(usuario, 'cinco_observacoes')
        
        # Badge: Primeira Foto
        if instance.foto1:
            tem_foto_anterior = Observacao.objects.filter(
                usuario=usuario
            ).exclude(foto1='').exclude(id=instance.id).exists()
            
            if not tem_foto_anterior:
                atribuir_badge(usuario, 'primeira_foto')
        
        # Badge: Geógrafo (observação com geolocalização)
        if instance.latitude and instance.longitude:
            tem_geo_anterior = Observacao.objects.filter(
                usuario=usuario,
                latitude__isnull=False,
                longitude__isnull=False
            ).exclude(id=instance.id).exists()
            
            if not tem_geo_anterior:
                atribuir_badge(usuario, 'explorador')


@receiver(post_save, sender=Projeto)
def badge_projetos(sender, instance, created, **kwargs):
    """
    Badges relacionadas a fases do projeto
    """
    if not created:  # Só verificar em atualizações
        # Atribuir badges a todos os membros do grupo
        membros = instance.grupo.membros.all()
        
        # Badge: Fase 1 Aprovada
        if instance.fase1_aprovada:
            for membro in membros:
                atribuir_badge(membro, 'fase1_completa')
        
        # Badge: Fase 3 Aprovada
        if instance.fase3_aprovada:
            for membro in membros:
                atribuir_badge(membro, 'fase3_completa')
        
        # Badge: Fase 6 Aprovada
        if instance.fase6_aprovada:
            for membro in membros:
                atribuir_badge(membro, 'fase6_completa')
        
        # Badge: Projeto Concluído
        if instance.status == 'concluido':
            for membro in membros:
                atribuir_badge(membro, 'projeto_concluido')


@receiver(m2m_changed, sender=Grupo.membros.through)
def badge_grupos(sender, instance, action, pk_set, **kwargs):
    """
    Badges relacionadas a participação em grupos
    """
    if action == 'post_add':
        # Badge: Colaborador (entrou em um grupo)
        for usuario_id in pk_set:
            from .models import Usuario
            try:
                usuario = Usuario.objects.get(id=usuario_id)
                atribuir_badge(usuario, 'colaborador')
            except Usuario.DoesNotExist:
                pass


@receiver(post_save, sender=Grupo)
def badge_lider(sender, instance, created, **kwargs):
    """
    Badge: Líder de Grupo
    """
    if instance.lider:
        atribuir_badge(instance.lider, 'lider')

