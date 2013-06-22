#admin.py

from django.contrib import admin
from .models import Need

class NeedAdmin(admin.ModelAdmin):
    list_display = ['need', 'slug']
    
admin.site.register(Need, NeedAdmin)