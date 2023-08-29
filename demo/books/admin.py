from django.contrib import admin
from .models import books

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'library_id', 'name', 'age', 'bookfile')
    search_fields = ['name']
    list_filter = ('book_id', 'library_id', 'name', 'age')

admin.site.register(books, BookAdmin)