from django.shortcuts import render

# 🎭 DRF imports - our API toolkit!
from rest_framework.views import APIView  # Base class for all views
from rest_framework.response import Response  # For sending JSON responses
from rest_framework import status  # HTTP status codes (200, 201, 400, etc.)
from rest_framework.permissions import IsAuthenticated  # VIP-only access!

# 💅 Our Gossip model and serializer
from .models import Gossip
from .serializers import GossipSerializer

# Create your views here.

# 📰 List All Gossip - GET /api/gossip/
# Like opening the cafeteria to hear all the latest tea!
class GossipListAPIView(APIView):
    """
    API endpoint to LIST all gossip posts.
    
    🔐 Permission: IsAuthenticated (must have JWT token)
    📍 Endpoint: GET /api/gossip/
    
    This is like scrolling through everyone's gossip posts!
    Only people with valid JWT tokens can see the tea ☕
    """
    
    # 🔐 Require authentication for this endpoint
    # No token? No entry! Like being on the Plastics' guest list.
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """
        Handle GET requests to retrieve all gossip.
        
        Steps:
        1. Fetch ALL gossip from database (newest first)
        2. Serialize it (convert to JSON)
        3. Return as response
        
        Returns:
        - 200 OK: List of all gossip posts
        """
        # 👀 Get all gossip posts, ordered by newest first
        # The '-' before 'created_at' means descending order
        gossips = Gossip.objects.all().order_by('-created_at')
        
        # 📦 Serialize the data (convert to JSON-friendly format)
        # many=True because we're serializing multiple objects
        serializer = GossipSerializer(gossips, many=True)
        
        # 📤 Return the serialized data as a JSON response
        # status.HTTP_200_OK means "Everything's cool, here's your data!"
        return Response(serializer.data, status=status.HTTP_200_OK)


# ✨ Create New Gossip - POST /api/gossip/new/
# Time to spill some fresh tea!
class GossipCreateAPIView(APIView):
    """
    API endpoint to CREATE a new gossip post.
    
    🔐 Permission: IsAuthenticated (must have JWT token)
    📍 Endpoint: POST /api/gossip/new/
    
    This is where YOU become the source of the tea!
    Post your own spicy gossip to share with everyone.
    """
    
    # 🔐 Require authentication for this endpoint
    # You need to be logged in to spread rumors!
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        """
        Handle POST requests to create new gossip.
        
        Expected data format (JSON):
        {
            "title": "Regina Got Dumped!",
            "content": "She just found out her boyfriend..."
        }
        
        Note: posted_by is automatically set to current user!
        
        Returns:
        - 201 Created: Successfully created new gossip
        - 400 Bad Request: Invalid or missing data
        """
        # 📋 Get the data sent by the user
        # request.data contains the JSON payload
        data = request.data
        
        # 🎯 Add the current user as the poster
        # The user is extracted from the JWT token automatically!
        # This ensures you can't pretend to be someone else
        data['posted_by'] = request.user.id
        
        # 📦 Create a serializer instance with the data
        serializer = GossipSerializer(data=data)
        
        # ✅ Check if the data is valid
        # The serializer will run validations automatically
        if serializer.is_valid():
            # 💾 Save to database
            # This creates a new Gossip object in the database
            serializer.save()
            
            # 🎉 Success! Return the created gossip
            # status.HTTP_201_CREATED means "Your creation was successful!"
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        # ❌ Validation failed - return errors
        # status.HTTP_400_BAD_REQUEST means "Something's wrong with your data!"
        return Response(
            serializer.errors,  # Show what went wrong
            status=status.HTTP_400_BAD_REQUEST
        )
