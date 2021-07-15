from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.mixins import UpdateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from users.models import Resume, UserVacancyRelation
from users.permissions import IsOwnerOrReadOnly
from users.serializers import ResumeDetailSerializer, ResumeListSerializer, UserVacancySerializer
from vacancies.models import Vacancy
from vacancies.serializers import VacancyListSerializer


class ResumeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Resume.objects.filter(user=self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ResumeListSerializer
        elif self.action == 'retrieve':
            return ResumeDetailSerializer

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class UserBookmarkVacancyView(UpdateModelMixin, GenericViewSet):
    serializer_class = UserVacancySerializer
    lookup_field = 'vacancy'

    def get_object(self):
        print(self.kwargs)
        vacancy = Vacancy.objects.get(pk=self.kwargs['vacancy'])
        obj, created = UserVacancyRelation.objects.get_or_create(user=self.request.user, vacancy=vacancy)
        return obj


class BookmarksListView(ListModelMixin, GenericViewSet):
    serializer_class = VacancyListSerializer

    def get_queryset(self):
        return Vacancy.objects.filter(relations__user=self.request.user, relations__in_bookmarks=True)


class ResponsesListView(ListModelMixin, GenericViewSet):
    serializer_class = VacancyListSerializer

    def get_queryset(self):
        return UserVacancyRelation.objects.filter(user=self.request.user, in_response=True).vacancy.all()
