from django.shortcuts import render
from django.template import context

from goods.models import Products


# Create your views here.
def catalog(request):
    # Save in another element, not int context
    goods = Products.objects.all()

    context = {
        "title": "Home - Catalog",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
