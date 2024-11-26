from django.shortcuts import render,redirect
from .models import Farm , Crop


# Create your views here.
def home(request):
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
        if request.POST.get('add_crop'):
            crop_name = request.POST.get('crops')
            farm_size = request.POST.get('farm_size')
            quantity = request.POST.get('quantity')
            price = request.POST.get('price')
            save_crop = Crop(crop_name=crop_name,crop_quantity=quantity,crop_price=price)
            save_farm = Farm(farm_size=farm_size)
            save_crop.save()
            save_farm.save()
            return redirect('content')

    return render(request,'main/add_item.html',{})