#!/bin/bash
# Script de comandos para usar no PythonAnywhere

echo "=== Comandos para Deploy no PythonAnywhere ==="
echo ""
echo "1. Criar ambiente virtual:"
echo "mkvirtualenv --python=/usr/bin/python3.10 ciencia_cidada"
echo ""
echo "2. Instalar dependências:"
echo "pip install django==4.2.7 pillow python-decouple"
echo ""
echo "3. Configurar banco de dados:"
echo "python manage.py migrate"
echo ""
echo "4. Criar superusuário:"
echo "python manage.py createsuperuser"
echo ""
echo "5. Coletar arquivos estáticos:"
echo "python manage.py collectstatic --noinput"
echo ""
echo "=== Configuração WSGI ==="
echo "Caminho do projeto: /home/yanpedro@WPA10PE09SRVWD/ciencia-cidada"
echo "Caminho do virtualenv: /home/yanpedro@WPA10PE09SRVWD/.virtualenvs/ciencia_cidada"

