from typing import Any, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Post

# blog -> templates -> blog -> template.html

# Create your views here.

#function based views -> render page and explicitly pass information
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# class based views, we are just setting variables -> they have a lot more built in functionalities
class PostListView(ListView):
    model = Post 
    template_name = 'blog/home.html' # django looks for template -> <app>/<model>_<view_type>.html
    # either we can create one with the name or change the template_name
    context_object_name = 'posts' # by default list view calls this variable object list instead of post
    ordering = ['-date_posted']
    paginate_by = 5
    

# Displays only the blogs by the selected user 
class UserPostListView(ListView):
    # When we create a new url pattern for this, we will specify username and url pattern itself
    model = Post 
    template_name = 'blog/user_posts.html' 
    context_object_name = 'posts'
    paginate_by = 5
    
    # In order to modify the query set that this list view returns
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) # kwargs is query parameters
        return Post.objects.filter(author=user).order_by('-date_posted')
    
    
# Provides Detail View for Any Blog
class PostDetailView(DetailView):
    model = Post
    
    
# LoginRequiredMixin provides functionality that user must be logged in to access the view for creating blog (class-based)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        # form that you are submitting, take that instance and set the author = current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form) # runs form_valid method on our parent class
    

# Now that we inherit UserPassesTestMixin, we can create a function test_func that UserPassesTestMixin will run in order to see if user passes a certain test condition
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def test_func(self):
        #  we want the exact post we are currently updating 
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# We want user to be logged in as well as be the author for the post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # We need to add a success url attribute to redirect to the page after deletion
    success_url = '/'
    
    # Same test function
    def test_func(self):
        # parenthesis is important to treat it as a method, else it gets treated as an attribute
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')