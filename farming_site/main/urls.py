from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('content/', views.content, name='contents'),
    path('oders/', views.oders, name='oders'),
    path('add/', views.add_item, name='add'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)