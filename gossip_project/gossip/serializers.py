from rest_framework import serializers  # DRF serializers - translates models to JSON
from .models import Gossip  # Import our Gossip model
from django.contrib.auth.models import User  # Django's User model

# 💅 Gossip Serializer - packages gossip data into JSON format
# Think of it like wrapping your tea in a pretty little box for delivery!
class GossipSerializer(serializers.ModelSerializer):
    """
    Serializes the Gossip model to/from JSON.
    
    This is what transforms database rows into delicious JSON packets
    that can be sent over the internet. Like packaging gossip texts!
    """
    
    # 📝 Read-only field showing who posted the gossip
    # It will display the username automatically
    posted_by = serializers.ReadOnlyField(source='posted_by.username')
    
    # ⏰ Read-only field showing when it was posted
    # You can't manually set this - it's automatic!
    created_at = serializers.ReadOnlyField()
    
    class Meta:
        """
        Metadata for the serializer.
        Tells DRF which model to serialize and which fields to include.
        """
        # The model we're serializing
        model = Gossip
        
        # Fields to include in the API response
        # These are ALL the fields from our Gossip model!
        fields = ['id', 'title', 'content', 'posted_by', 'created_at']
        
        # Alternative: use '__all__' to include every field automatically
        # fields = '__all__'
    
    # 🔍 Optional: Add custom validation here if needed
    # For example, you could validate that titles aren't offensive
    def validate_title(self, value):
        """
        Custom validation for the title field.
        You could add checks here (e.g., no bad words!).
        """
        # For now, we'll keep it simple
        return value
