from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    query = request.GET.get("q")
    if query:
        products = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query)
    else:
        products = Product.objects.all()

    cart = request.session.get("cart", {})
    cart_count = sum(cart.values())

    return render(request, "products/product_list.html", {
        "products": products,
        "cart_count": cart_count,
        "query": query,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, "products/product_detail.html", {
        "product": product
    })


def antigravity_view(request):
    return render(request, "antigravity.html")