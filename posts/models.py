from django.db import models
from django.urls import reverse

# from charity_site.organizations.models import Organization
from organizations.models import Organization
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Post(models.Model):
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	publisher_user = models.ForeignKey(User, related_name='user_post',
                                        on_delete=models.CASCADE, null = True,
		                                blank = True)
	publisher_org = models.ForeignKey(Organization, related_name='org_post',
                                        on_delete=models.CASCADE, null = True,
		                                blank = True)
	votes = models.IntegerField(default = 0)
	#voters = models.ForeignKey(Profile, related_name='list_of_voted_users', on_delete=models.CASCADE, null = True,
	#	blank = True)

	def __init__(self, *args, **kwargs):
		self.voters_list = []
		return super().__init__(*args, **kwargs)


	def get_absolute_url(self):
		return reverse('posts:detail', kwargs={'id': self.id})
	def get_votes(self):
		return self.votes
	def up_vote(self):
		self.votes = self.votes + 1
	def add_voter(self, voter) :
		if voter not in self.voters_list:
			self.voters_list.append(voter)
			#self.voters_list = self.voters_list + voter
		else: 
			pass
		return self.voters_list	
	@property	
	def get_voters(self):
		return self.voters_list	

	def down_vote(self):
		self.votes = self.votes -1

	#def down_vote(self):

	#	self.votes = self.votes -1
	#def append_user(self, user):
	#	self.voters = self.voters.append(user)

class Voters(models.Model):
    voter = models.ForeignKey(User, related_name='list_of_voted_users',
                            on_delete=models.CASCADE, null = True,
                            blank = True)
    post = models.ForeignKey(Post, related_name='posts_of_voters',
                                on_delete=models.CASCADE, null = True,
                                blank = True)

class Comment(models.Model):
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	publisher_user = models.ForeignKey(User, related_name='user_comment', 
										on_delete=models.CASCADE, null = True, blank = True)

	publisher_org = models.ForeignKey(Organization, related_name='org_comment', 
										on_delete=models.CASCADE, null=True, blank = True)

	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	votes = models.IntegerField(default = 0)
	
	def get_votes(self):
		return self.votes
	def up_vote(self):
		self.votes = self.votes + 1
	def down_vote(self):
		self.votes = self.votes -1