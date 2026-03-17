from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Trail
from .serializers import TrailListSerializer, TrailDetailSerializer

class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.prefetch_related('images', 'likes', 'comments').all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['location', 'difficulty']
    search_fields = ['name', 'description', 'keywords']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TrailDetailSerializer
        return TrailListSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
