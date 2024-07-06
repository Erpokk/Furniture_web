from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render


from goods.models import Products
from goods.utils import q_search


# Create your views here.
def catalog(request, category_slug=None):

    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    # Filte dropdown menu
    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    # Save in another element, not int context
    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)
    # PAge paginator, how many goods will be displayed on page
    paginator = Paginator(goods, 3)

    cur_page = paginator.page(page)

    context = {"title": "Home - Catalog", "goods": cur_page, "slug_url": category_slug}
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {"product": product}

    return render(request, "goods/product.html", context=context)
