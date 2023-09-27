from django.core.management.base import BaseCommand
from lesson_2_app.models import Author, Article


class Command(BaseCommand):
    help = "Delete authors by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = Author.objects.filter(pk=pk).first()
        if author is not None:
            author.delete()
        self.stdout.write(f'{author}')