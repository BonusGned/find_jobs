from django.db import models
from multiselectfield import MultiSelectField

from users.models import User


class Vacancy(models.Model):
    ENTRY = 'Без опыта'
    MIDDLE = '1-3 год'
    SENIOR = 'от 3 и более лет'
    WORK_EXPERIENCE_CHOICES = [
        (ENTRY, 'Без опыта'),
        (MIDDLE, '1-3 год'),
        (SENIOR, 'от 3 и более лет'),
    ]
    REMOTE = 'Удалённая работа'
    FULL_TIME = 'Полная занятость'
    PART_TIME_EMPLOYMENT = 'Частичная занятость'
    TYPE_JOB = [
        (REMOTE, 'Удалённая работа'),
        (FULL_TIME, 'Полная занятость'),
        (PART_TIME_EMPLOYMENT, 'Частичная занятость'),
    ]
    title = models.CharField('Заголовок', max_length=50)
    description = models.TextField('Описание', max_length=5000)
    price = models.PositiveIntegerField('Зарплата', blank=True, null=True)
    work_experience = models.CharField('Опыт работы', choices=WORK_EXPERIENCE_CHOICES, max_length=20)
    type_job = MultiSelectField('Формат работы', choices=TYPE_JOB)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    employer = models.ForeignKey(User, related_name='vacancies', on_delete=models.CASCADE, verbose_name='Работадатель')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Skill(models.Model):
    name = models.CharField('Навык', max_length=124)
    vacancy = models.ForeignKey(Vacancy, related_name='skills', on_delete=models.CASCADE, verbose_name='Вакансия')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
