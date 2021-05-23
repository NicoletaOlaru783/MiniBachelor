from .models import Comment
from rest_framework import viewsets, permissions
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated

# CommentViewSet


class CommentViewSet(viewsets.ModelViewSet):
    # Check if user is authenticated
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Comment.objects.all()
        # Query tags allowed
        id = self.request.query_params.get('id')
        questionId = self.request.query_params.get('questionId')
        projectId = self.request.query_params.get('projectId')

        if id is not None:
            queryset = queryset.filter(id=id)
        if questionId is not None:
            queryset = queryset.filter(questionId=questionId)
        if projectId is not None:
            queryset = queryset.filter(projectId=projectId)

        return queryset

    serializer_class = CommentSerializer
