#!/usr/bin/env python
"""
🔍 Debug script to check user accounts
Run this with: python debug_users.py
"""

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gossip_project_core.settings')
django.setup()

from django.contrib.auth.models import User

print("🔍 Checking all users in database...\n")

# Get all users
users = User.objects.all()

if not users.exists():
    print("❌ No users found in database!")
else:
    print(f"✅ Found {users.count()} user(s):\n")
    
    for user in users:
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")
        print(f"Is Staff: {user.is_staff}")
        print(f"Is Superuser: {user.is_superuser}")
        print(f"Active: {user.is_active}")
        print("-" * 40)

# Try to find firdous specifically
print("\n🔍 Looking for 'firdous' user...")
try:
    firdous_user = User.objects.get(username='firdous')
    print(f"✅ Found 'firdous'!")
    print(f"   Email: {firdous_user.email}")
    print(f"   Is Staff: {firdous_user.is_staff}")
    print(f"   Is Superuser: {firdous_user.is_superuser}")
except User.DoesNotExist:
    print("❌ User 'firdous' not found!")
    print("\nCreating new superuser 'firdous' now...")
    try:
        firdous_user = User.objects.create_superuser(
            username='firdous',
            email='firdous@admin.com',
            password='firdous',
        )
        print("✅ Superuser 'firdous' created successfully!")
        print(f"   Email: {firdous_user.email}")
        print(f"   Password: firdous")
    except Exception as e:
        print(f"❌ Error creating user: {e}")
