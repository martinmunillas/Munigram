#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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