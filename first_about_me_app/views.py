from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    html = """           
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Django hw1_2</title>
    </head>
        <body>
        <h2>Welcome to 'about me' homework1 page!</h2>

                <h2>About app:</h2><br>
                <p>I am Dmitry Lobanovsky - GB student</p>
                <p>This is Django homework app2</p>
                <br>

                <footer>
                    <p>Django. Homework1. About me app</p>
                </footer>
        </body>
    </html>
    """
    logger.info(f'{request}HW_1_2 page accessed')
    return HttpResponse(html)