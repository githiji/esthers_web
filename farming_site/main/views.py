from django.shortcuts import render


# Create your views here.
def home(request):
   return render( request,'main/home.html', {})

def content(request):
    return render( request, "main/content.html", {})
def contact(request):
    pass

def about(request):
    pass


def oders(request):
    pass