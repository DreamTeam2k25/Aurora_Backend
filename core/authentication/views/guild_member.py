from rest_framework import viewsets

from core.authentication.serializers import GuildMemberDataSerializer
from core.authentication.models import GuildMemberData

class GuildMemberViewSet(viewsets.ModelViewSet):
    queryset = GuildMemberData.objects.all()
    serializer_class = GuildMemberDataSerializer
    lookup_field = 'id'

    http_method_names = ['get', 'post', 'patch', 'put']

    ordering_fields = ['id']
    ordering = ['id']
    