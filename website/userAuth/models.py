from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
User
Profession		(CharField)
Interests		(CharField)
Image			(ImageField)
"""
class extUser(models.Model):
    User = models.ForeignKey(User, unique=True)
    Profession = models.CharField(max_length=50, blank=True, null=True)
    Intrests = models.CharField(max_length=100, blank=True, null=True)
    Image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.User.username
