from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from core.authentication.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'last_login', 'date_joined']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está em uso")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Este nome de usuário já está em uso")
        if len(value) < 3:
            raise serializers.ValidationError("Nome de usuário deve ter pelo menos 3 caracteres")
        return value

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Nome deve ter pelo menos 3 caracteres")
        return value

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        
        data['user_id'] = self.user.id
        data['name'] = self.user.name
        data['email'] = self.user.email
        data['username'] = self.user.username

        # Se houver relacionamentos, você pode incluir também
        # if hasattr(self.user, 'profile'):
        #     data['profile'] = {
        #         'bio': self.user.profile.bio,
        #         'image': self.user.profile.image.url if self.user.profile.image else None,
        #     }
        
        return data
