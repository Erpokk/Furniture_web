from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


# Create your views here.
def index(request):
    context = {"title": "Home - main", "content": "Furniture shop"}
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - About us",
        "content": "We are very good",
        "text_on_page": "Very good goods",
    }
    return render(request, "main/about.html", context)
