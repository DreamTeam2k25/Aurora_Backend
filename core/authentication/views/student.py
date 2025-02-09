from rest_framework import viewsets
from core.authentication.models import Student
from core.authentication.serializers import StudentDetailSerializer, StudentWriteSerializer
from rest_framework.response import Response
from core.authentication.filters import StudentFilter
from rest_framework import status
from django.db import transaction
from core.authentication.utils import select_course_by_turma

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    lookup_field = 'id'
    filterset_class = StudentFilter
    ordering_fields = ['matricula']
    ordering = ['matricula']
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return StudentDetailSerializer
        return StudentWriteSerializer

    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response({'error': f'Erro ao listar os estudantes: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            with transaction.atomic():
                user_id = serializer.validated_data.pop('user')

                turma = serializer.validated_data.get("turma", "")
                curso = select_course_by_turma(turma)
                
                student = Student.objects.create(
                    user=user_id,
                    curso=curso,
                    **serializer.validated_data
                )

                response_serializer = self.get_serializer(student)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {'error': f'Erro ao criar estudante: {str(e)}'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        
    