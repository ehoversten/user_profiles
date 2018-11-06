from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.post

    def __repr__(self):
        # return "<ID: {} - Post object: {}>".format(self.id, self.post)
        return "<PK: {} - Post object: {}>".format(self.pk, self.post)
