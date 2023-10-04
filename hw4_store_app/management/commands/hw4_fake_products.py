from django.core.management.base import BaseCommand
from hw4_store_app.models import Product
from random import randint


class Command(BaseCommand):
    help = "Generate fake products"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Numbers of creating products')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(product_name=f'Product_{i}', description=f'{i}-description',
                              price=randint(100, 100000)/100, quantity=randint(5, 50))
            product.save()
            self.stdout.write(f'{product}')
