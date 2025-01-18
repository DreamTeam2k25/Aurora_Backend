from rest_framework import serializers
from core.authentication.models import Student, User, guild_member
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
                user_data = validated_data.pop('user')
                user = User.objects.create(**user_data)

                turma = validated_data.get("turma", "")
                if turma in ['1info1', '1info2', '1info3', '2info1', '2info2', '2info3', '3info1', '3info2', '3info3']:
                    validated_data["curso"] = "informatica"
                elif turma in ['1agro1', '1agro2', '1agro3', '2agro1', '2agro2', '2agro3', '3agro1', '3agro2', '3agro3']:
                    validated_data["curso"] = "agropecuaria"
                elif turma in ['1quimi', '2quimi', '3quimi']:
                    validated_data["curso"] = "quimica"

                student = Student.objects.create(user=user, **validated_data)

                return student

            except Exception as e:
                raise serializers.ValidationError(f"Erro ao criar o estudante: {e}")

    def update(self, instance, validated_data):
        with transaction.atomic():
            try:
                # Atualizar os dados do usuário
                user_data = validated_data.pop('user', None)
                if user_data:
                    for attr, value in user_data.items():
                        current_value = getattr(instance.user, attr, None)
                        if current_value != value:  # Apenas atualiza se o valor for diferente
                            setattr(instance.user, attr, value)
                    instance.user.save()

                # Determinar o curso com base na turma
                turma = validated_data.get("turma", "")
                if turma in ['1info1', '1info2', '1info3', '2info1', '2info2', '2info3', '3info1', '3info2', '3info3']:
                    validated_data["curso"] = "informatica"
                elif turma in ['1agro1', '1agro2', '1agro3', '2agro1', '2agro2', '2agro3', '3agro1', '3agro2', '3agro3']:
                    validated_data["curso"] = "agropecuaria"
                elif turma in ['1quimi', '2quimi', '3quimi']:
                    validated_data["curso"] = "quimica"

                # Atualizar os dados do estudante
                for attr, value in validated_data.items():
                    setattr(instance, attr, value)
                instance.save()

                # Adicionar o estudante como membro da guilda, se aplicável
                if instance.is_guild_member:
                    guild_member.objects.get_or_create(student=instance)

                return instance

            except Exception as e:
                raise serializers.ValidationError(f"Erro ao atualizar o estudante: {e}")
