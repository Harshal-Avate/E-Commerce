from django.shortcuts import render, redirect, get_object_or_404
from .models import Product,Order

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

    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    cart_items = []
    total_price = 0

    for product in products:
        quantity = cart[str(product.id)]
        item_total = product.price * quantity
        total_price += item_total

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "item_total": item_total,
        })

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "products/cart.html", context)

def remove_from_cart(request, id):
    cart = request.session.get("cart", {})
    id = str(id)

    if id in cart:
        del cart[id]

    request.session["cart"] = cart
    return redirect("cart")

def increase_quantity(request, id):
    cart = request.session.get("cart", {})
    id = str(id)

    if id in cart:
        cart[id] += 1
    else:
        cart[id] = 1

    request.session["cart"] = cart
    return redirect("cart")


def decrease_quantity(request, id):
    cart = request.session.get("cart", {})
    id = str(id)

    if id in cart:
        cart[id] -= 1

        if cart[id] <= 0:
            del cart[id]

    request.session["cart"] = cart
    return redirect("cart")

def checkout(request):
    cart = request.session.get("cart", {})
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    total_price = 0

    for product in products:
        quantity = cart[str(product.id)]
        total_price += product.price * quantity

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        Order.objects.create(
            name=name,
            phone=phone,
            address=address,
            total_price=total_price
        )

        request.session["cart"] = {}

        return redirect("product_list")

    return render(request, "products/checkout.html", {"total_price": total_price})