from django.core.management.base import BaseCommand
from hw2_store_app.models import User, Product, Order


class Command(BaseCommand):
    help = "Get order by user_name."

    def add_arguments(self, parser):
        parser.add_argument('user_name', type=str, help='user name')

    def handle(self, *args, **kwargs):
        user_name = kwargs.get('user_name')
        user = User.objects.filter(name=user_name).first()
        if user is not None:
            orders = Order.objects.filter(customer=user).all()
            if orders is not None:
                self.stdout.write(f'User {user}"s orders are: {orders}')
