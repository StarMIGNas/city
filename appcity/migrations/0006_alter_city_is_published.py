# Generated by Django 4.2.1 on 2024-11-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcity', '0005_rename_time_creat_city_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=0, verbose_name='Статус'),
        ),
    ]
