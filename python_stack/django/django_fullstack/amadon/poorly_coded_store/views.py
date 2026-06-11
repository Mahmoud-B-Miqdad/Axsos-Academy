from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def buy_product(request):
    """Skinny View handling the secure POST processing and redirecting safely."""
    if request.method == "POST":
        # Delegate all security calculations to the Fat Model Manager
        Order.objects.process_purchase(request.POST, request.session)
        return redirect('/checkout/')
    return redirect('/')

def checkout(request):
    """Renders the final thank you page without risk of processing orders twice."""
    context = {
        "last_charge": request.session.get('last_charge', 0.0),
        "total_items": request.session.get('total_items', 0),
        "total_spent": request.session.get('total_spent', 0.0)
    }
    return render(request, "store/checkout.html", context)