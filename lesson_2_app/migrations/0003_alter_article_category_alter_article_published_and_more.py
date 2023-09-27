# Generated by Django 4.2.5 on 2023-09-26 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_2_app', '0002_author_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(default='Humor', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateField(default=datetime.datetime(2023, 9, 26, 16, 35, 49, 17661, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='author',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2023, 9, 26, 16, 35, 49, 17021, tzinfo=datetime.timezone.utc)),
        ),
    ]
