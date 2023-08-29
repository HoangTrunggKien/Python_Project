from django.shortcuts import render
from .models import library as library_model
# Create your views here.
def get_home(request):
    library_list = library_model.objects.filter().order_by('library_id')
    return render(request, 'home.html', {'library_list' : library_list})


