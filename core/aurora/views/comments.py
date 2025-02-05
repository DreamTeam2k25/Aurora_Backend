from django_filters.rest_framework import DjangoFilterBackend
from core.aurora.serializers import CommentsSerializer, CreateCommentSerializer
from core.aurora.models import Comments
from rest_framework.viewsets import ModelViewSet
from core.aurora.filter.filter_comments import CommentsFilter 

class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentsFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCommentSerializer
        return CommentsSerializer
