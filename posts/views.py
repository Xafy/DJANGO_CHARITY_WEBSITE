from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import exceptions
from django.urls import reverse
from django.db.models import Q
from .models import Post, Comment, Voters
from organizations.models import Organization
# Create your views here.

def OrderingByTime(request):
	slug = None
	ids = []
	if request.user.is_authenticated:
		slug = request.user.slug
		voted_users = Voters.objects.filter(voter = request.user)
		for vote in voted_users:
			ids.append(vote.post.id)
	user_posts = Post.objects.all().exclude(publisher_user__isnull = True).order_by("-created_at")
	org_posts = Post.objects.all().exclude(publisher_org__isnull=True).order_by("-created_at")
	return render(request, 'community/index.html', {'ids' : ids,'slug' : slug, 'user_posts': user_posts, 'org_posts': org_posts})

def OrderingByVotes(request):
	slug =None
	ids=[]
	if request.user.is_authenticated:
		slug = request.user.slug
		voted_users = Voters.objects.filter(voter = request.user)
		for vote in voted_users:
			ids.append(vote.post.id)
	user_posts = Post.objects.all().exclude(publisher_user__isnull = True).order_by('-votes')
	org_posts = Post.objects.all().exclude(publisher_org__isnull=True).order_by('-votes')
	return render(request, 'community/index.html', {'ids' : ids,'slug' : slug, 'user_posts': user_posts, 'org_posts': org_posts})


def PublishPostView(request, slug):
	content = request.POST.get("text")
	path = request.get_full_path()
	if 'publish/user/' in path :
		Post.objects.create(content=content, publisher_user=request.user)
		return HttpResponseRedirect(reverse('accounts:profile', args=(slug,)))
	else :
		publisher_org = Organization.objects.get(slug = slug)
		Post.objects.create(content=content, publisher_org=publisher_org)
		return HttpResponseRedirect(reverse('org:detail', args=(slug,)))

def PostView(request, id):
	post = Post.objects.get(id=id)
	if post.publisher_user :
		user = post.publisher_user
		org = None
	elif post.publisher_org :
		org = post.publisher_org
		user = None
	comments = Comment.objects.filter(post=post)
	votes = post.get_votes()
	ids = []

	if request.user.is_authenticated:
		voted_users = Voters.objects.filter(voter = request.user)
		for vote in voted_users:
			ids.append(vote.post.id)
	return render(request, 'posts/detail.html', {'post': post, 'comments': comments, 'votes': votes, 'ids': ids, 'user': user, 'org':org})

def CommentsCreation(request, id):
	post = Post.objects.get(id = id)
	Comment.objects.create(content = request.POST.get('comment'), publisher_user=request.user, post = post)
	return HttpResponseRedirect(reverse('posts:detail', args=(post.id,)))



def PostUpView(request, id):
	post = Post.objects.get(id = id)
	users = Voters.objects.filter(post = post)
	if not users:
		Voters.objects.create(post = post, voter = request.user)

	empty_list = []

	for user in users:
		empty_list.append(user.voter.slug)
	if request.user.slug not in empty_list:

		post.up_vote()
		Voters.objects.create(post = post, voter = request.user)
		post.save()
	else:
		pass
	previous_url = request.META.get('HTTP_REFERER')

	return HttpResponseRedirect(previous_url)



def PostUnvoteView(request, id):

	previous_url = request.META.get('HTTP_REFERER')

	post = Post.objects.get(id = id)

	Voters.objects.filter(Q(post_id= id) & Q(voter=request.user)).delete()
	post.down_vote()
	post.save()

	return HttpResponseRedirect(previous_url)