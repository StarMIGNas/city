# Generated by Django 4.2.1 on 2024-11-27 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.SlugField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]