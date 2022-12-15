from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SigninForm, SignupForm
from posts.models import Comment, Voters, Post
from donations.models import Donation
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
User = get_user_model()


# from . import forms


def home(request) :
    donations=Donation.objects.all().filter(emergency = True)
    return render(request, 'home.html', {'donations':donations,})

def about(request) :
    return render(request, 'about-us.html', {})

def zaky(request) :
    return render(request, 'zaky.html', {})

def how_com(request) :
    return render(request, 'how-com.html', {})

def how_don(request) :
    return render(request, 'how-don.html', {})


def signin_page(request):
    form = SigninForm(request.POST or None)
    context = {
        'form' : form
    }
    # print('user is logged in')
    # print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email , password=password)
        # print(request.user.is_authenticated)
        # print(user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print('error')
    
    return render(request, 'auth/signin.html', context)

def logout_view(request):
    logout(request)
    return redirect("/")

def signup_page(request):
    form = SignupForm(request.POST or None)
    context = {
        "form" : form
    }

    if form.is_valid():
        print(form.cleaned_data)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        full_name = form.cleaned_data.get('full_name')
        user_name = form.cleaned_data.get('user_name')
        # firstname = form.cleaned_data.get('firstname')
        # seconedname = form.cleaned_data.get('seconedname')
        # lastname = form.cleaned_data.get('lastname')
        # birth_date = form.cleaned_data.get('birth_date')
        # phone = form.cleaned_data.get('phone')
        new_user = User.objects.create_user(email,full_name, user_name, password)
        print(new_user)
        return redirect("/")
    return render(request, 'auth/signup.html', context)

def community(request) :
    ids = []
    slug = None
    if request.user.is_authenticated:
        slug = request.user.slug
        voted_users = Voters.objects.filter(voter = request.user)
        for vote in voted_users:
            ids.append(vote.post.id)		
    user_posts = Post.objects.all().exclude(publisher_user__isnull = True)
    org_posts = Post.objects.all().exclude(publisher_org__isnull=True)
    return render(request, 'community/index.html', {'ids' : ids,'slug' : slug, 'user_posts': user_posts, 'org_posts': org_posts})


# def suggestion_view(request):
#     form = forms.SuggestionForm()
#     return render(request, 'suggest.html', {'form' : form})

# class EmergencyListView(ListView):
#     template_name = "home.html"
#     queryset = Donation.objects.all().filter(emergency = True)

# def emergency(request):
#     donations=Donation.objects.all().filter(emergency = True)
#     return render(request, 'home.html', {'donations':donations,})