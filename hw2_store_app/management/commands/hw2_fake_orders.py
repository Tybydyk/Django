from random import randint

from django.core.management.base import BaseCommand
from hw2_store_app.models import User, Product, Order


class Command(BaseCommand):
    help = "Generate fake order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Numbers of creating orders')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            total_price = 0
            u_pk = randint(1, 9)
            customer = User.objects.filter(pk=u_pk).first()
            if customer is not None:
                order = Order(customer=customer, total_price=total_price)
                order.save()
                for _ in range(0, 9):
                    p_pk = randint(1, 9)
                    product = Product.objects.filter(pk=p_pk).first()
                    if product is not None:
                        self.stdout.write(f'{product}')
                        self.stdout.write(f'{product.price}')
                        total_price += product.price
                        self.stdout.write(f'{total_price}')
                        order.products.add(product)
                        order.total_price = total_price
                order.save()
            self.stdout.write(f'{order}')