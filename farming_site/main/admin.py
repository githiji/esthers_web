from django.contrib import admin
from .models import Farm , Crop

class farmadmin(admin.ModelAdmin):
    list_display = ('name','farm_name','farm_size')

admin.site.register(Farm, farmadmin)
admin.site.register(Crop)
# Register your models here.
