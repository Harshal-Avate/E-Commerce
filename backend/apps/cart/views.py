from decimal import Decimal
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from apps.products.models import Product


def get_cart_data(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total_price = Decimal("0.00")

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            item_total = product.price * quantity

            cart_items.append({
                "product": product,
                "quantity": quantity,
                "item_total": item_total,
            })

            total_price += item_total
        except Product.DoesNotExist:
            continue

    return cart_items, total_price


def cart_view(request):
    cart_items, total_price = get_cart_data(request)
    return render(request, "cart/cart.html", {
        "cart_items": cart_items,
        "total_price": total_price,
    })


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if product.stock < 1:
        messages.error(request, "This product is out of stock.")
        return redirect("product_list")

    cart = request.session.get("cart", {})
    product_id = str(product_id)
    
    # Try to get quantity from POST, default to 1
    try:
        quantity = int(request.POST.get("quantity", 1))
    except ValueError:
        quantity = 1

    if quantity < 1:
        quantity = 1

    if product_id in cart:
        new_quantity = cart[product_id] + quantity
        if new_quantity <= product.stock:
            cart[product_id] = new_quantity
        else:
            cart[product_id] = product.stock
            messages.warning(request, f"You cannot add more than {product.stock} available stock.")
    else:
        if quantity <= product.stock:
            cart[product_id] = quantity
        else:
            cart[product_id] = product.stock
            messages.warning(request, f"Added maximum available stock ({product.stock}).")

    request.session["cart"] = cart
    request.session.modified = True
    messages.success(request, f"{product.name} added to cart.")
    return redirect("cart")


def increase_quantity(request, product_id):
    cart = request.session.get("cart", {})
    product = get_object_or_404(Product, id=product_id)
    product_id = str(product_id)

    if product_id in cart:
        if cart[product_id] < product.stock:
            cart[product_id] += 1
        else:
            messages.warning(request, "No more stock available.")

    request.session["cart"] = cart
    request.session.modified = True
    return redirect("cart")


def decrease_quantity(request, product_id):
    cart = request.session.get("cart", {})
    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] -= 1
        if cart[product_id] <= 0:
            del cart[product_id]

    request.session["cart"] = cart
    request.session.modified = True
    return redirect("cart")


def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session["cart"] = cart
    request.session.modified = True
    return redirect("cart")


def buy_now(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if product.stock < 1:
        messages.error(request, "This product is out of stock.")
        return redirect("product_list")

    cart = request.session.get("cart", {})
    product_id = str(product_id)

    try:
        quantity = int(request.POST.get("quantity", 1))
    except ValueError:
        quantity = 1

    if quantity < 1:
        quantity = 1
    elif quantity > product.stock:
        quantity = product.stock

    # In Amazon's buy now, it doesn't necessarily replace the cart, 
    # but for this simple implementation we just add it and go to checkout.
    if product_id in cart:
        new_quantity = cart[product_id] + quantity
        cart[product_id] = min(new_quantity, product.stock)
    else:
        cart[product_id] = quantity
    
    request.session["cart"] = cart
    request.session.modified = True
    
    return redirect("checkout")