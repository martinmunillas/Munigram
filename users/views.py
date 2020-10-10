#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from users.models import Profile

def login_view(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            return redirect('feed')
        else:
            return render(req, 'users/login.html', {'error': 'Invalid password or username',})
    return render(req, 'users/login.html')

@login_required
def logout_view(req):
    logout(req)
    return redirect('login')

def signup_view(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        password_conf = req.POST['password_conf']
        if password != password_conf:
            return render(req, 'users/signup.html', {'error': 'Password confirmation should match'})
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(req, 'users/signup.html', {'error': 'That username already exists'})
        user.email = req.POST['email']
        user.first_name = req.POST['first_name']
        user.last_name = req.POST['last_name']
        user.save()

        profile = Profile(user=user)
        profile.save()
        return redirect('login')
           
    return render(req, 'users/signup.html')