from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from core.authentication.models import GuildMemberData, Student, Office
from django.db import transaction

class UpdateMemberDataView(APIView):
    def _get_objects(self, student_id: int, office_id: int) -> tuple:
        """
        Recupera os objetos Student e Office ou retorna 404 se não encontrados.
        """
        student = get_object_or_404(Student, id=student_id)
        office = get_object_or_404(Office, id=office_id)
        return student, office

    def post(self, request, student_id: int, office_id: int) -> Response:
        """
        Associa um estudante a um cargo do grêmio.
        """
        try:
            with transaction.atomic():
                student, office = self._get_objects(student_id, office_id)

                if GuildMemberData.objects.filter(student=student, office=office).exists():
                    return Response(
                        {"detail": "Estudante já associado a este office."},
                        status=status.HTTP_409_CONFLICT
                    )

                GuildMemberData.objects.create(student=student, office=office)
                student.is_guild_member = True
                student.save()

                return Response(
                    {"detail": "Registro criado com sucesso."}, 
                    status=status.HTTP_201_CREATED
                )
        except Exception as e:
            return Response(
                {"detail": f"Erro ao criar registro: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, student_id: int, office_id: int) -> Response:
        """
        Remove a associação de um estudante com um cargo do grêmio.
        """
        try:
            student, office = self._get_objects(student_id, office_id)
            
            deleted_count = GuildMemberData.objects.filter(
                student=student, 
                office=office
            ).delete()[0]

            if deleted_count == 0:
                return Response(
                    {"detail": "Nenhum registro encontrado para deletar."},
                    status=status.HTTP_404_NOT_FOUND
                )

            return Response(
                {"detail": "Registro deletado com sucesso."}, 
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"detail": f"Erro ao deletar registro: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
