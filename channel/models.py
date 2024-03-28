from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from core.models import user_directory_path

# Create your models here.

# for show visiblity vise video
STATUS = (
    ("active", "active"),
    ("disable", "disable"),

)


class Channel(models.Model):
    img = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    full_name=models.CharField(max_length=200)
    channel_name=models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    keywords = TaggableManager()
    joined = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, max_length=100, default="active")
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user_user")
    subscriber = models.ManyToManyField(User,related_name="user_sub")
    verified=models.BooleanField(default=False)

    def __str__(self):
        return self.channel_name

