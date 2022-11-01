from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Project, Category, Image


class HomePageView(TemplateView):

    template_name = "crowdfunding_app/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['highest_projects'] = Project.objects.order_by('-rate')[:5]
        context['latest_projects'] = Project.objects.orderby('-create_date')[:5]
        context['featured_projects'] = Project.objects.filter(featured=1)[:5]
        context['categories'] = Category.objects.all()
        return context


def index(request):
    return HttpResponse("Crowdfunding app homepage")

# Create your views here.
