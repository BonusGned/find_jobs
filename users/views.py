from rest_framework import viewsets

from users.models import Resume
from users.serializers import ResumeDetailSerializer, ResumeListSerializer


class ResumeViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Resume.objects.filter(user=self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ResumeListSerializer
        elif self.action == 'retrieve':
            return ResumeDetailSerializer
