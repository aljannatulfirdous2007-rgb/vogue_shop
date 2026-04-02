from django.contrib import admin
from .models import Gossip  # Import our Gossip model

# Register your models here.

# 💅 Gossip Admin Configuration
# This is the "backstage" where you can manage all the gossip!
# Access it at: http://localhost:8000/admin/

@admin.register(Gossip)  # Decorator that registers the model automatically
class GossipAdmin(admin.ModelAdmin):
    """
    Customizes how Gossip appears in Django admin panel.
    Makes it easy to view and manage all the tea! ☕
    """
    
    # 👀 What columns to display in the list view
    # Shows at a glance: title, who posted it, and when
    list_display = ['title', 'posted_by', 'created_at']
    
    # 🔍 Add filter options on the right sidebar
    # Lets you filter by user (who posted what)
    list_filter = ['posted_by', 'created_at']
    
    # 🔎 Add a search bar to search through gossip
    # Search by title or content - find any tea quickly!
    search_fields = ['title', 'content']
    
    # 📅 Order by date by default (newest first)
    # Same ordering as the model - keeps it consistent
    ordering = ['-created_at']
    
    # 📖 How many items to show per page
    # Don't overwhelm with too much at once!
    list_per_page = 20
    
    # 💡 Optional: Make certain fields read-only
    # You can't change who posted it or when - that's history!
    readonly_fields = ['posted_by', 'created_at']
