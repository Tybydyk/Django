from django.core.management.base import BaseCommand
from hw2_store_app.models import Product


class Command(BaseCommand):
    help = "Get product by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            self.stdout.write(f'ID {pk} : {product}')