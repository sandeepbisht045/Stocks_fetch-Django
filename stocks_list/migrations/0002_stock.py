# Generated by Django 3.2.4 on 2021-08-24 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('symbol', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=30)),
            ],
        ),
    ]
