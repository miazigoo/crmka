# Generated by Django 3.0.4 on 2020-04-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, db_index=True, max_length=28, verbose_name='Имя Клиента')),
                ('customer_surname', models.CharField(blank=True, db_index=True, max_length=28, verbose_name='Фамилия Клиента')),
                ('customer_patronymic', models.CharField(blank=True, db_index=True, max_length=28, verbose_name='Отчество Клиента')),
                ('customer_phone', models.IntegerField(blank=True, db_index=True, verbose_name='Номер Клиента')),
                ('uznali_o_nas', models.CharField(blank=True, max_length=48, verbose_name='Узнали о нас ')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]