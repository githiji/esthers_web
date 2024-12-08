from django.shortcuts import render,redirect
from .models import Farm , Crop
from .forms import CropForm

# Create your views here.
def home(request):
   if request.method == 'POST':
       if request.POST.get('login'):
           return redirect('/login')
       elif request.POST.get('singup'):
           return redirect('/register')
   return render( request,'main/home.html', {})

def content(request):
    crops = Crop.objects.all()
    return render( request, "main/content.html", {'crops':crops} )
def contact(request):
    pass

def about(request):
    pass


def oders(request):
    pass

def add_item(request):
    if request.method == 'POST':
        form = CropForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('content')
    else:
        form = CropForm()

    return render(request,'main/add_item.html',{'form':CropForm()})


