from django.urls import path
from . import views as crowdfund_app


urlpatterns = [
    path('', crowdfund_app.index, name='index'),
    path('category-projects/<int:category_id>', crowdfund_app.category_projects, name='category_projects'),
]
