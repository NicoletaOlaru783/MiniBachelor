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

    def get_queryset(self):
        queryset = Question.objects.all()
        # Query tags allowed
        id = self.request.query_params.get('id')
        user = self.request.query_params.get('user')
        isPublic = self.request.query_params.get('isPublic')
        # fields from user
        school = self.request.query_params.get('school')

        if id is not None:
            queryset = queryset.filter(id=id)
        if user is not None:
            queryset = queryset.filter(user=user)
        if isPublic is not None:
            queryset = queryset.filter(isPublic=isPublic)

        # fields from user
        user = self.request.user
        if school is not None:
            queryset = queryset.filter(user=school)
        return queryset

    serializer_class = QuestionSerializer
