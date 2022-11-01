from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=200)


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    details = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 related_name='projects')
    total_target = models.FloatField()
    rate = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    tags = TaggableManager()
    featured = models.BooleanField(default=False)
    inappropriate_vote = models.IntegerField(default=0)
    active = models.BooleanField(default=True)


class Image(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    inappropriate_vote = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
