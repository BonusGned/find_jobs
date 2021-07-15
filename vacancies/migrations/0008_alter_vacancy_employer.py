# Generated by Django 3.2.5 on 2021-07-13 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0007_auto_20210713_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to=settings.AUTH_USER_MODEL, verbose_name='Работодатель'),
        ),
    ]