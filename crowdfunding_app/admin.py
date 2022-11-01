from django.contrib import admin
from .models import Project, Category, Image, Comment

# Register your models here.
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Comment)
