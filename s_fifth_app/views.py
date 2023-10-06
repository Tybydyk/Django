from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info(f'{request}Index page accessed')
    return HttpResponse("Lesson5 page")
