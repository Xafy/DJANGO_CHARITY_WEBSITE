from django.urls import path

from .views import ProfileUpdate, ProfileDetail

urlpatterns = [
    path('<slug>/', ProfileDetail.as_view(), name ='profile'),
    path('edit/<slug>/', ProfileUpdate.as_view(), name ='edit'),
]