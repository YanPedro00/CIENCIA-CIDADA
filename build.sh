#!/usr/bin/env bash
# exit on error
set -o errexit

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "📁 Collecting static files..."
python manage.py collectstatic --no-input

echo "🔄 Running migrations..."
python manage.py migrate --noinput --verbosity 2

echo "👥 Creating initial data..."
python manage.py init_data

echo "✅ Build complete!"

