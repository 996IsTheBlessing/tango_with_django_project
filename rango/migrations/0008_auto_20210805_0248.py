# Generated by Django 2.1.5 on 2021-08-05 02:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20210805_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]