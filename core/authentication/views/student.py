from rest_framework import viewsets

from core.authentication.models import Student

from core.authentication.serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'matricula'
    filter_fields = ['matricula']
    search_fields = ['matricula']
    ordering_fields = ['matricula']
    ordering = ['matricula']
    