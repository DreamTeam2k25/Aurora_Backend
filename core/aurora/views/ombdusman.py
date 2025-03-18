from core.aurora.models import Ombdusman
from core.aurora.serializers import OmbdusmanCreateSerializer, OmbdusmanSerializer
from rest_framework.viewsets import ModelViewSet



class ObdusmanViewSet(ModelViewSet):
    queryset = Ombdusman.objects.order_by('?')
    serializer_class = OmbdusmanSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return OmbdusmanCreateSerializer
        return OmbdusmanSerializer

  