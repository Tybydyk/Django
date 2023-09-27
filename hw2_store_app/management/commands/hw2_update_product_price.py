

from django.core.management.base import BaseCommand
from hw2_store_app.models import Product


class Command(BaseCommand):
    help = "Update product price by product_id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='product ID')
        parser.add_argument('new_prise', type=str, help='new prise')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.price = kwargs.get('new_prise')
            product.save()
        self.stdout.write(f'{product}')