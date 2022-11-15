from django.http import HttpResponse
import random
from articles.models import (Article,Page)
from django.template.loader import render_to_string
from django.db.models import Avg

def article_home_view(request):
    return HttpResponse


def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    avg_visits = Page.objects.aggregate(avg_visits=Avg('visits_counts'))['avg_visits']
    print(avg_visits)
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
    }
    # Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)