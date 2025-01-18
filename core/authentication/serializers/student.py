from rest_framework import serializers
from core.authentication.models import Student, User
from core.authentication.serializers import UserSerializer


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['matricula', 'user', 'curso', 'turma', 'is_guild_member']
        read_only_fields = ['curso', 'is_guild_member']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        
        user = User.objects.create(**user_data)
        
        print(validated_data)
        if validated_data["turma"] in ['1info1', '1info2', '1info3', '2info1', '2info2', '2info3', '3info1', '3info2', '3info3']:
            validated_data["curso"] = "informatica"
        elif validated_data["turma"] in ['1agro1', '1agro2', '1agro3', '2agro1', '2agro2', '2agro3', '3agro1', '3agro2', '3agro3']:
            validated_data["curso"] = "agropecuaria"
        elif validated_data["turma"] in ['1quimi', '2quimi', '3quimi']:
            validated_data["curso"] = "quimica"
        student = Student.objects.create(user=user, **validated_data)

        return student