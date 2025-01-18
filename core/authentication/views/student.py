from rest_framework import viewsets

from core.authentication.models import Student

from core.authentication.serializers import StudentSerializer

import django_filters


class StudentFilter(django_filters.FilterSet):
    TURMA_CHOICES = [
        ('1info1', '1info1'),
        ('1info2', '1info2'),
        ('1info3', '1info3'),
        ('2info1', '1info1'),
        ('2info2', '1info2'),
        ('2info3', '1info3'),
        ('3info1', '1info1'),
        ('3info2', '1info2'),
        ('3info3', '1info3'),
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
    lookup_field = 'matricula'
    filterset_class = StudentFilter


    ordering_fields = ['matricula']
    ordering = ['matricula']
    