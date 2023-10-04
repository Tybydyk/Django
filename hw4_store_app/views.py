from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
import logging
from .forms import ProductUpd
from .models import User, Product
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info(f'{request}Index page accessed')
    return HttpResponse("HomeWork4_Store")

def users(request):
    logger.info(f'{request}users page accessed')
    users = User.objects.all()
    return HttpResponse(users)

def products(request):
    logger.info(f'{request}users page accessed')
    products = Product.objects.all()
    return HttpResponse(products)


def prod_upd(request):
    logger.info(f'{request} request received')
    if request.method == 'POST':
        form = ProductUpd(request.POST, request.FILES)
        if form.is_valid():
            product_name = form.data['product_name']
            description = form.data['description']
            price = form.data['price']
            quantity = form.data['quantity']
            product_id = form.data['product']
            product = Product.objects.filter(id=product_id).first()

            product.product_name = product_name
            product.description = description
            product.price = price
            product.quantity = quantity
            image = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product.image = image.name
            product.save()
            logger.info(f'{product.product_name} saved')
            return render(request, 'hw4_store_app/prod_upd.html', {'message': "Updated"})
    else:
        form = ProductUpd()
    return render(request, 'hw4_store_app/prod_upd.html', {'form': form})