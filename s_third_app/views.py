from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
import logging

from django.views.generic import TemplateView
from . import models


def index(request):
    return HttpResponse("Hi, third world!")

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


def my_view(request):
    context = {"name": "John"}
    return render(request, "s_third_app/template1.html", context)

class TemplIf(TemplateView):
    template_name = "s_third_app/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context

def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}

    return render(request, 's_third_app/templ_for.html', context)

def author_posts(request, author_id):
    author = get_object_or_404(models.Author, pk=author_id)
    posts = models.Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 's_third_app/author_posts.html', {'author': author, 'posts': posts})

def post_full(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    return render(request, 's_third_app/post_full.html', {'post': post})