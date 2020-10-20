#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.models import Profile
from users.forms import ProfileForm, SignUpForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid password or username',})
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', context={'form': form})




@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website'] 
            profile.biography = data['biography'] 
            profile.phone_number = data['phone_number'] 
            profile.picture = data['picture']
            profile.save()
            return redirect('update_profile')
    else:
        form = ProfileForm
    return render(request, 'users/update_profile.html', {'user': request.user, 'profile': profile, 'form': form})