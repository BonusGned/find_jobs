from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from vacancies.models import Vacancy
from vacancies.serializers import VacancyDetailSerializer, VacancyListSerializer


class VacancyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vacancy.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_serializer_class(self):
        if self.action == 'list':
            return VacancyListSerializer
        elif self.action == 'retrieve':
            return VacancyDetailSerializer
