from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'register/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/content')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'register/login.html', {})
    else:
        return render(request, 'register/login.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('/')

# Create your views here.
