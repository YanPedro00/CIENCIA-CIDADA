# Generated manually for Entrega 5
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_atividade'),
    ]

    operations = [
        # Adicionar campos de anexos no Projeto
        migrations.AddField(
            model_name='projeto',
            name='relatorio_final',
            field=models.FileField(blank=True, help_text='Documento completo do projeto', null=True, upload_to='relatorios/', verbose_name='Relatório Final (PDF/DOCX)'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='apresentacao',
            field=models.FileField(blank=True, help_text='Slides da apresentação do projeto', null=True, upload_to='apresentacoes/', verbose_name='Apresentação (PPT/PDF)'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='foto_equipe',
            field=models.ImageField(blank=True, help_text='Foto do grupo', null=True, upload_to='fotos_equipe/', verbose_name='Foto da Equipe'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='anexo_extra1',
            field=models.FileField(blank=True, null=True, upload_to='anexos/', verbose_name='Anexo Extra 1'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='anexo_extra2',
            field=models.FileField(blank=True, null=True, upload_to='anexos/', verbose_name='Anexo Extra 2'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='anexo_extra3',
            field=models.FileField(blank=True, null=True, upload_to='anexos/', verbose_name='Anexo Extra 3'),
        ),
        
        # Criar modelo Badge
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Badge')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('icone', models.CharField(default='🏆', help_text='Emoji que representa a badge', max_length=50, verbose_name='Ícone (Emoji)')),
                ('pontos', models.IntegerField(default=10, help_text='Pontos ganhos ao conquistar esta badge', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Pontos')),
                ('criterio', models.CharField(choices=[('primeira_observacao', 'Primeira Observação Criada'), ('cinco_observacoes', '5 Observações Criadas'), ('fase1_completa', 'Fase 1 Aprovada'), ('fase3_completa', 'Fase 3 Aprovada'), ('fase6_completa', 'Fase 6 Aprovada'), ('projeto_concluido', 'Projeto Concluído'), ('primeira_foto', 'Primeira Foto Anexada'), ('explorador', 'Observações com Geolocalização'), ('colaborador', 'Membro de Grupo'), ('lider', 'Líder de Grupo')], max_length=50, unique=True, verbose_name='Critério')),
                ('ativa', models.BooleanField(default=True, verbose_name='Ativa')),
                ('criada_em', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Badge',
                'verbose_name_plural': 'Badges',
                'ordering': ['nome'],
            },
        ),
        
        # Criar modelo UsuarioBadge
        migrations.CreateModel(
            name='UsuarioBadge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conquistada_em', models.DateTimeField(auto_now_add=True, verbose_name='Conquistada em')),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conquistadores', to='core.badge', verbose_name='Badge')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='badges_conquistadas', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Badge do Usuário',
                'verbose_name_plural': 'Badges dos Usuários',
                'ordering': ['-conquistada_em'],
                'unique_together': {('usuario', 'badge')},
            },
        ),
        
        # Criar modelo PontuacaoGrupo
        migrations.CreateModel(
            name='PontuacaoGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontos_totais', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Pontos Totais')),
                ('atualizada_em', models.DateTimeField(auto_now=True, verbose_name='Atualizada em')),
                ('grupo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pontuacao', to='core.grupo', verbose_name='Grupo')),
            ],
            options={
                'verbose_name': 'Pontuação do Grupo',
                'verbose_name_plural': 'Pontuações dos Grupos',
                'ordering': ['-pontos_totais'],
            },
        ),
    ]

