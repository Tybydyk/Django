from django.shortcuts import render
import logging
import random
from datetime import datetime, timedelta

from django.template.response import TemplateResponse

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

# Доработаем задачу 8 из прошлого семинара про клиентов, товары и заказы.
# 📌 Создайте шаблон для вывода всех заказов клиента и списком товаров внутри каждого заказа.
# 📌 Подготовьте необходимый маршрут и представление.
# Продолжаем работать с товарами и заказами.
# 📌 Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
# ○ за последние 7 дней (неделю)
# ○ за последние 30 дней (месяц)
# ○ за последние 365 дней (год)
# 📌 *Товары в списке не должны повторяться.

def user_orders(request, user_id):
    user = models.User.objects.filter(pk=user_id).first()
    if user is not None:
        orders = models.Order.objects.filter(customer=user).all()

        if orders is not None:
            for order in orders:
                order_products = order.products.all()
                orders_dict = {order: order_products}
            context = {"user": user, "orders_dict": orders_dict}
            return render(request, 'hw2_store_app/user_orders.html', context)

def user_products_per_time(request, user_id, interval):
    user = models.User.objects.filter(pk=user_id).first()
    message = f'User {user.name} products per time={interval.upper()}'
    if user is not None:
        if interval.lower() == 'week':
            time_interval = 7
        elif interval.lower() == 'month':
            time_interval = 30
        elif interval.lower() == 'year':
            time_interval = 365
        else:
            message = 'the time interval can be WEEK, MONTH or YEAR only'
            time_interval = 1
        check_date = datetime.now() - timedelta(time_interval)
        orders = models.Order.objects.filter(customer=user, date_ordered__gte=check_date).all().order_by('date_ordered')
        products = []
        for order in orders:
            products.append(order.products.all())
        product_set = set(products)
        context = {"message": message, "products": product_set}
        return render(request, 'hw2_store_app/user_products_per_time.html', context)