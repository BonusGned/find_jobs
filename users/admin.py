from django.contrib import admin

from users.models import Resume, SkillResume


class SkillInline(admin.TabularInline):
    model = SkillResume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    inlines = (SkillInline,)
