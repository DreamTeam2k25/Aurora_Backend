from rest_framework import viewsets, status
from rest_framework.response import Response
from cloudinary.uploader import upload
from core.uploader.models import Video
import uuid
from core.uploader.serializers import VideoUploadSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoUploadSerializer
    
    def create(self, request, *args, **kwargs):
        """
        Sobrescreve o método de criação para fazer o upload do documento para o Cloudinary.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            description = serializer.validated_data.get('description', '')

            cloudinary_response = upload(file, folder='media/videos', resource_type='video')

            video = Video.objects.create(
                attachment_key=uuid.uuid4(),
                public_id=cloudinary_response['public_id'],
                file=cloudinary_response['url'],
                description=description
            )

            return Response({
                'id': video.id,
                'attachment_key': video.attachment_key,
                'public_id': video.public_id,
                'file': video.file,
                'description': video.description,
                'uploaded_on': video.uploaded_on
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            