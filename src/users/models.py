# coding: utf-8

import hashlib
from datetime import datetime
from urllib import parse

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        user = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username')
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **kwargs):
        super_user = self.create_user(email, password, **kwargs)

        super_user.is_admin = True
        super_user.is_active = True
        super_user.is_staff = True
        super_user.save(using=self._db)

        return super_user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=60)

    name = models.CharField(verbose_name='Full name', max_length=120,
                            blank=True)

    avatar_original = models.CharField(max_length=260, blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    def get_short_name(self):
        if self.name:
            names = self.name.split()
            first_name = names[0]

            return first_name
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(perm_list, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"slug": self.slug})

    def get_thumbnail_url(self):
        return self.get_gravatar_thumbnail_url()

    def get_picture_upload_url(self):
        return '%savatar/upload/' % self.get_absolute_url()

    def get_avatar_file_name(self):
        return 'avatar-%s' % self.username

    def get_gravatar_thumbnail_url(self, size=100):
        # Set your variables here
        email = self.email
        default = 'identicon'
        # construct the url
        gravatar_url = "https://secure.gravatar.com/avatar/" + hashlib.md5(
            email.lower().encode('utf-8')).hexdigest() + "?"
        gravatar_url += parse.urlencode({'d': default, 's': str(size)})

        return gravatar_url
