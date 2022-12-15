from django.urls import path

from .views import donation_list_view, DonationDetailView, donation_request

urlpatterns = [
    path('list/', donation_list_view, name ='list'),
    path('detail/<pk>/', DonationDetailView.as_view(), name ='detail'),
    path('request/', donation_request, name ='request'),

]