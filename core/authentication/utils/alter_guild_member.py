from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from core.authentication.models import GuildMemberData, Student, Office

class UpdateMemberDataView(APIView):
    def post(self, request, student_id, office_id):
        student = get_object_or_404(Student, id=student_id)
        office = get_object_or_404(Office, id=office_id)

        existing_record = GuildMemberData.objects.filter(student=student, office=office).exists()
        if existing_record:
            return Response(
                {"detail": "Estudante já associado a este office."},
                status=status.HTTP_409_CONFLICT
            )

        GuildMemberData.objects.create(student=student, office=office)
        return Response({"detail": "Registro criado com sucesso."}, status=status.HTTP_201_CREATED)

    def delete(self, request, student_id, office_id):
        student = get_object_or_404(Student, id=student_id)
        office = get_object_or_404(Office, id=office_id)
        
        deleted_count = GuildMemberData.objects.filter(student=student, office=office).delete()[0]
        if deleted_count == 0:
            return Response(
                {"detail": "Nenhum registro encontrado para deletar."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response({"detail": "Registro deletado com sucesso."}, status=status.HTTP_200_OK)
