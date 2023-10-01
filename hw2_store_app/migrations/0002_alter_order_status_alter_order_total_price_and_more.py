# Generated by Django 4.2.5 on 2023-09-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw2_store_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('INWORK', 'in_working'), ('FINISHED', 'finished'), ('CANCELED', 'canceled')], default='INWORK', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=15),
        ),
    ]
