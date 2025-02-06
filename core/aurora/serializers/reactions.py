from rest_framework.serializers import ModelSerializer
from core.aurora.models import Reactions

class ReactionsSerializer(ModelSerializer):
    class Meta:
        model = Reactions
        fields = '__all__'
        