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

        # fields from user
        school = self.request.query_params.get('school')
        programme = self.request.query_params.get('programme')

        if id is not None:
            queryset = queryset.filter(id=id)
        if user is not None:
            queryset = queryset.filter(user=user)

        # fields from user
        if school is not None:
            user = self.request.user.school
            queryset = queryset.filter(user__school=school)

        # fields from user
        if programme is not None:
            user = self.request.user.programme
            queryset = queryset.filter(user__programme=programme)

        return queryset

    serializer_class = ProjectSerializer
