# Generated by Django 3.2.4 on 2021-08-25 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_list', '0002_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=400)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks_list.users')),
            ],
        ),
    ]
