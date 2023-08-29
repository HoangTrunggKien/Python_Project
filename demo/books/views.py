from django.shortcuts import render, redirect
from .models import books as book_model
from home.models import library as library_model

# Create your views here.
def get_books(request, id):
    book_list = book_model.objects.filter(library_id = id)
    library = library_model.objects.get(library_id = id)
    return render(request, 'books.html', {'book_list' : book_list, 'library' : library})

def get_book_form(request):
    library_list = library_model.objects.filter()
    return render(request, 'bookForm.html', {'library_list' : library_list})

def add_book(request):
    if request.method == 'POST':
        library_id = request.POST['library']
        name = request.POST['fullName']
        age = request.POST['age']
        bookfile = request.FILES['bookfile']

        library = library_model.objects.get(library_id = library_id)

        book = book_model.objects.create(library_id = library, name = name, age = age, bookfile = bookfile)
        book.save()
        return redirect('/library/' + str(library_id))
    else:
        return render(request, 'error.html')



