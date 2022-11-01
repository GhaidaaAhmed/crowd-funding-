from django.contrib import admin
from .models import Project, Category, Image

# Register your models here.
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Image)
