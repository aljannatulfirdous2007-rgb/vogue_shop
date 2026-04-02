# 💅 Gossip Project - Complete Setup Script
# This script sets up the entire project from scratch!
# Run this if you want to start fresh.

Write-Host "🎭 Starting Gossip Project Setup..." -ForegroundColor Cyan
Write-Host ""

# Step 1: Check Python installation
Write-Host "🐍 Checking Python installation..." -ForegroundColor Yellow
try {
    python --version
    Write-Host "✅ Python found!" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found! Please install Python 3.8+ first." -ForegroundColor Red
    exit 1
}

Write-Host ""

# Step 2: Create virtual environment (if it doesn't exist)
$VENV_PATH = "c:\Users\Al jannatul firdous\gossip_env"
if (-Not (Test-Path $VENV_PATH)) {
    Write-Host "📦 Creating virtual environment at $VENV_PATH..." -ForegroundColor Yellow
    python -m venv $VENV_PATH
    Write-Host "✅ Virtual environment created!" -ForegroundColor Green
} else {
    Write-Host "✅ Virtual environment already exists!" -ForegroundColor Green
}

Write-Host ""

# Step 3: Activate virtual environment
Write-Host "🔌 Activating virtual environment..." -ForegroundColor Yellow
& "$VENV_PATH\Scripts\Activate.ps1"
Write-Host "✅ Virtual environment activated!" -ForegroundColor Green

Write-Host ""

# Step 4: Install dependencies
Write-Host "📥 Installing dependencies (django, djangorestframework, djangorestframework-simplejwt)..." -ForegroundColor Yellow
pip install django djangorestframework djangorestframework-simplejwt
Write-Host "✅ Dependencies installed!" -ForegroundColor Green

Write-Host ""

# Step 5: Navigate to project directory
$PROJECT_PATH = "c:\Users\Al jannatul firdous\my_unique_django_project\gossip_project"
if (-Not (Test-Path $PROJECT_PATH)) {
    Write-Host "📁 Creating project directory..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $PROJECT_PATH | Out-Null
    
    Set-Location $PROJECT_PATH
    
    Write-Host "🏗️ Creating Django project..." -ForegroundColor Yellow
    django-admin startproject gossip_project_core .
    Write-Host "✅ Django project created!" -ForegroundColor Green
    
    Write-Host "📝 Creating gossip app..." -ForegroundColor Yellow
    python manage.py startapp gossip
    Write-Host "✅ Gossip app created!" -ForegroundColor Green
} else {
    Write-Host "✅ Project already exists! Skipping creation..." -ForegroundColor Green
    Set-Location $PROJECT_PATH
}

Write-Host ""

# Step 6: Run migrations
Write-Host "🗄️ Running database migrations..." -ForegroundColor Yellow
python manage.py makemigrations
python manage.py migrate
Write-Host "✅ Migrations complete!" -ForegroundColor Green

Write-Host ""

# Step 7: Create superuser (if doesn't exist)
Write-Host "👑 Creating superuser 'QueenBee'..." -ForegroundColor Yellow
try {
    $existingUser = python -c "from django.contrib.auth.models import User; User.objects.get(username='QueenBee')" 2>&1
    Write-Host "✅ Superuser already exists!" -ForegroundColor Green
} catch {
    python manage.py createsuperuser --username QueenBee --email queenbee@plastics.com --noinput
    # Set password using our script
    python set_password.py
    Write-Host "✅ Superuser created!" -ForegroundColor Green
}

Write-Host ""
Write-Host "🎉 Setup Complete!" -ForegroundColor Cyan
Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""
Write-Host "🚀 Next Steps:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Start the server:" -ForegroundColor White
Write-Host "   python manage.py runserver" -ForegroundColor Cyan
Write-Host ""
Write-Host "2. Open your browser to:" -ForegroundColor White
Write-Host "   http://127.0.0.1:8000/" -ForegroundColor Cyan
Write-Host ""
Write-Host "3. Access Django admin:" -ForegroundColor White
Write-Host "   http://127.0.0.1:8000/admin/" -ForegroundColor Cyan
Write-Host "   Username: QueenBee" -ForegroundColor Cyan
Write-Host "   Password: PlasticsRule2024!" -ForegroundColor Cyan
Write-Host ""
Write-Host "4. Read the documentation:" -ForegroundColor White
Write-Host "   Open README.md in your project folder" -ForegroundColor Cyan
Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""
Write-Host "💅 Time to spill some tea! ☕" -ForegroundColor Magenta
Write-Host ""
