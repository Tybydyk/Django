from django.core.management.base import BaseCommand
from hw2_store_app.models import User, Product, Order


class Command(BaseCommand):
    help = "Delete order by user_id."

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='user id')

    def handle(self, *args, **kwargs):
        user_id = kwargs.get('user_id')
        user = User.objects.filter(pk=user_id).first()
        if user is not None:
            orders = Order.objects.filter(customer=user).all()
            if orders is not None:
                self.stdout.write(f'User {user}"s orders will be deleted: {orders}')
                for order in orders:
                    order.delete()