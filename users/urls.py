from django.urls import path

from users.views import ResumeViewSet

urlpatterns = [
    path('resume/', ResumeViewSet.as_view({'get': 'list'})),
    path('resume/<slug:pk>/', ResumeViewSet.as_view({'get': 'retrieve'})),
]
