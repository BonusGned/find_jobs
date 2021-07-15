import uuid as uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import CustomUserManager
from vacancies.models import Vacancy


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField('Email адрес', unique=True)
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Фамилия', max_length=20)
    location = models.CharField('Место нахождения', max_length=124)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    phone_number = PhoneNumberField('Номер телефона', unique=True, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'location']

    def __str__(self):
        return f'{self.first_name} {self.last_name} | Email: {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='resumes', on_delete=models.CASCADE, verbose_name='Соискатель')
    title = models.CharField('Заголовок', max_length=124)
    description = models.TextField('Информация о пользователе', max_length=5000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'


class UserVacancyRelation(models.Model):
    user = models.ForeignKey(User, related_name='relations', on_delete=models.CASCADE, verbose_name='Соискатель')
    vacancy = models.ForeignKey(Vacancy, related_name='relations', on_delete=models.CASCADE,
                                verbose_name='Вакансия')
    in_bookmarks = models.BooleanField('Избранное', default=False)
    in_response = models.BooleanField('Отклик', default=False)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}: {self.vacancy.title}, Заклдаки: {self.in_bookmarks}, ' \
               f'Отклик: {self.in_response}'

    class Meta:
        verbose_name = 'Закладки и отклики'
        verbose_name_plural = 'Закладки и отклики'


class SkillResume(models.Model):
    name = models.CharField('Наименование навыка', max_length=124)
    resume = models.ForeignKey(Resume, related_name='skills', on_delete=models.CASCADE, verbose_name='Резюме')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
