from rest_framework import serializers
from core.authentication.models import Student, User, guild_member
from core.authentication.utils import select_course_by_turma
from core.authentication.serializers import UserSerializer
from django.db import transaction

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['id', 'matricula', 'curso', 'turma', 'is_guild_member', 'user']
        read_only_fields = ['curso', 'is_guild_member']

    def create(self, validated_data):
        with transaction.atomic():
            try:
                # Criando o usuário
                user_data = validated_data.pop('user')
                user = User.objects.create(**user_data)

                # Definindo o curso com base na turma
                turma = validated_data.get("turma", "")
                validated_data["curso"] = select_course_by_turma(turma)

                # Criando o estudante
                student = Student.objects.create(user=user, **validated_data)
                return student

            except Exception as e:
                raise serializers.ValidationError(f"Erro ao criar o estudante: {e}")
