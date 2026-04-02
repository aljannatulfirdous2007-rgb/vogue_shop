from django.db import models
from django.conf import settings  # Import settings to get custom user model

# Create your models here.

# 💅 Gossip Model - where all the tea is spilled!
# This is where we store all the juicy gossip posts
class Gossip(models.Model):
    """
    A piece of gossip posted by a user. 
    Think of it like a post in the Mean Girls cafeteria!
    
    Fields:
    - title: The headline of your gossip (max 200 characters)
    - content: The full story - spill ALL the tea!
    - posted_by: Who spilled the tea? (link to User)
    - created_at: When was the gossip posted? (automatically set)
    """
    
    # 📰 Title - make it catchy! Like "Regina Got Dumped!"
    title = models.CharField(
        max_length=200, 
        help_text="The headline of your gossip - make it fetch!"
    )
    
    # 📝 Content - the full story, every delicious detail
    content = models.TextField(
        help_text="Spill ALL the tea! Don't leave out any details."
    )
    
    # 👤 Posted By - who's brave enough to share this?
    # ForeignKey means one User can post many pieces of gossip
    # on_delete=models.CASCADE means if user is deleted, their gossip disappears too
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use custom user model
        on_delete=models.CASCADE,
        related_name='gossips',  # Lets us do user.gossips.all()
        help_text="The person who spilled the tea ☕"
    )
    
    # ⏰ Created At - timestamp automatically added when created
    # auto_now_add=True means it's set once when the object is created
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="When this spicy tea was served"
    )
    
    def __str__(self):
        """
        Returns a string representation of the gossip.
        This is what you'll see in the admin panel.
        Example: "Regina Got Dumped - posted by QueenBee"
        """
        return f"{self.title} - posted by {self.posted_by.username}"
    
    class Meta:
        """
        Metadata options for the Gossip model.
        This controls how gossip is ordered and displayed.
        """
        # Order by newest first (like a social media feed)
        ordering = ['-created_at']
        # Pretty name for the model in admin panel
        verbose_name = 'Gossip Post'
        verbose_name_plural = 'All Gossip Posts'  # Yes, there will be many!
