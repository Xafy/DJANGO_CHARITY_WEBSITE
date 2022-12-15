from django.urls import path

from .views import (
                    OrganizationListView, OrganizationDetailView,
                    OrganizationUpdateView, OrganizationCreateView
                    ,UserOrgsView
                    )
urlpatterns = [
    path('list/', OrganizationListView.as_view(), name ='list'),
    path('detail/<slug>/', OrganizationDetailView.as_view(), name ='detail'),
    path('edit/<slug>/', OrganizationUpdateView.as_view(), name ='edit'),
    path('create/', OrganizationCreateView.as_view(), name ='create'),
    path('user-orgs/<slug>', UserOrgsView, name ='user-orgs'),

]