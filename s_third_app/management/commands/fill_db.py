from random import choices
from django.core.management.base import BaseCommand
from s_third_app.models import Author, Post


LOREM = 'Orci nulla pellentesque dignissim enim sit. Elit ullamcorper dignissim cras tincidunt lobortis. Purus  ' \
'accumsan in nisl nisi. Parturient montes nascetur ridiculus mus. Fermentum et sollicitudin ac orci phasellus ' \
'egestas. Maecenas pharetra convallis posuere morbi. Eget felis eget nunc lobortis mattis aliquam. Orci porta non ' \
'pulvinar neque laoreet suspendisse interdum consectetur. Enim praesent elementum facilisis leo vel. Commodo ' \
'viverra maecenas accumsan lacus vel facilisis volutpat est. Imperdiet massa tincidunt nunc pulvinar sapien. Id ' \
'diam maecenas ultricies mi eget mauris pharetra. Posuere ac ut consequat semper. Aliquet nibh praesent tristique ' \
'magna sit amet purus gravida quis. At elementum eu facilisis sed odio morbi quis. Amet justo donec enim diam ' \
'vulputate ut. Egestas integer eget aliquet nibh praesent tristique magna sit amet. Feugiat vivamus at augue eget ' \
'arcu dictum varius duis at.'

class Command(BaseCommand):
    help = "Generate fake authors and posts."
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')
    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=64)),
                    author=author
                )
                post.save()