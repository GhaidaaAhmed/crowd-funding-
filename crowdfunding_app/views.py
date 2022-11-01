from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "crowdfunding_app/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


def index(request):
    return HttpResponse("Crowdfunding app homepage")

# Create your views here.
