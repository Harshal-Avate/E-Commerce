from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    cart = request.session.get("cart", [])
    cart_count = len(cart)
    context = {
        "products": products,
        "cart_count": cart_count
    }
    return render(request, "products/product_list.html", context)

def product_detail(request, id):
    products = Product.objects.get.get_object_or_404(Product, id=id)
    context = {
        "product": products
    }
    return render(request, 'products/product_detail.html', {'product': products})

def add_to_cart(request, id):
    cart = request.session.get('cart', [])
    cart.append(id)
    request.session['cart'] = cart
    return redirect('product_list')

def cart_view(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    return render(request, 'products/cart.html', {'products': products})

def cart_view(request):
    cart = request.session.get("cart", []) #This gets the cart from the session.
    products = Product.objects.filter(id__in=cart)
    context = {
        "products": products
    }
    return render(request, "products/cart.html", context)

