from django.db import models

from django.db.models.functions import Lower 
from django.utils import timezone
from django.contrib.auth.models import User 
from django.utils.text import slugify
import time
from uiLibraries import extractColors

# new imports

from django.urls import reverse

from django.core.validators import MinValueValidator, MaxValueValidator


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

# core/models.py


class Blockchain(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='coin_images/' , default="airdropLogo.jpg", blank=True, null=True)
    description = models.CharField(max_length=255)
    ticker = models.CharField(max_length=25)
    def __str__(self):
            return self.name

class Event(models.Model):

    #airdrop = models.ForeignKey(Airdrop, on_delete=models.CASCADE, related_name='events')

    title = models.CharField(max_length=255)

    description = models.TextField(blank=True, null=True)

    start_date = models.DateField()

    end_date = models.DateField()

    start_time = models.TimeField(blank=True, null=True)

    end_time = models.TimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  
  


    
class Airdrop(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    ticker = models.CharField(default="",max_length=25)
    legibility = models.CharField(default="",max_length=5)
    difficulty = models.CharField(default="",max_length=7)
    startprice = models.FloatField()
    blockchain = models.ForeignKey(Blockchain,on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True, related_name='events')
    img = models.ImageField(upload_to='coin_images/' , default="/storage/emulated/0/airdrop_8290002-1.png", blank=True, null=True)
    contract_add = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    description = models.TextField(blank=True , null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    followers = models.IntegerField()
    integrity_score = models.FloatField()
    slug = models.SlugField(unique=True, blank=True, null=True,  max_length=50)
    color = models.JSONField(default=dict,blank=True, null=True)

    #recently added
    # New fields

    category = models.CharField(max_length=50, choices=[

        ('DeFi', 'DeFi'),

        ('NFT', 'NFT'),

        ('Gaming', 'Gaming'),

        ('Others', 'Others')

    ],default='Others')

    

    token_type = models.CharField(max_length=50, choices=[

        ('ERC-20', 'ERC-20'),

        ('BEP-20', 'BEP-20'),

        ('SPL', 'SPL'),

        ('Others', 'Others')

    ],default='Others')

    


    creator = models.CharField(default=" ",max_length=255)

    partners = models.JSONField(default=dict, blank=True, null=True)


    timeline = models.JSONField(default=dict, blank=True, null=True)

    token_allocation = models.JSONField(default=dict, blank=True, null=True)

    vesting_schedule = models.JSONField(default=dict, blank=True, null=True)

    lockup_periods = models.JSONField(default=dict, blank=True, null=True)

    token_utility = models.JSONField(default=dict, blank=True, null=True)

    community_size = models.IntegerField(blank=True, null=True)

    social_media_metrics = models.JSONField(default=dict, blank=True, null=True)

    website_traffic = models.JSONField(default=dict, blank=True, null=True)

    faqs = models.JSONField(default=dict, blank=True, null=True)

    terms_conditions = models.TextField(blank=True, null=True)

    privacy_policy = models.TextField(blank=True, null=True)

    tokenomics = models.JSONField(default=dict, blank=True, null=True)

    roadmap = models.JSONField(default=dict, blank=True, null=True)

    team_info = models.JSONField(default=dict, blank=True, null=True)

    advisors = models.JSONField(default=dict, blank=True, null=True)



    investors = models.JSONField(default=dict, blank=True, null=True)


    airdrop_history = models.JSONField(default=dict, blank=True, null=True)

    testimonials = models.JSONField(default=dict, blank=True, null=True)

    ratings_reviews = models.JSONField(default=dict, blank=True, null=True)

    audit_reports = models.JSONField(default=dict, blank=True, null=True)

    token_listing = models.JSONField(default=dict, blank=True, null=True)

    localization = models.JSONField(default=dict, blank=True, null=True)

    user_guides = models.JSONField(default=dict, blank=True, null=True)

    updates_news = models.JSONField(default=dict, blank=True, null=True)

    compliance_info = models.JSONField(default=dict, blank=True, null=True)

    status = models.CharField(max_length=50, choices=[

        ('Upcoming', 'Upcoming'),

        ('Ongoing', 'Ongoing'),

        ('Completed', 'Completed')

    ],default='Ongoing')

    airdrop_type = models.CharField(max_length=50, choices=[

        ('Bounty', 'Bounty'),

        ('Giveaway', 'Giveaway'),

        ('Fork', 'Fork'),

        ('Others', 'Others')

    ], default='Others')

    eligibility_criteria = models.JSONField(default=dict, blank=True, null=True)

    claim_distribution = models.JSONField(default=dict, blank=True, null=True)

    user_interactions = models.JSONField(default=dict, blank=True, null=True)

    budget_funding = models.JSONField(default=dict, blank=True, null=True)

    token_price_market = models.JSONField(default=dict, blank=True, null=True)

    security_measures = models.JSONField(default=dict, blank=True, null=True)

    
        

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            # Ensure uniqueness
            counter = 1
            while Airdrop.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.name)}-{counter}"
                counter += 1
        # Assuming you have a function to extract colors from the image
        """
        colors = extractColors.extractColors(self.img.path)
        self.color = {
            'dominant_color': colors['dominant_color'],
            'progress_in_color': colors['lightest_color'],
            'progress_out_color': colors['darkest_color']
        }
        """
        #super(Airdrop, self).save(*args, **kwargs)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Task(models.Model):
    airdrop = models.ForeignKey(Airdrop, on_delete=models.CASCADE)
    description = models.TextField(blank=True , null=True)
    completed = models.BooleanField(default=False)


class FollowerProfile(models.Model):
    name = models.CharField(max_length=255)
    profile_url = models.CharField(max_length=255)
    follower_num = models.IntegerField()
    followed_airdrop = models.ManyToManyField(Airdrop)
    def __str__(self):
            return self.name
    

  
class ScopeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    telegram_number = models.CharField(max_length=20, blank=True)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    tracked_airdrops = models.TextField(blank=True)  # Consider using JSONField if you're using PostgreSQL

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_scope_user(sender, instance, created, **kwargs):
    if created:
        ScopeUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_scope_user(sender, instance, **kwargs):
    instance.scopeuser.save()
    
    

class Notification(models.Model):
    user = models.ForeignKey(ScopeUser, on_delete=models.CASCADE)
    airdrop = models.ForeignKey(Airdrop, on_delete=models.CASCADE)
    message = models.TextField(blank=True , null=True)
    sent = models.BooleanField(default=False)