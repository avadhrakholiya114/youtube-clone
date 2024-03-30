from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

# for show visiblity vise video
VISIBILITY = (
    ("public", "public"),
    ("unlisted", "unlisted"),
    ("Members only", "Members only"),
    ("private", "private")
)
CATEGORIES = (
    ("game", "Gaming"),
    ("music", "Music"),
    ("beauty", "Beauty"),
    ("education", "Education"),
    ("comedy", "Comedy"),
    ("food", "Food"),
    ("technology", "Technology"),
    ("travel", "Travel"),
    ("sports", "Sports"),
    ("lifestyle", "Lifestyle"),
    ("news", "News"),
    ("entertainment", "Entertainment"),
    ("other", "Other")
)




# This helps in organizing uploaded files and prevents naming conflicts between different users ' files.
def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


class Video(models.Model):
    videos = models.FileField(upload_to=user_directory_path)
    img = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    tags = TaggableManager()
    date = models.DateTimeField(auto_now=True)
    visibility = models.CharField(choices=VISIBILITY, max_length=100, default="public")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    views = models.PositiveIntegerField(default=0)
    catagory = models.CharField(choices=CATEGORIES, max_length=100, default="other")
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    comment=models.CharField(max_length=10000)
    # on_delete = models.SET_NULL, null = True measn when user deleted comment not delete that time
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    active = models.BooleanField(default=True)
    video = models.ForeignKey(Video,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:30]
