from django.contrib import admin

from users.models import Resume, SkillResume, UserVacancyRelation, User


class SkillInline(admin.TabularInline):
    model = SkillResume


class UserVacancyRelationInline(admin.TabularInline):
    model = UserVacancyRelation


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (UserVacancyRelationInline,)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    inlines = (SkillInline,)
