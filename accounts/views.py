from .models import Account
from rest_framework import viewsets, permissions
from .serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response

# AccountViewSet


class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = AccountSerializer

    def retrieve(self, request, *args, **kwargs):
        # Check if user is authenticated
        permission_classes = (IsAuthenticated,)

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
        if school is not None:
            school = queryset.filter(school=school)

        return queryset

    def create(self, request, *args, **kwargs):
        # Check if user is authenticated
        permission_classes = [
            permissions.AllowAny
        ]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
