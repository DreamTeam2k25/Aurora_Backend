from core.aurora.models import Ombdusman
from rest_framework.serializers import ModelSerializer

class OmbdusmanCreateSerializer(ModelSerializer):
    class Meta:
        model = Ombdusman
        fields = '__all__'

class OmbdusmanSerializer(ModelSerializer):
    class Meta:
        model = Ombdusman
        fields = '__all__'

