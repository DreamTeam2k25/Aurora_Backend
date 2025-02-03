from core.aurora.models import Posts, PostImage
from rest_framework import serializers

class PostImagesSerializer(serializers.ModelSerializer):
    """
    Serializer para as imagens relacionadas ao post.
    """
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = PostImage
        fields = ["id", "image_url", "post"]

    def get_image_url(self, obj):
        """
        Retorna a URL completa da imagem.
        """
        if obj.image.file:
            return obj.image.file.url
        return None


class PostsListSerializer(serializers.ModelSerializer):
    """
    Serializer de listagem de Posts, incluindo as imagens relacionadas.
    """
    images = PostImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Posts
        fields = ["id", "title", "content", "created_at", "images"]

class PostsCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, required=True)
    content = serializers.CharField(required=True)
    images = serializers.ListField(
        child=serializers.FileField(),  
        write_only=True,  
        required=False  
    )

    class Meta:
        model = Posts
        fields = ["id", "title", "content", "images"]

    def validate_images(self, value):
        """
        Valida se cada arquivo é uma imagem válida.
        """
        for image in value:
            if image.content_type not in ["image/jpeg", "image/png"]:
                raise serializers.ValidationError(f"Formato de imagem inválido: {image.content_type}. Use JPEG ou PNG.")
        return value