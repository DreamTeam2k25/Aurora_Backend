from rest_framework import serializers
from core.authentication.models import GuildMemberData

class GuildMemberDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuildMemberData
        fields = ['id', 'office', 'student', 'year_active']
        read_only_fields = ['verified', 'verification_token']