from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# flash messages -> messages.something --> something = debug, info, success, warning, error

# Create your views here.
def register(request):
    if request.method == 'POST': 
        # form is instantiated and populated with data from request.POST   
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', {'form': form})

# add functionality that user must be logged in to view this page
@login_required
def profile(request):
    return render(request, 'users/profile.html')