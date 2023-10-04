import logging
import random
from django.template.response import TemplateResponse
from . import models
from django.http import HttpResponse
from . import forms
from django.shortcuts import render
from django.contrib import messages

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


def view_all_articles(request):
    articles = models.Article.objects.all()
    context = {'title': 'Список статей',
               'articles': articles}
    return TemplateResponse(request, 'lesson_2_app/template_articles_list.html', context)


def view_article(request, id_article):
    try:
        article = models.Article.objects.get(pk=id_article)
        context = {'title': article.title,
                   'text': article.content}
        article.show_count += 1
        article.save()
    except:
        context = {'title': f"article {id_article}",
                   'text': 'does not exist'}
    finally:
        return TemplateResponse(request, 'lesson_2_app/template_article.html', context)


def create_author(request):
    if request.method == 'POST':
        form = forms.AuthorForms(request.POST)
        if form.is_valid():
            author = models.Author(f_name=form.cleaned_data['name'],
                                   l_name=form.cleaned_data['surname'],
                                   email=form.cleaned_data['email'],
                                   biography=form.cleaned_data['biography'],
                                   birthday=form.cleaned_data['birthday'])
            author.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully')
    else:
        form = forms.AuthorForms()
    return render(request, 'lesson_2_app/author_form.html', {'form': form})

def create_article(request):
    if request.method == 'POST':
        form = forms.NewArticleForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = forms.NewArticleForm()
    return render(request, 'lesson_2_app/author_form.html', {'form': form})

def create_article_form(request):
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully')
    else:
        form = forms.ArticleForm()
    return render(request, 'lesson_2_app/author_form.html', {'form': form})

