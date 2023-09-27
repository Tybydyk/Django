from django.core.management.base import BaseCommand
from hw2_store_app.models import User


class Command(BaseCommand):
    help = "Update user phone by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='user ID')
        parser.add_argument('phone', type=str, help='user phone')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            user.phone = kwargs.get('phone')
            user.save()
        self.stdout.write(f'{user}')