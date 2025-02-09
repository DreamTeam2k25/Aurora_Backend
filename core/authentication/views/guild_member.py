from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.authentication.serializers import GuildMemberDataSerializer
from core.authentication.models import GuildMemberData

class GuildMemberViewSet(viewsets.ModelViewSet):
    queryset = GuildMemberData.objects.all()
    serializer_class = GuildMemberDataSerializer
    lookup_field = 'id'

    http_method_names = ['get', 'post', 'patch', 'put']

    ordering_fields = ['id']
    ordering = ['id']
    
@api_view(['GET'])
def verify_member(resquest, verify_token):
    try:
        member = GuildMemberData.objects.get(verification_token=verify_token)
    except GuildMemberData.DoesNotExist:
        return Response({'error': 'Token de verificação inválido'}, status=status.HTTP_404_NOT_FOUND)
    
    member.verified= True
    member.verification_token = None
    member.save()
    
    return Response({'message': 'Usuário verificado com sucesso'}, status=status.HTTP_200_OK)