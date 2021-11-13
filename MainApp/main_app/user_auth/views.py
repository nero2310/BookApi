from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.

def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm(request)
        return render(request, "user_auth/login_page.html", context={'form': form})

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "user_auth/login_sucess.html")
        else:
            return render(request, "user_auth/login_page.html", context={'form': form})


def logout_user(request):
    logout(request)
    return render(request, "user_auth/logout_page.html")


def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request, "user_auth/register_sucess.html")
        else:
            return render(request, "user_auth/register_page.html")
    else:
        form = UserCreationForm()
        return render(request, "user_auth/register_page.html", context={'form': form})


def user_profile(request):
    user = get_user(request)
    return render(request, "user_auth/user_profile.html", context = {'user': user})