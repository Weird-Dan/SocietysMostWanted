from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
"""
User
Profession		(CharField)
Interests		(CharField)
Image			(ImageField)
"""
class extUser(models.Model):
    User = models.ForeignKey(User, unique=True)
    Profession = models.CharField(max_length=50, null=True)
    Intrests = models.CharField(max_length=100, null=True)
    Image = models.ImageField(null=True)

"""
Category of posts

"""
class Category(models.Model):
    Category = models.CharField(max_length=100, unique=True)
    Description = models.CharField(max_length=500)
    Icon_Image = models.ImageField()
    Background_Image = models.ImageField()

    def post_count(self):
         return self.post_set.count()

    def __str__(self):
        return self.Category

"""
Post with an idea

"""
class Post(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Idea = models.TextField(unique=True)
    Tags = models.CharField(max_length=200)
    Views = models.IntegerField(default=0)
    Wants = models.IntegerField(default=0)
    Shlts = models.IntegerField(default=0)
    Post_Date = models.DateTimeField(default=datetime.now)

    def get_absolute_url(self):
        return reverse("smw:Idea", kwargs={'pk':self.pk})

    def comment_count(self):
         return self.comment_set.count()

    def __str__(self):
        return self.Title

"""
Comment on Post

"""
class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Text = models.TextField()
    Post_Date = models.DateTimeField(default=datetime.now)

    class Meta:
        unique_together = ("User", "Text", "Post")

    def __str__(self):
        return self.Post.Title+" : "+self.Text
