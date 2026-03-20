from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order, OrderItem
from apps.cart.views import get_cart_data


@login_required
def checkout(request):
    cart_items, total_price = get_cart_data(request)

    if not cart_items:
        messages.warning(request, "Your cart is empty.")
        return redirect("product_list")

    if request.method == "POST":
        form = OrderForm(request.POST)

        address_line = request.POST.get("address", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        pincode = request.POST.get("pincode", "")
        full_address = f"{address_line}, {city}, {state} - {pincode}"

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.address = full_address
            order.total_price = total_price
            order.save()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    quantity=item["quantity"],
                    price=item["product"].price,
                )

                product = item["product"]
                product.stock -= item["quantity"]
                product.save()

            request.session["cart"] = {}
            request.session.modified = True

            messages.success(request, "Order placed successfully.")
            return redirect("order_success", order_id=order.id)
        else:
            messages.error(request, "Failed to place order. Please check the checkout details.")
    else:
        form = OrderForm()

    return render(request, "orders/checkout.html", {
        "form": form,
        "cart_items": cart_items,
        "total_price": total_price,
    })


@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/order_success.html", {"order": order})


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "orders/order_list.html", {"orders": orders})