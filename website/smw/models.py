from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
"""
User
Username		(CharField, Unique)
Name			(CharField)
Age			(IntegerField)
Profession		(CharField)
Interests		(CharField)
Image			(ImageField)
E-mail			(EmailField, Unique)
Sign_Date		(DateTimeField)
"""

class Post:
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.ForeignKey(Comment)
    Heading = models.CharField(max_length=200)
    Description = models.TextField(unique=True)
    Tags = models.CharField(max_length=200)
    Views = models.IntegerField(default=0)
    Wants = models.IntegerField(default=0)
    Shlts = models.IntegerField(default=0)
    Post_Date = models.DateTimeField(default=datetime.now)

class Comment:
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Text = models.TextField()
    Post_Date = models.DateTimeField(default=datetime.now)

    class Meta:
        unique_together = ("User", "Text", "Post")

class Category:
    Category = models.CharField(max_length=100, unique=True)
    Description = models.CharField(max_length=500)
    Icon_Image = models.ImageField()
    Background_Image = models.ImageField()
