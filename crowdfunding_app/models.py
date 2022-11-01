from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    appropriate = models.CharField(max_length=7, choices=[
        ('under_8', 'under 8'),
        ('8', '8'),
        ('15', '15'),
        ('adults', 'adults'),
    ])
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
