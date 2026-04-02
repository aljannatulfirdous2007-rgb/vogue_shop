#!/usr/bin/env python
"""
💅 Quick script to set superuser password
Run this with: python set_password.py
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
    # Set the password - this is for development only!
    user.set_password('PlasticsRule2024!')
    user.save()
    print("✅ Password set successfully for QueenBee!")
    print("📝 Login credentials:")
    print(f"   Username: QueenBee")
    print(f"   Password: PlasticsRule2024!")
    print("\n💡 Remember to change this in production!")
except User.DoesNotExist:
    print("❌ User 'QueenBee' not found. Please create the superuser first.")
