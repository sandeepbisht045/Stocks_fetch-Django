# Generated by Django 3.2.4 on 2021-08-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_list', '0004_stock_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='desc',
            field=models.CharField(max_length=10000),
        ),
    ]
