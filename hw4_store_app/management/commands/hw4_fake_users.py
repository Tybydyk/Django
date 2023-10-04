from django.core.management.base import BaseCommand
from hw4_store_app.models import User

class Command(BaseCommand):
    help = "Generate fake users"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Numbers of creating users')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user = User(name=f'Name{i}', email=f'mail{i}@mail.ru', phone=f'{i}11-{i}22-{i}3-{i}4',
                          address=f'room {i}, {i}-street, City_{i}')
            user.save()
            self.stdout.write(f'{user}')