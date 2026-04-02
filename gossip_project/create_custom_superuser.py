#!/usr/bin/env python
"""
🔐 Create Custom Superuser
Run this script and edit the username, email, and password below!
"""

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gossip_project_core.settings')
django.setup()

from django.contrib.auth.models import User

# ==================== EDIT THESE VALUES ====================
# Change these to whatever you want!
DESIRED_USERNAME = "your_username_here"      # ← Change this!
DESIRED_EMAIL = "your_email@example.com"     # ← Change this!
DESIRED_PASSWORD = "your_password_here"      # ← Change this!
# ===========================================================

print(f"🔐 Creating superuser: {DESIRED_USERNAME}...\n")

try:
    # Check if user already exists
    existing_user = User.objects.get(username=DESIRED_USERNAME)
    print(f"⚠️ User '{DESIRED_USERNAME}' already exists!")
    print("Updating password...")
    existing_user.set_password(DESIRED_PASSWORD)
    existing_user.email = DESIRED_EMAIL
    existing_user.is_staff = True
    existing_user.is_superuser = True
    existing_user.save()
    print(f"✅ Password updated for '{DESIRED_USERNAME}'!\n")
    
except User.DoesNotExist:
    # Create new superuser
    user = User.objects.create_superuser(
        username=DESIRED_USERNAME,
        email=DESIRED_EMAIL,
        password=DESIRED_PASSWORD,
    )
    print(f"✅ Superuser '{DESIRED_USERNAME}' created successfully!\n")

print("📝 LOGIN DETAILS:")
print(f"   Username: {DESIRED_USERNAME}")
print(f"   Email: {DESIRED_EMAIL}")
print(f"   Password: {DESIRED_PASSWORD}")
print(f"\n💡 Admin Panel: http://127.0.0.1:8000/admin/")
