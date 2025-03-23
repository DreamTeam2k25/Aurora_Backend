from core.aurora.models import Ombdusman
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.authentication.models import User

class OmbdusmanCreateSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    class Meta:
        model = Ombdusman
        fields = '__all__'

class OmbdusmanSerializer(ModelSerializer):
    class Meta:
        model = Ombdusman
        fields = '__all__'

