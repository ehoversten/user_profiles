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
    image       = models.ImageField(upload_to='profile_image', blank=True)

    # objects = models.Manager()
    # objects = UserProfileManager()

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return "<ID: {} - User: {}>".format(self.id, self.user)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
