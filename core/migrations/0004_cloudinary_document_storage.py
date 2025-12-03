# Generated manually for Cloudinary document storage

from django.db import migrations, models
import core.storage


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_entrega5_anexos_gamificacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='arquivo',
            field=models.FileField(blank=True, null=True, storage=core.storage.DocumentStorage(), upload_to='atividades/', verbose_name='Arquivo Anexo'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='anexo_extra1',
            field=models.FileField(blank=True, null=True, storage=core.storage.DocumentStorage(), upload_to='anexos/', verbose_name='Anexo Extra 1'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='anexo_extra2',
            field=models.FileField(blank=True, null=True, storage=core.storage.DocumentStorage(), upload_to='anexos/', verbose_name='Anexo Extra 2'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='anexo_extra3',
            field=models.FileField(blank=True, null=True, storage=core.storage.DocumentStorage(), upload_to='anexos/', verbose_name='Anexo Extra 3'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='apresentacao',
            field=models.FileField(blank=True, help_text='Slides da apresentação do projeto', null=True, storage=core.storage.DocumentStorage(), upload_to='apresentacoes/', verbose_name='Apresentação (PPT/PDF)'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='relatorio_final',
            field=models.FileField(blank=True, help_text='Documento completo do projeto', null=True, storage=core.storage.DocumentStorage(), upload_to='relatorios/', verbose_name='Relatório Final (PDF/DOCX)'),
        ),
    ]

