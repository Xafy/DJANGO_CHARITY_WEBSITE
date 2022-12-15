import os
import random

from django.db.models.deletion import CASCADE
from tags.models import Donation_Tag
from organizations.models import Organization
from django.db import models
from django.conf import settings
from django.urls import reverse


# methods
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
    
def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 39999954635)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f"donations/{new_filename}/{final_filename}"

#class mangers
class DonationManager(models.Manager):
    # def get_queryset(self):
    #     return ProductQuerySet(self.model, using=self._db)

    # def all(self):
    #     return self.get_queryset().active()

    # def featured(self):
    #     return self.get_queryset().filter(featured=True)

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

# Create your models here.
class Donation(models.Model):
    title            = models.CharField(max_length=120)
    description      = models.TextField()
    goal             = models.FloatField(default= 00.00)
    reached          = models.FloatField(default=0)
    tag              = models.ForeignKey(Donation_Tag, on_delete=models.CASCADE)   
    org              = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)   
    image            = models.ImageField(upload_to=upload_image_path, null = True, blank=True)
    send_content     = models.CharField(max_length=20, default="0000")
    send_number      = models.CharField(max_length=20, default="0000")
    active           = models.BooleanField(default=True)
    timestamp        = models.DateTimeField(auto_now_add=True)
    emergency        = models.BooleanField(default=False)

    objects = DonationManager()

    def __str__(self):
	    return self.title