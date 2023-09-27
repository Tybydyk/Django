from django.core.management.base import BaseCommand
from hw2_store_app import models


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='user ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = models.User.objects.filter(pk=pk).first()
        if user is not None:
            self.stdout.write(f'{user}')