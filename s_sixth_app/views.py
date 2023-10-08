from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
import logging

from django.views.generic import TemplateView
from django.shortcuts import render
from django.db.models import Sum
from s_fifth_app.models import Product


def index(request):
    return HttpResponse("Hi, third world!")


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 's_sixth_app/total_count.html', context)

def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 's_sixth_app/total_count.html', context)

def total_in_template(request):
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 's_sixth_app/total_count.html', context)