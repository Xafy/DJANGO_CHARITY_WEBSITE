from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core import exceptions
from django.views.generic.detail import DetailView
from posts.models import Voters
from .forms import ProfileChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class ProfileUpdate(UpdateView):
	model = User
	template_name = "edit_profile.html"
	form_class = ProfileChangeForm
	login_url = 'signin'

	def get_object(self):
		obj = User.objects.get(slug = self.kwargs.get('slug'))
		if obj != self.request.user:
			raise exceptions.PermissionDenied()
		return obj

	def get_context_data(self, **kwargs):
		context = super(ProfileUpdate, self).get_context_data(**kwargs)
		return context 
	
	def get_queryset(self):
		base_qs = super(ProfileUpdate, self).get_queryset()
		return base_qs.filter(user_name=self.request.user.user_name)

class ProfileDetail(DetailView):
	model = User
	template_name="user_profile.html"
	def get_object(self):
		return User.objects.get(slug = self.kwargs.get('slug'))

	def get_context_data(self, **kwargs):
		context = super(ProfileDetail, self).get_context_data(**kwargs)
		request = self.request
		slug =None
		ids=[]
		if request.user.is_authenticated:
			slug = request.user.slug
			voted_users = Voters.objects.filter(voter = request.user)
			for vote in voted_users:
				ids.append(vote.post.id)
		context['ids'] = ids
		return context 