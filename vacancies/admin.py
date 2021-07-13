from django.contrib import admin

from vacancies.models import Vacancy, Skill


class SkillInline(admin.TabularInline):
    model = Skill


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    inlines = (SkillInline,)
