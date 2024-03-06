from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
VISIBILITY=(
    ("public","public"),
    ("unlisted","unlisted"),
    ("Members only","Members only"),
    ("private","private")
)
def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


class Video(models.Model):
    videos = models.FileField(upload_to=user_directory_path)
    img=models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    title=models.CharField(max_length=100)
    desc=models.TextField(null=True,blank=True)
    tags = TaggableManager()
    date=models.DateTimeField(auto_now=True)
    visibility=models.CharField(choices=VISIBILITY,max_length=100,default="public")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    views=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
class Channel():
    pass


class Profile():
    pass
