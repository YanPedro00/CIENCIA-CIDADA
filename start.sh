#!/usr/bin/env bash
# Exit on error
set -e

echo "🚀 Starting Django deployment..."

echo "📦 Checking database connection..."
python manage.py check --database default

echo "📝 Creating migrations..."
python manage.py makemigrations --noinput

echo "🔄 Running migrations..."
python manage.py migrate --noinput --verbosity 2

echo "🏆 Creating badges..."
python manage.py criar_badges || echo "⚠️  Badges já existem ou comando falhou"

echo "👥 Creating initial users..."
python manage.py init_data

echo "✅ Setup complete! Starting Gunicorn..."
exec gunicorn config.wsgi --log-file -

