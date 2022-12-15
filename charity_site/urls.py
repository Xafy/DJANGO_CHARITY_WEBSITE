"""charity_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from . import views

urlpatterns = [
    
    path('', views.home, name ='home'),
    path('signin/', views.signin_page, name ='signin'),
    path('logout/', views.logout_view, name ='logout'),
    path('signup/', views.signup_page, name ='signup'),
    path('community/', views.community, name ='community'),
    path('about-us/', views.about, name ='about-us'),
    path('zaky/', views.zaky, name ='zaky'),
    path('how-community/', views.how_com, name ='how-com'),
    path('how-donate/', views.how_don, name ='how-don'),
    path('donation/', include(('donations.urls', 'donations'), namespace='donation')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('org/', include(('organizations.urls', 'organizations'), namespace='org')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('post/', include(('posts.urls', 'posts'), namespace='posts')),
    path('admin/', admin.site.urls),    
    # path('courses/', include(('courses.urls','courses'), namespace='courses')),
    # path('suggest/', views.suggestion_view, name ='suggest'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
