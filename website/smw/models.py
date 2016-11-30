from django.db import models
from django.contrib.auth.models import User as authUser
from datetime import datetime
from django.urls import reverse

# Create your models here.

"""
Category of posts
"""
class Category(models.Model):
    Category = models.CharField(max_length=100, unique=True)
    Description = models.CharField(max_length=500)
    Icon_Image = models.ImageField(blank=True, null=True)
    Background_Image = models.ImageField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("smw:cat", kwargs={'pk':self.pk})

    def post_count(self):
         return self.post_set.count()

    def __str__(self):
        return self.Category

"""
Post with an idea
"""
class Post(models.Model):
    User = models.ForeignKey(authUser, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Idea = models.TextField(unique=True)
    Tags = models.CharField(max_length=200, blank=True, null=True)
    Views = models.IntegerField(default=0)
    Wants = models.ManyToManyField(authUser, related_name="Wants")
    Shlts = models.ManyToManyField(authUser, related_name="Shlts")
    Post_Date = models.DateTimeField(default=datetime.now)

    def get_absolute_url(self):
        return reverse("smw:Idea", kwargs={'pk':self.pk})

    def comment_count(self):
         return self.comment_set.count()

    def Want_count(self):
        return self.Wants.all().count()

    def Shlt_count(self):
        return self.Shlts.all().count()

    def __str__(self):
        return self.Title

"""
Comment on Post
"""
class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    User = models.ForeignKey(authUser, on_delete=models.CASCADE)
    Text = models.TextField()
    Post_Date = models.DateTimeField(default=datetime.now)

    class Meta:
        unique_together = ("User", "Text", "Post")

    def __str__(self):
        return self.Post.Title+" : "+self.Text
