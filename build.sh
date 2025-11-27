#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "📁 Collecting static files..."
python manage.py collectstatic --no-input

echo "✅ Build complete!"
echo "ℹ️  Migrations will run during startup (when database is available)"

