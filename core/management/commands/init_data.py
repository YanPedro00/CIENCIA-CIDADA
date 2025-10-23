from django.core.management.base import BaseCommand
from core.models import Usuario


class Command(BaseCommand):
    help = 'Inicializa dados de teste no banco de dados'

    def handle(self, *args, **kwargs):
        # Criar admin
        if not Usuario.objects.filter(username='admin').exists():
            Usuario.objects.create_superuser(
                username='admin',
                email='admin@cienciacidada.com',
                password='admin123456',
                first_name='Admin',
                last_name='Sistema',
                tipo='professor'
            )
            self.stdout.write(self.style.SUCCESS('✅ Admin criado!'))
        else:
            self.stdout.write(self.style.WARNING('⚠️  Admin já existe'))
        
        # Criar professor de teste
        if not Usuario.objects.filter(username='prof.silva').exists():
            Usuario.objects.create_user(
                username='prof.silva',
                email='silva@escola.com',
                password='prof123',
                first_name='Maria',
                last_name='Silva',
                tipo='professor'
            )
            self.stdout.write(self.style.SUCCESS('✅ Prof. Silva criado!'))
        else:
            self.stdout.write(self.style.WARNING('⚠️  Prof. Silva já existe'))
        
        # Criar estudantes de teste
        estudantes = [
            {'username': 'joao.santos', 'first_name': 'João', 'last_name': 'Santos'},
            {'username': 'ana.costa', 'first_name': 'Ana', 'last_name': 'Costa'},
            {'username': 'pedro.oliveira', 'first_name': 'Pedro', 'last_name': 'Oliveira'},
            {'username': 'maria.souza', 'first_name': 'Maria', 'last_name': 'Souza'},
        ]
        
        for dados in estudantes:
            if not Usuario.objects.filter(username=dados['username']).exists():
                Usuario.objects.create_user(
                    username=dados['username'],
                    email=f"{dados['username']}@email.com",
                    password='aluno123',
                    first_name=dados['first_name'],
                    last_name=dados['last_name'],
                    tipo='estudante'
                )
                self.stdout.write(self.style.SUCCESS(f'✅ {dados["first_name"]} {dados["last_name"]} criado!'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠️  {dados["first_name"]} {dados["last_name"]} já existe'))
        
        self.stdout.write(self.style.SUCCESS('\n🎉 Inicialização concluída!'))

