from django.db.models.deletion import CASCADE
from django.db import models
from django.db.models.signals import m2m_changed, pre_save, post_save

from donations.models import Donation
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.

#cart manager
class CartManager(models.Manager):

    # to create a new cart or get data if the cart already exist
    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            print('cart exists')
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            new_obj = True
            cart_obj = Cart.objects.new(user=None)
            request.session['cart_id'] = cart_obj.id

        return cart_obj, new_obj

    # to create a cart for the user
    def new(self, user = None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        
        return self.model.objects.create(user = user_obj)

    


class Cart(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    donations = models.ManyToManyField(Donation, blank=True)
    time_added = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=00.00, max_length=20)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

def m2m_changed_cart_reciever(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == "post_clear":
        print(action)
        donations = instance.donations.all()
        total = 0 
        for x in donations:
            total += x.goal
            instance.total = total
            instance.save()
            print(total)

m2m_changed.connect(m2m_changed_cart_reciever, sender = Cart)

# def pre_save_cart_reciever(sender, instance, *args, **kwargs):
#     instance.total = instance.sub_total * 1.25

# pre_save.connect(pre_save_cart_reciever, sender = Cart)