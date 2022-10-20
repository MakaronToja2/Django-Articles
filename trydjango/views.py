from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string

def home_view(request):
    number = random.randint(1,3)
    article_obj = Article.objects.get(id=number)
    article_qs = Article.objects.all()
    context = {
        "object_list": article_qs,
        'object': article_obj,
        "title" : article_obj.title,
        "id" : article_obj.id,
        'content': article_obj.content
    }
    HTML_STRING = render_to_string('home-view.html', context = context)
    #HTML_STRING = """
    #<h1>{title}(id: {id})</h1>
    #<p>{content}</p>
    #""".format(**context)
    return HttpResponse(HTML_STRING)
