from rest_framework import serializers
from core.uploader.models import Image, Document

class ImageUploadSerializer(serializers.ModelSerializer):
    file = serializers.ImageField(required=True)
    description = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = Image
        fields = ["id", "file", "description", "uploaded_on"]

    def validate_file(self, value):
        """
        Valida o tipo de arquivo da imagem.
        Aceita apenas arquivos de imagem.
        """
        if value.content_type not in ['image/jpeg', 'image/png']:
            raise serializers.ValidationError("Only JPEG and PNG images are allowed.")
        return value

class DocumentUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)
    description = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = Document
        fields = ["id", "file", "description", "uploaded_on"]

    def validate_file(self, value):
        """
        Valida o tipo de arquivo do documento.
        Aceita apenas arquivos PDF.
        """
        if value.content_type not in ['application/pdf']:
            raise serializers.ValidationError("Only PDFs documents are allowed.")
        return value