from rest_framework import viewsets
from core.authentication.models import Student, User
from core.authentication.serializers import StudentSerializer
import django_filters
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from core.authentication.utils import select_course_by_turma

class StudentFilter(django_filters.FilterSet):
    TURMA_CHOICES = [
        ('1info1', '1info1'),
        ('1info2', '1info2'),
        ('1info3', '1info3'),
        ('2info1', '2info1'),
        ('2info2', '2info2'),
        ('2info3', '2info3'),
        ('3info1', '3info1'),
        ('3info2', '3info2'),
        ('3info3', '3info3'),
        ('1agro1', '1agro1'),
        ('1agro2', '1agro2'),
        ('1agro3', '1agro3'),
        ('2agro1', '2agro1'),
        ('2agro2', '2agro2'),
        ('2agro3', '2agro3'),
        ('3agro1', '3agro1'),
        ('3agro2', '3agro2'),
        ('3agro3', '3agro3'),
        ('1quimi', '1quimi'),
        ('2quimi', '2quimi'),
        ('3quimi', '3quimi'),
    ]
    
    CURSO_CHOICES = [
        ('informatica', 'Informatica Para Internet'),
        ('quimica', 'Quimica'),
        ('agropecuaria', 'Agropecuaria'),
    ]
    id = django_filters.NumberFilter()
    matricula = django_filters.CharFilter(lookup_expr='icontains')
    curso = django_filters.ChoiceFilter(choices=Student.CURSO_CHOICES)
    turma = django_filters.ChoiceFilter(choices=Student.TURMA_CHOICES)

    class Meta:
        model = Student
        fields = ['id', 'matricula', 'curso', 'turma']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'
    filterset_class = StudentFilter
    ordering_fields = ['matricula']
    ordering = ['matricula']

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
                user_data = serializer.validated_data.pop('user')
                user = User.objects.create(**user_data)

                turma = serializer.validated_data.get("turma", "")
                curso = select_course_by_turma(turma)
                
                student = Student.objects.create(
                    user=user,
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
        
        
    