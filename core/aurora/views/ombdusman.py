from core.aurora.models import Ombdusman
from core.aurora.serializers import OmbdusmanCreateSerializer, OmbdusmanSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

class PaginationOmbdusman(PageNumberPagination):
    page_size = 9

class ObdusmanViewSet(ModelViewSet):
    queryset = Ombdusman.objects.order_by('-id')
    serializer_class = OmbdusmanSerializer
    pagination_class = PaginationOmbdusman
    
    def get_serializer_class(self):
        if self.action == 'create':
            return OmbdusmanCreateSerializer
        return OmbdusmanSerializer