from core.aurora.models import Reactions
from core.aurora.serializers import ReactionsSerializer
from rest_framework.viewsets import ModelViewSet

class ReactionsViewSet(ModelViewSet):
    queryset = Reactions.objects.all()
    serializer_class = ReactionsSerializer