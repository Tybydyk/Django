from django.shortcuts import render
from django.http import HttpResponse
import logging
import random

logger = logging.getLogger(__name__)

def index(request):
    logger.info(f'{request}Index page accessed')
    return HttpResponse("Hi, world!")

def heads_tails(request):
    logger.info(f'{request}heads_tails page accessed')
    return HttpResponse(str(random.choice(['Heads', 'Tales'])))

def rand_int(request):
    logger.info(f'{request}rand_int page accessed')
    return HttpResponse(str(random.randint(1, 100)))

def cube(request):
    logger.info(f'{request} cube page accessed {str(random.randint(1, 6))}')
    return HttpResponse(str(random.randint(1, 6)))

def about(request):
    try:
        # some code that might raise an exception
        result = 1 / 1
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse(f'{request}This is the about page.')
