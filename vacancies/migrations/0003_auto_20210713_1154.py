# Generated by Django 3.2.5 on 2021-07-13 11:54

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_auto_20210713_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='type_job',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Удалённая работа', 'Удалённая работа'), ('Полная занятость', 'Полная занятость'), ('Частичная занятость', 'Частичная занятость')], max_length=53, verbose_name='Формат работы'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='work_experience',
            field=models.CharField(choices=[('Без опыта', 'Без опыта'), ('1-3 год', '1-3 год'), ('от 3 и более лет', 'от 3 и более лет')], max_length=20, verbose_name='Опыт работы'),
        ),
    ]