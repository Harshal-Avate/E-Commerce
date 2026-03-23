from .models import Category

def categories_processor(request):
    return {
        'all_categories': Category.objects.all()
    }

def cart_processor(request):
    cart = request.session.get("cart", {})
    cart_count = sum(cart.values())
    return {
        'global_cart_count': cart_count
    }
