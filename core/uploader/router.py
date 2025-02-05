from rest_framework.routers import DefaultRouter

from core.uploader.views import DocumentViewSet, ImageViewSet, VideoViewSet

uploader_router = DefaultRouter()
uploader_router.register(r'documents', DocumentViewSet)
uploader_router.register(r'images', ImageViewSet)
uploader_router.register(r'videos', VideoViewSet)
