from django.shortcuts import render, redirect

from .models import Cart
from donations.models import Donation

from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your views here.

def cart_home(requset):
    cart_obj = Cart.objects.new_or_get(requset)
    return render(requset, "cart/home.html", {'cart' : cart_obj})

def cart_update(request):
    donation_id = request.POST.get['donation_id']
    if donation_id is not None:
        try:
            donation_obj = Donation.objects.get(id = donation_id)
        except:
            print("Product does not exist anymore")
            return redirect("cart:home")

    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if donation_obj in cart_obj.donations.all():
        cart_obj.donations.remove(donation_obj)
    else:
        cart_obj.donations.add(donation_obj)
    request.session['cart_items'] = cart_obj.donations.count()
    return redirect["cart:home"] 
