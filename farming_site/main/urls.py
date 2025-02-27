from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('content/', views.content, name='contents'),
    path('oders/', views.oders, name='oders'),
    path('add/', views.add_item, name='add'),
    path('content/<int:id>/', views.content_info, name='content_info'),
]