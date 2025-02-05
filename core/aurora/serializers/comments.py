from rest_framework.serializers import ModelSerializer
from core.aurora.models import Comments

class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'post', 'user', 'comment', 'created_at', 'updated_at']
        depth = 2

class CreateCommentSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
