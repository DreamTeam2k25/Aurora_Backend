from rest_framework import serializers
from core.uploader.models import Video

class VideoUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)
    description = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = Video
        fields = ["id", "file", "description", "uploaded_on"]

    def validate_file(self, value):
        """
        Valida o tipo de arquivo do video.
        Aceita apenas arquivos de mp4.
        """
        if value.content_type not in ['video/mp4']:
            raise serializers.ValidationError("Only MP4 videos are allowed.")
        return value
