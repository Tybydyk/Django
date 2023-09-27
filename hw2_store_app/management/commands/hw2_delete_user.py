from django.core.management.base import BaseCommand
from hw2_store_app.models import User


class Command(BaseCommand):
    help = "Delete user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='user ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            self.stdout.write(f'{user} will be deleted ')
            user.delete()