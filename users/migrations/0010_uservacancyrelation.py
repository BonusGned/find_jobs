# Generated by Django 3.2.5 on 2021-07-13 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0006_alter_uservacancyrelation_options'),
        ('users', '0009_alter_resume_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVacancyRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_bookmarks', models.BooleanField(default=False, verbose_name='Избранное')),
                ('in_response', models.BooleanField(default=False, verbose_name='Отклик')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations', to=settings.AUTH_USER_MODEL, verbose_name='Соискатель')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations', to='vacancies.vacancy', verbose_name='Вакансия')),
            ],
            options={
                'verbose_name': 'Закладки и отклики',
                'verbose_name_plural': 'Закладки и отклики',
            },
        ),
    ]
