from django.core.management.base import BaseCommand
from core.models import Badge


class Command(BaseCommand):
    help = 'Cria as badges iniciais do sistema (Gamificação - Entrega 5)'

    def handle(self, *args, **kwargs):
        badges_data = [
            {
                'nome': 'Primeira Observação',
                'descricao': 'Parabéns! Você criou sua primeira observação científica.',
                'icone': '🔬',
                'pontos': 10,
                'criterio': 'primeira_observacao',
            },
            {
                'nome': 'Explorador',
                'descricao': 'Coletou 5 observações com dados. Continue explorando!',
                'icone': '🌍',
                'pontos': 50,
                'criterio': 'cinco_observacoes',
            },
            {
                'nome': 'Problema Definido',
                'descricao': 'Fase 1 (Problema de Pesquisa) aprovada pelo professor.',
                'icone': '❓',
                'pontos': 20,
                'criterio': 'fase1_completa',
            },
            {
                'nome': 'Metodologia Aprovada',
                'descricao': 'Fase 3 (Metodologia) aprovada. Seu método está sólido!',
                'icone': '📋',
                'pontos': 30,
                'criterio': 'fase3_completa',
            },
            {
                'nome': 'Conclusão Científica',
                'descricao': 'Fase 6 (Conclusão) aprovada. Você está quase lá!',
                'icone': '🎯',
                'pontos': 40,
                'criterio': 'fase6_completa',
            },
            {
                'nome': 'Projeto Completo',
                'descricao': 'Parabéns! Você concluiu todo o projeto científico.',
                'icone': '🏆',
                'pontos': 100,
                'criterio': 'projeto_concluido',
            },
            {
                'nome': 'Fotógrafo Científico',
                'descricao': 'Anexou sua primeira foto a uma observação.',
                'icone': '📸',
                'pontos': 15,
                'criterio': 'primeira_foto',
            },
            {
                'nome': 'Geógrafo',
                'descricao': 'Registrou observações com geolocalização.',
                'icone': '🗺️',
                'pontos': 25,
                'criterio': 'explorador',
            },
            {
                'nome': 'Colaborador',
                'descricao': 'Entrou em um grupo de pesquisa.',
                'icone': '🤝',
                'pontos': 10,
                'criterio': 'colaborador',
            },
            {
                'nome': 'Líder de Grupo',
                'descricao': 'Foi eleito líder do grupo. Boa sorte!',
                'icone': '👑',
                'pontos': 30,
                'criterio': 'lider',
            },
        ]

        created_count = 0
        for badge_info in badges_data:
            badge, created = Badge.objects.get_or_create(
                criterio=badge_info['criterio'],
                defaults=badge_info
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"✅ Badge criada: {badge.icone} {badge.nome}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"⏭️  Badge já existe: {badge.icone} {badge.nome}")
                )

        self.stdout.write(
            self.style.SUCCESS(f'\n🎉 Total de badges criadas: {created_count}/{len(badges_data)}')
        )

