# Generated by Django 2.1.5 on 2021-08-06 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0010_category_followed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='followed',
        ),
    ]
