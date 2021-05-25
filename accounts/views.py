from .models import Account
from rest_framework import viewsets, permissions
from .serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response

# AccountViewSet


class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Account.objects.all()

        # Query tags allowed
        id = self.request.query_params.get('id')
        email = self.request.query_params.get('email')
        programme = self.request.query_params.get('programme')
        role = self.request.query_params.get('role')
        school = self.request.query_params.get('school')

        if id is not None:
            queryset = queryset.filter(id=id)
        if email is not None:
            queryset = queryset.filter(email=email)
        if programme is not None:
            queryset = queryset.filter(programme=programme)
        if role is not None:
            queryset = queryset.filter(role=role)
        if programme is not None:
            school = queryset.filter(school=school)

        return queryset
