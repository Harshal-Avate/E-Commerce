from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'product': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})

def add_to_cart(request, id):
    cart = request.sesson.get('cart', [])
    cart.append(id)
    request.sesson['cart'] = cart
    return redirect('product_list')

def cart_view(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    return render(request, 'products/cart.html', {'products': products})