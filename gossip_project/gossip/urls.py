# 🎭 URL Configuration for the Gossip App
# Maps URLs to our API views - like a map to all the tea spots!

from django.urls import path  # For defining URL patterns
from .views import (
    GossipListAPIView,    # View to list all gossip
    GossipCreateAPIView,  # View to create new gossip
)

# 💅 App name - helps organize URLs in big projects
# We can refer to this as 'gossip' when reversing URLs
app_name = 'gossip'

# 🔥 URL Patterns - where the magic happens!
# Each pattern maps a URL to a view class
urlpatterns = [
    # 📰 GET /api/gossip/ - List ALL gossip posts
    # Like scrolling through the rumor mill feed
    # Anyone with a JWT token can see what's trending!
    path('', GossipListAPIView.as_view(), name='gossip-list'),
    
    # ✨ POST /api/gossip/new/ - Create NEW gossip
    # Time to spill some fresh tea!
    # Only authenticated users can drop new rumors
    path('new/', GossipCreateAPIView.as_view(), name='gossip-create'),
]

# 📝 Quick Reference:
# -------------------
# Full URLs when combined with project urls.py:
# - GET  /api/gossip/       → List all gossip (needs JWT token)
# - POST /api/gossip/new/   → Create new gossip (needs JWT token)
#
# How to use in Postman:
# 1. Get your JWT token first from /api/token/
# 2. Add header: Authorization: Bearer <your_token>
# 3. Make requests to these endpoints!
