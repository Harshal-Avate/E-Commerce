from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    cart = request.session.get("cart", [])
    cart_count = sum(cart.values())
    context = {
        "products": products,
        "cart_count": cart_count
    }
    return render(request, "products/product_list.html", context)

def product_detail(request, id):
    products = get_object_or_404(Product, id=id)
    context = {
        "product": products
    }
    return render(request, 'products/product_detail.html', {'product': products})

def add_to_cart(request, id):
    cart = request.session.get("cart", {})

    if isinstance(cart, list):
        new_cart = {}
        for item in cart:
            new_cart[str(item)] = 1
        cart = new_cart

    id = str(id)

    if id in cart:
        cart[id] += 1
    else:
        cart[id] = 1

    request.session["cart"] = cart
    return redirect("cart")

def cart_view(request):
    cart = request.session.get("cart", {})

    products = Product.objects.filter(id__in=cart.keys())

    total_price = 0

    for product in products:
        total_price += product.price * cart[str(product.id)]

    context = {
        "products": products,
        "cart": cart,
        "total_price": total_price
    }

    return render(request, "products/cart.html", context)

def remove_from_cart(request, id):
    cart = request.session.get("cart", {})
    id = str(id)

    if id in cart:
        del cart[id]

    request.session["cart"] = cart
    return redirect("cart")