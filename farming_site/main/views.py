from django.shortcuts import render,redirect
from .models import Farm , Crop
from .forms import CropForm

# Create your views here.
def home(request):
   if request.method == 'POST':
       if request.POST.get('login'):
           return redirect('/register/login')
       elif request.POST.get('singup'):
           return redirect('/register')
   return render( request,'main/home.html', {})

def content(request):
    crops = Crop.objects.all()
    return render( request, "main/content.html", {'crops':crops} )
def content_info(request, id ):
   item = Crop.objects.get(id=id)
   if request.method == 'POST':
       if request.POST.get('comment')=='comment':
           req = request.POST.get('comment')
           save_comment= Crop(comment=req)
           save_comment.save()
   return render( request, "main/content_info.html", {'item':item} )

def about(request):
    pass


def oders(request):
    pass

def add_item(request):
    if request.method == 'POST':
        form = CropForm(request.POST, request.FILES)
        if form.is_valid():
              # Add parentheses to call the method
            # Extract cleaned data from the form
            if request.POST.get('add_crop'):
                name = form.cleaned_data.get('name')
                price = form.cleaned_data.get('price')
                image = form.cleaned_data.get('image')
                quantity = form.cleaned_data.get('quantity')
                second_image = form.cleaned_data.get('second_image')
                # Save the data to the database
                saved_crop = Crop(
                    name=name,
                    price=price,
                    image=image,
                    quantity=quantity  
                )
                saved_crop.save()

                return redirect('/content')  # Redirect to the desired page
            elif request.POST.get('delete_crop'):
                crop_name = request.POST.get('crop_name')
                Crop.objects.filter(name=crop_name).delete()
            return redirect('/content')

    else:
        form = CropForm()

    return render(request, 'main/add_item.html', {'form': form})

