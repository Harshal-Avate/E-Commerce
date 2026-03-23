from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category


def product_list(request):
    query = request.GET.get("q")
    category_slug = request.GET.get("category")
    
    products = Product.objects.all()

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    if category_slug:
        products = products.filter(category__slug=category_slug)

    return render(request, "products/product_list.html", {
        "products": products,
        "query": query,
        "selected_category": category_slug,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, "products/product_detail.html", {
        "product": product
    })


def antigravity_view(request):
    return render(request, "antigravity.html")