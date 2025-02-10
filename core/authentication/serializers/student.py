from rest_framework import serializers
from core.authentication.models import Student, User
from core.authentication.serializers import UserSerializer

class StudentWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id', 'matricula', 'curso', 'turma', 'user']
        read_only_fields = ['curso']

    def validate_turma(self, value):
        valid_turmas = dict(Student.TURMA_CHOICES).keys()
        if value not in valid_turmas:
            raise serializers.ValidationError("Turma inválida")
        return value

    def validate_matricula(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Matrícula deve ter pelo menos 5 caracteres")
        return value

    def validate(self, data):
        if Student.objects.filter(matricula=data.get('matricula')).exists():
            raise serializers.ValidationError("Já existe um estudante com esta matrícula")
        return data

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'matricula', 'curso', 'turma', 'user']
        read_only_fields = ['curso']
        depth = 1
    

