from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
    )
from . import views

urlpatterns = [
    # django has already processed the /blog/ part, now just see the remaining part
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # Since we are providing the primary key, we do not need to add another template
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # template it expects is just a form that asks for confirmation
    path('about/', views.about, name='blog-about'),
]