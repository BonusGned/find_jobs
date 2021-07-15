from rest_framework import serializers

from users.models import Resume, UserVacancyRelation


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class ResumeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('title', 'description')


class UserVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVacancyRelation
        fields = ('in_bookmarks', 'in_response')
