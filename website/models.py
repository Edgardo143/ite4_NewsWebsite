from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    category = models.CharField(max_length=100, default='default_category_value')

    def __str__(self):
        return self.title
class NewsCategory(models.Model):
    CATEGORY_CHOICES = [
        ('politics', 'Politics'),
        ('entertainment', 'Entertainment'),
        ('sports', 'Sports'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

