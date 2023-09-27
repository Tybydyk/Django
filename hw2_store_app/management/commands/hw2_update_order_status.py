from django.core.management.base import BaseCommand
from hw2_store_app.models import Order


class Command(BaseCommand):
    help = "Update order status by order_id."

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='order_id')
        parser.add_argument('order_status', type=str, help='order_status - INWORK, FINISHED, CANCELED')

    def handle(self, *args, **kwargs):
        order_id = kwargs.get('order_id')
        order = Order.objects.filter(pk=order_id).first()
        if order is not None:
            order_status = kwargs.get('order_status')
            if order_status in ['INWORK', 'FINISHED', 'CANCELED']:
                order.status = order_status
                order.save()
            self.stdout.write(f'Status of order {order} was changed to {order_status}')
