from accounts.models import Account
from .models import Question
from rest_framework import viewsets, permissions
from .serializers import QuestionSerializer
from accounts.serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated

# QuestionViewSet


class QuestionViewSet(viewsets.ModelViewSet):
    # Check if user is authenticated
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(userName=self.request.user.name,
                        userSurname=self.request.user.surname)

    def get_queryset(self):
        queryset = Question.objects.all()

        # Query tags allowed
        id = self.request.query_params.get('id')
        user = self.request.query_params.get('user')
        isPublic = self.request.query_params.get('isPublic')
        # fields from user
        school = self.request.query_params.get('school')
        programme = self.request.query_params.get('programme')

        if id is not None:
            queryset = queryset.filter(id=id)
        if user is not None:
            queryset = queryset.filter(user=user)
        if isPublic is not None:
            queryset = queryset.filter(isPublic=isPublic)

        # fields from user
        if school is not None:
            user = self.request.user.school
            queryset = queryset.filter(user__school=school)

        # fields from user
        if programme is not None:
            user = self.request.user.programme
            queryset = queryset.filter(user__programme=programme)

        return queryset

    serializer_class = QuestionSerializer
