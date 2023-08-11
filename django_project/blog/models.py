from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # one author -> many post, one post -> one author. One to Many Relationship(Foreign Key)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
    # redirect redirects you to a specific route, wherease reverse return full url to that route as string
    # This method returns the path to any specific instance
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    