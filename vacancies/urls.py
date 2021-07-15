from django.urls import path

from vacancies.views import VacancyViewSet

urlpatterns = [
    path('', VacancyViewSet.as_view({'get': 'list'})),
    path('<int:pk>/', VacancyViewSet.as_view({'get': 'retrieve'})),
    path('<int:pk>/', VacancyViewSet.as_view({'post': 'create'})),
]
