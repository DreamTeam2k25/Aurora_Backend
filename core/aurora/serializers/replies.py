from rest_framework.serializers import ModelSerializer
from core.aurora.models import Replies

class RepliesSerializer(ModelSerializer):
    class Meta:
        model = Replies
        fields = ['id', 'user', 'comment', 'reply', 'created_at', 'updated_at']
        depth = 2

class CreateRepliesSerializer(ModelSerializer):
    class Meta:
        model = Replies
        fields = '__all__'
