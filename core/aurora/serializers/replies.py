from rest_framework.serializers import ModelSerializer
from core.aurora.models import Replies, ReplieOfReplie

class RepliesSerializer(ModelSerializer):
    class Meta:
        model = Replies
        fields = ['id', 'user', 'comment', 'reply', 'created_at', 'updated_at']
        depth = 2

class CreateRepliesSerializer(ModelSerializer):
    class Meta:
        model = Replies
        fields = '__all__'

class ReplieOfReplieSerializer(ModelSerializer):
    class Meta:
        model = ReplieOfReplie
        fields = ['id', 'user', 'comment_replie']
        depth = 2

class ReplieOfReplieCreateSerializer(ModelSerializer):
    class Meta:
        model = ReplieOfReplie,
        fields = '__all__'
