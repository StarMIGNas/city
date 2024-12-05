from django.contrib import admin
from .models import City

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    ordering = ['time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 5
admin.site.register(City, CityAdmin)