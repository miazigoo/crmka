# Generated by Django 3.0.4 on 2020-04-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='customer',
        ),
        migrations.AddField(
            model_name='post',
            name='customer',
            field=models.ManyToManyField(blank=True, null=True, to='customer.Customer', verbose_name='Клиент'),
        ),
    ]