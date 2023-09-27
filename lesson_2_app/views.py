import logging
import random
from . import models
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info(f'{request}Index page accessed')
    return HttpResponse("Lesson 2")

def heads_tails(request):
    logger.info(f'{request}heads_tails page accessed')
    n = request.GET.get('n', '5')
    res = random.choice(['Heads', 'Tails'])
    res_w = models.HeadsTails(res=res)
    res_w.save()
    data = models.HeadsTails.statistic(n)
    return HttpResponse(data.items())

def author_read(request):
    logger.info(f'{request}author page accessed')
    authors = models.Author.objects.all()
    return HttpResponse(authors)

def articles(request):
    logger.info(f'{request}articles page accessed')
    articles = models.Article.objects.all()
    return HttpResponse(articles)

def article_by_author(request):
    logger.info(f'{request}articles by author')
    name = request.GET.get('name')
    author_id = models.Author.objects.filter(f_name=name).first()
    articles = models.Article.objects.filter(author=author_id).all()
    return HttpResponse(articles)