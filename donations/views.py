from cart.models import Cart
from django.shortcuts import render
from django.http import Http404

from django.views.generic import ListView, DetailView

from tags.models import Donation_Tag
from .models import Donation


# Create your views here.
# class DonationListView(ListView):
#     template_name = "donations/list.html"
#     queryset = Donation.objects.all()

#     # def get_queryset(self, *args, **kwargs):
#     #     request = self.request
#     #     return Donation.objects.all()

# # class EmergencyListView(ListView):
# #     template_name = "donations/emergency.html"
# #     queryset = Donation.objects.all().filter(emergency = True)

def donation_list_view(request) :
    tags = Donation_Tag.objects.all()
    donations = Donation.objects.all()
    return render(request, 'donations/list.html', {'tags':tags, 'donations' : donations})

class DonationDetailView(DetailView):
    queryset = Donation.objects.all()
    template_name = "donations/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DonationDetailView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context["cart"] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Donation.objects.filter(pk=pk)

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Donation.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("Product doesn't exist")
    #     return instance


def donation_request(request):
    return render(request, 'donations/request.html')
