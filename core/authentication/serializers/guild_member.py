from rest_framework import serializers
from core.authentication.models import Student

class GuildMemberDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'