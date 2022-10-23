from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string


def article_home_view(request):
    return HttpResponse


def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    print(id)
    random_id = random.randint(1, 3)  # pseudo random
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    # Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)