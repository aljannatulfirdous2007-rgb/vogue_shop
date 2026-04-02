#!/usr/bin/env python
"""
💅 Fix superuser email login issue
Run this with: python fix_admin_login.py
"""

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gossip_project_core.settings')
django.setup()

from django.contrib.auth.models import User

# Get the QueenBee user
try:
    user = User.objects.get(username='QueenBee')
    
    # Make sure email is set and user is staff/superuser
    user.email = 'queenbee@plastics.com'
    user.is_staff = True
    user.is_superuser = True
    user.save()
    
    print("✅ Superuser updated successfully!")
    print("\n📝 You can now login with EITHER:")
    print("\n   Option 1 - Username:")
    print(f"   Username: QueenBee")
    print(f"   Password: PlasticsRule2024!")
    print("\n   Option 2 - Email:")
    print(f"   Email: queenbee@plastics.com")
    print(f"   Password: PlasticsRule2024!")
    print("\n💡 Try refreshing the admin page and logging in again!")
    
except User.DoesNotExist:
    print("❌ User 'QueenBee' not found. Please run migrations and setup first.")
