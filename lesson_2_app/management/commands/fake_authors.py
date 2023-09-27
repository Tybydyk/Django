from django.core.management.base import BaseCommand
from lesson_2_app.models import Author, Article


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Numbers of ccreating authors')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(f_name=f'Name{i}', l_name=f'LastName{i}' , email=f'mail{i}@mail.ru')
            author.save()
            self.stdout.write(f'{author}')
            for j in range(1, count + 1):
                article = Article(title=f'Title{j}',
                                  content=f'Text from {author.f_name} #{j} is bla bla bla many long text',
                                    author=author)
                article.save()
                self.stdout.write(f'{article}')