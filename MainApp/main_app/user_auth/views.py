from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login_view(request):
    render(request, "user_auth/login_sucess.html")
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        print("Działa")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "user_auth/login_sucess.html")
        else:
            raise NotImplementedError
    else:
        form = AuthenticationForm(request)
        return render(request, "user_auth/login_page.html", context={'form': form})

def logout_user(request):
    logout(request)
    return render(request,"user_auth/logout_page.html")