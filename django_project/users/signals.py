# signal that gets fired after an object is saved
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# if user is created/saved -> post_save signal is sent, received by receiver
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # if user is created, create a profileobject with user=instance of user that was created
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
# **kwargs just accepts any more keyword arguments
def create_profile(sender, instance, **kwargs):
    instance.profile.save()