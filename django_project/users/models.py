from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # CASCADE means if user is deleted, then also ddelete the profile, but not vice versa
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    # if we don't have the __str__ method, it is just going to print Profile object
    def __str__(self):
        return f'{self.user.username} Profile'