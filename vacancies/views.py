from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from vacancies.models import Vacancy
from vacancies.serializers import VacancyDetailSerializer, VacancyListSerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ['price', 'location', 'type_job']
    search_fields = ['title', 'description']
    ordering_fields = ['created']

    def get_serializer_class(self):
        if self.action == 'list':
            return VacancyListSerializer
        elif self.action == 'retrieve':
            return VacancyDetailSerializer

    def perform_create(self, serializer):
        serializer.data['employer'] = self.request.user
        serializer.save()
