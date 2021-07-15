from rest_framework import serializers

from users.models import Resume, UserVacancyRelation


class ResumeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class ResumeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class UserVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVacancyRelation
        fields = ('in_bookmarks', 'in_response')
