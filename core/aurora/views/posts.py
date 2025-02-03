from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from core.aurora.models import Posts, PostImage
from core.uploader.models import Image
from core.uploader.helpers import create_image  
from core.aurora.serializers import PostsListSerializer, PostsCreateSerializer, PostImagesSerializer


class PostsViewSet(ModelViewSet):
    queryset = Posts.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PostsCreateSerializer
        return PostsListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data
        images_files = validated_data.pop("images", [])  

        post = Posts.objects.create(**validated_data)

        for image_file in images_files:
            try:
                image_instance = create_image(file=image_file, folder_path="media/posts")
                PostImage.objects.create(post=post, image=image_instance)
            except Exception as e:
                return Response(
                    {"error": f"Erro ao processar a imagem '{image_file.name}': {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        response_serializer = PostsListSerializer(post)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class PostImageViewSet(ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImagesSerializer