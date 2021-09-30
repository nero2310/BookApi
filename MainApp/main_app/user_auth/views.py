from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            render(request, "user_auth/login_sucess.html")
        else:
            raise NotImplementedError
    else:
        form = AuthenticationForm(request)
        render(request, "user_auth/login_page.html", context={'form': form})
