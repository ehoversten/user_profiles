from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save

# Create your models here.
class UserProfile(models.Model):
    user        = models.OneToOneField(User)
    description = models.CharField(max_length=255, default='')
    city        = models.CharField(max_length=100, default='')
    website     = models.URLField(default='')
    phone       = models.IntegerField(default=0)

    # objects = models.Manager()
    # objects = UserProfileManager()

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

    return user_profile

post_save.connect(create_profile, sender=User)


# objects = models.Manager()﻿
