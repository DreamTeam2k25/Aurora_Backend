from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
