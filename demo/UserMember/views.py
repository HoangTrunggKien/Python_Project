from dbm.ndbm import library
from django.shortcuts import render
from .forms import registerForm, loginForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
class registerUser(View):
    def get(self, request):
        rF = registerForm
        return render(request, 'UserMember/register.html', {'rF' : rF})
    def post(self, request):
        lF = loginForm
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'UserMember/login.html', {'lF' : lF})

class loginUser(View):
    def get(self, request):
        lF = loginForm
        return render(request, 'UserMember/login.html', {'lF' : lF})
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'Templates/home.html')
        else:
            return HttpResponse('Login Fail')
  

def logoutUser(request):
    logout(request)
    return HttpResponse('Đã đăng xuất')

