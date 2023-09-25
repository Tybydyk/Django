from django.http import HttpResponse
import logging


def index(request):
    return HttpResponse("Hi, second world!")
