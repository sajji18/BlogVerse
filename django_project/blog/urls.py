from django.urls import path
from . import views

urlpatterns = [
    # django has already processed the /blog/ part, now just see the remaining part
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]