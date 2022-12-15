from django.db import models

# Create your models here.
class Donation_Tag(models.Model):
    name = models.CharField(max_length=40)
    english_name = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
	    return self.name
