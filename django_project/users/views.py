from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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
    # these are model forms that are expecting to be working on specific model
    # so we can populate these forms just by passing the instance of object it expects
    u_form = UserUpdateForm(instance=request.user)
    # with this userform will have username and email filled in and profileform will have image filled in
    p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    # passing the context into templates so we can access these forms
    return render(request, 'users/profile.html', context)