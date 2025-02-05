from django_filters.rest_framework import DjangoFilterBackend
from core.aurora.serializers import RepliesSerializer, CreateRepliesSerializer
from core.aurora.models import Replies
from rest_framework.viewsets import ModelViewSet
from core.aurora.filter.filter_replies import RepliesFilter

class RepliesViewSet(ModelViewSet):
    queryset = Replies.objects.all()
    serializer_class = RepliesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RepliesFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateRepliesSerializer
        return RepliesSerializer
