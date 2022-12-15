from django.db import models
from datetime import datetime
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.urls import reverse

from django.contrib.auth.models import (
                                        AbstractBaseUser,
                                        BaseUserManager,
                                        )

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, user_name =None, password=None,
                        slug=None, bio=None, avatar_thumbnail =None, 
                        contact_information=None,location=None,
                        **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_admin', False)
        other_fields.setdefault('is_active', True)
        if not email:
            raise ValueError('users must have an email')
        if not password:
            raise ValueError('users must have a password')

        user_obj = self.model(
            email = self.normalize_email(email),
            full_name = full_name,
            user_name = user_name,
            slug = slug,
            bio = bio,
            avatar_thumbnail = avatar_thumbnail,
            contact_information = contact_information,
            location = location,
            **other_fields
        )
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, full_name=None, user_name =None, password=None,
                        slug= None, bio=None, avatar_thumbnail =None,
                        contact_information=None,location=None,
                        **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_admin', False)
        other_fields.setdefault('is_active', True)
        user = self.create_user(
            email,
            full_name = full_name,
            user_name = user_name,
            bio = bio,
            slug = slug,
            avatar_thumbnail = avatar_thumbnail,
            contact_information = contact_information,
            location = location,
            password = password,
            **other_fields
        )
        return user

    def create_superuser(self, email, full_name=None, user_name =None, password=None,
                        slug=None, bio=None, avatar_thumbnail =None,
                        contact_information=None, location=None,
                        **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_active', True)
        user = self.create_user(
            email,
            full_name = full_name,
            user_name = user_name,
            bio = bio,
            slug = slug,
            avatar_thumbnail = avatar_thumbnail,
            contact_information = contact_information,
            location = location,
            password = password,
            **other_fields
        )
        return user

        

class User(AbstractBaseUser):
    email                   = models.EmailField(unique=True, max_length=254)
    user_name               = models.CharField(unique=True, max_length=120)
    slug                    = models.SlugField(unique=True, blank=True)
    full_name               = models.CharField(max_length=254)
    bio                     = models.TextField(max_length=511, blank=True, null=True)
    avatar_thumbnail        = ProcessedImageField(upload_to='img/',
							    				default='/img/default.png',
                                                processors=[ResizeToFill(300, 300)],
                                                format='JPEG',
                                               options={'quality': 60})
    contact_information     = models.TextField(blank=True, null=True)
    location                = models.TextField(blank=True, null=True)                                        
    phone                   = models.CharField(max_length=245, blank=True, null=True)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_admin                = models.BooleanField(default=False)
    timestamp               = models.DateTimeField(default=datetime.now, blank=True)
    # confirmed             = models.BooleanField(default=False)
    # confirmed_date        = models.DateTimeField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name', 'user_name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def save(self, *args, **kwargs):
	    self.slug = self.user_name
	    super(User, self).save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return reverse('accounts:edit', kwargs={'slug': self.slug})
