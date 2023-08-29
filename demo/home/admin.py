from django.contrib import admin
from .models import library

# Register your models here.
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('library_id', 'name')
    search_fields = ['name']
    list_filter = ('library_id', 'name')
admin.site.register(library, LibraryAdmin)