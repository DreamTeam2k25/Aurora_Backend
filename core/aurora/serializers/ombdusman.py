from core.aurora.models import Ombdusman
from core.authentication.models import User
from rest_framework.serializers import ModelSerializer, SlugRelatedField

class OmbdusmanCreateSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=User.objects.all())
    class Meta:
        model = Ombdusman
        fields = '__all__'

class OmbdusmanSerializer(ModelSerializer):
    class Meta:
        model = Ombdusman
        fields = '__all__'
        depth=1

