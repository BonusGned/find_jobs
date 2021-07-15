from django.db import models
from multiselectfield import MultiSelectField


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
    location = models.CharField('Страна/Город', max_length=200, blank=True, null=True)
    address = models.CharField('Адрес', max_length=200, blank=True, null=True)
    work_experience = models.CharField('Опыт работы', choices=WORK_EXPERIENCE_CHOICES, max_length=20)
    type_job = MultiSelectField('Формат работы', choices=TYPE_JOB)
    created = models.DateTimeField('Дата публикации', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)
    employer = models.ForeignKey('users.User', related_name='vacancies', on_delete=models.CASCADE,
                                 verbose_name='Работодатель')
    responding = models.ManyToManyField('users.User', through='users.UserVacancyRelation', related_name='my_vacancies')

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
