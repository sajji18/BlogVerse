from django.contrib import admin
from .models import Post

# In order to see your models in the admin page, register them in admin.py

# Register your models here.
admin.site.register(Post)
