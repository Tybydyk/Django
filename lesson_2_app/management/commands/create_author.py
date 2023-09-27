from django.core.management.base import BaseCommand
from lesson_2_app.models import Author


class Command(BaseCommand):
    help = "Create author."

    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com',password='secret', age=25)
        author = Author(f_name='Nike', l_name='last_name', email='nike@example.com')
        author.save()
        self.stdout.write(f'{author}')