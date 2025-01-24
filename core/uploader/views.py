from rest_framework import viewsets, status
from rest_framework.response import Response
from cloudinary.uploader import upload
from .models import Image
import uuid
from .serializers import ImageUploadSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageUploadSerializer

    def create(self, request, *args, **kwargs):
        """
        Sobrescreve o método de criação para fazer o upload da imagem para o Cloudinary.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            description = serializer.validated_data.get('description', '')

            cloudinary_response = upload(file, folder='media/users')

            image = Image.objects.create(
                attachment_key=uuid.uuid4(),
                public_id=cloudinary_response['public_id'],
                file=cloudinary_response['secure_url'],
                description=description
            )

            return Response({
                'id': image.id,
                'attachment_key': image.attachment_key,
                'public_id': image.public_id,
                'file': image.file,
                'description': image.description,
                'uploaded_on': image.uploaded_on
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
