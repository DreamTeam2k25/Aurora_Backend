from django.core.cache import cache
from django.shortcuts import get_object_or_404

from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.authentication.serializers import GuildMemberDataSerializer
from core.authentication.models import GuildMemberData

class Verify(APIView):
    def get(self, request, student_id):
        cache_key = f"verified_status_{student_id}"
        verified_status = cache.get(cache_key)
        
        if verified_status is None:
            member = get_object_or_404(GuildMemberData, student=student_id)
            verified_status = member.verified
            cache.set(cache_key, verified_status, 60*60)
        
        return Response({'student': student_id, 'verified': verified_status}, status = status.HTTP_200_OK)
    
@api_view(['GET'])
def verify_member(resquest, verify_token):
    try:
        member = GuildMemberData.objects.get(verification_token=verify_token)
    except GuildMemberData.DoesNotExist:
        return Response({'error': 'Token de verificação inválido'}, status=status.HTTP_404_NOT_FOUND)
    
    member.verified= True
    member.verification_token = None
    member.save()
    print(member.student)
    cache.delete(f"verified_status_{member.student.id}")  
    
    return Response({'message': 'Usuário verificado com sucesso'}, status=status.HTTP_200_OK)

