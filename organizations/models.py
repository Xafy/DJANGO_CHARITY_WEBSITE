from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.views.generic import UpdateView
from django.core import exceptions

from django.urls import reverse
from django.template.defaultfilters import slugify

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Organization(models.Model):
	moderators = models.ManyToManyField(User)
	name = models.CharField(max_length=254, unique=True)
	slug = models.SlugField(max_length=254, unique=True, blank=True)
	bio = models.TextField()
	avatar_thumbnail = ProcessedImageField(upload_to='img/',
											default='img/default2.png',
											format='JPEG',
											options={'quality': 60})
	logo = ProcessedImageField(upload_to='img/',
								default='img/default2.png',
								format='JPEG',
								options={'quality': 60})
	location = models.TextField()
	# tags = models.ManyToManyField(Tag)
	contact_information = models.TextField()
	verified = models.BooleanField(default=False)
	
	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			if slugify(self.name):
				self.slug = slugify(self.name)
			else:
				self.slug = self.name.replace( " ", "-")
		super(Organization, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('org:detail', kwargs={'slug': self.slug}) 

