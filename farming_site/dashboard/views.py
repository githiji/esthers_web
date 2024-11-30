from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm

def dashboard(request):
    form = TweetForm()
    tweets = Tweet.objects.all().order_by('-created_at')

    if request.method == 'post':
        form = TweetForm(request.POST)
        if form.is_valid():
          tweet = form.save(commit=False)
          tweet.user = request.user
          tweet.save()
          return redirect('dashboard')

    return render(request, 'dashboard/dashboard.html', {'form':form, 'tweets':tweets})
# Create your views here.
