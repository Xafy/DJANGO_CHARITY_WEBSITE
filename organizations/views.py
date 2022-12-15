from django.shortcuts import render
from django.http import Http404
from django.core import exceptions
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from accounts.views import ProfileDetail
from posts.models import Voters
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import OrganizationChangeForm, OrganizationCreateForm

from .models import Organization


# Create your views here.
class OrganizationListView(ListView):
    template_name = "organizations/list.html"
    queryset = Organization.objects.all()


class OrganizationDetailView(DetailView):
    model = Organization
    queryset = Organization.objects.all()
    template_name = "organizations/detail.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        return Organization.objects.filter(slug=slug)

    def get_context_data(self, **kwargs):
        context = super(OrganizationDetailView, self).get_context_data(**kwargs)
        request = self.request
        slug =None
        ids=[]
        if request.user.is_authenticated:
            slug = request.user.slug
            voted_users = Voters.objects.filter(voter = request.user)
            for vote in voted_users:
                ids.append(vote.post.id)
        context['ids'] = ids
        # moderators = []
        # org_obj = Organization.objects.all().filter(slug=slug)
        # moderators = org_obj['moderators']
        # if request.user in moderators:
        #     moderator = request.user
        # else:
        #     moderator = None
        # context['moderator'] = moderator

        return context 

    
class OrganizationUpdateView(UpdateView):
    model = Organization
    template_name = "organizations/edit.html"
    form_class = OrganizationChangeForm

    def get_object(self):
        obj = Organization.objects.get(slug = self.kwargs.get('slug'))
        if self.request.user not in obj.moderators.all() :
            raise exceptions.PermissionDenied()
        return obj        

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        return super().form_valid(form)


class OrganizationCreateView(CreateView):
    model = Organization
    template_name = "organizations/create.html"
    form_class = OrganizationCreateForm


    def form_valid(self, form):
        form.instance.save()
        my_p = User.objects.get(user_name=self.request.user.user_name)
        form.instance.moderators.add(my_p)
        return super().form_valid(form) 


def UserOrgsView(request, slug):
	orgs = User.objects.get(slug=slug).organization_set
	print('heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeey')
	print(User.objects.get(slug=slug).organization_set)
	return render(request, 'organizations/user_orgs.html', { 'orgs' : orgs})