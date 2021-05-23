from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated

# ProjectViewSet


class ProjectViewSet(viewsets.ModelViewSet):
    # Check if user is authenticated
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Project.objects.all()
        # Query tags allowed
        id = self.request.query_params.get('id')
        user = self.request.query_params.get('user')

        if id is not None:
            queryset = queryset.filter(id=id)
        if user is not None:
            queryset = queryset.filter(user=user)

        return queryset

    serializer_class = ProjectSerializer
