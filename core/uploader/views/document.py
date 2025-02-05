from rest_framework import viewsets, status
from rest_framework.response import Response
from cloudinary.uploader import upload
from core.uploader.models import Document
import uuid
from core.uploader.serializers import DocumentUploadSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentUploadSerializer
    
    def create(self, request, *args, **kwargs):
        """
        Sobrescreve o método de criação para fazer o upload do documento para o Cloudinary.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            description = serializer.validated_data.get('description', '')

            cloudinary_response = upload(file, folder='media/documents', resource_type='raw')

            document = Document.objects.create(
                attachment_key=uuid.uuid4(),
                public_id=cloudinary_response['public_id'],
                file=cloudinary_response['url'],
                description=description
            )

            return Response({
                'id': document.id,
                'attachment_key': document.attachment_key,
                'public_id': document.public_id,
                'file': document.file,
                'description': document.description,
                'uploaded_on': document.uploaded_on
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            