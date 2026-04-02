#!/usr/bin/env python
"""
🔐 Force reset password for firdous user
Run this with: python force_reset_password.py
"""

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gossip_project_core.settings')
django.setup()

from django.contrib.auth.models import User

print("🔐 Resetting password for 'firdous'...\n")

try:
    # Get the user
    user = User.objects.get(username='firdous')
    
    # Force set the password (this hashes it properly)
    user.set_password('firdous')
    
    # Ensure all flags are correct
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.email = 'firdous@admin.com'
    
    # Save to database
    user.save()
    
    print("✅ Password reset successful!")
    print("\n📝 LOGIN CREDENTIALS:")
    print(f"   Username: firdous")
    print(f"   Email: firdous@admin.com")
    print(f"   Password: firdous")
    print("\n💡 Try logging in again at: http://127.0.0.1:8000/admin/")
    print("\n⚠️ If still having issues:")
    print("   1. Clear your browser cache and cookies")
    print("   2. Try using an incognito/private window")
    print("   3. Restart the Django server")
    
except User.DoesNotExist:
    print("❌ User 'firdous' not found!")
    print("Creating new superuser...")
    User.objects.create_superuser(
        username='firdous',
        email='firdous@admin.com',
        password='firdous'
    )
    print("✅ New superuser created!")
