from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=None)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    post = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)
