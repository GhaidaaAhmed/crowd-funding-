from django.contrib import admin
from django.urls import path
from . import views as crowdfund_app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', crowdfund_app.index, name='index')
]
