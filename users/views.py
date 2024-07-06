from django.shortcuts import render
from django.template import context


# Create your views here.
def login(request):
    context = {"title": "User login"}
    return render(request, "users/login.html", context)


def registration(request):
    context = {"title": "User registration"}
    return render(request, "users/registration.html", context)


def profile(request):
    context = {"title": "User profile"}
    return render(request, "users/profile.html", context)


def logout(request):
    context = {"title": "User registration"}
    return render(request, "", context)
