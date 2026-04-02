#!/usr/bin/env python
"""
💅 Update superuser credentials to: firdous / firdous
Run this with: python update_credentials.py
"""

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gossip_project_core.settings')
django.setup()

from django.contrib.auth.models import User

print("🔐 Updating superuser credentials...\n")

# Try to get existing QueenBee user or create new one
try:
    # First, check if 'firdous' already exists
    user = User.objects.get(username='firdous')
    print("✅ User 'firdous' already exists. Updating password...")
    user.set_password('firdous')
    user.email = 'firdous@admin.com'
    user.is_staff = True
    user.is_superuser = True
    user.save()
    
except User.DoesNotExist:
    # Create new superuser
    print("📝 Creating new superuser 'firdous'...")
    user = User.objects.create_superuser(
        username='firdous',
        email='firdous@admin.com',
        password='firdous',
        is_staff=True,
        is_superuser=True
    )
    print("✅ Superuser created successfully!")

print("\n" + "="*50)
print("🎉 CREDENTIALS UPDATED SUCCESSFULLY!")
print("="*50)
print("\n📝 NEW LOGIN DETAILS:")
print("\n   Username: firdous")
print("   Password: firdous")
print("   Email: firdous@admin.com")
print("\n🌐 Admin Panel: http://127.0.0.1:8000/admin/")
print("\n💡 You can now login with these credentials!")
print("="*50)
