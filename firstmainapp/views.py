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
        <title>Django hw1_1</title>
    </head>
        <body>
        <h2>Welcome to 'main' homework1 page!</h2>

                <h2>About app:</h2><br>
                <p>This is a very simple MAIN page.</p><br>
    
                <footer>
                    <p>Django. Homework1. MAIN app</p>
                </footer>
        </body>
    </html>
    """
    logger.info(f'{request}HW_1_1 page accessed')
    return HttpResponse(html)