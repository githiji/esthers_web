from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'register/register.html', {'form': form})

# Create your views here.
