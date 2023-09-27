from django.shortcuts import render
import logging
import random
from . import models
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info(f'{request}Index page accessed')
    return HttpResponse("HomeWork2_Store")

def users(request):
    logger.info(f'{request}users page accessed')
    users = models.User.objects.all()
    return HttpResponse(users)

def products(request):
    logger.info(f'{request}users page accessed')
    products = models.Product.objects.all()
    return HttpResponse(products)

def orders(request):
    logger.info(f'{request}users page accessed')
    orders = models.Order.objects.all()
    return HttpResponse(orders)