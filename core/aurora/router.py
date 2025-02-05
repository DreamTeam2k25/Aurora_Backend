from rest_framework.routers import DefaultRouter

from core.aurora.views import CommentsViewSet, PostsViewSet, PostImageViewSet

aurora_router = DefaultRouter()
aurora_router.register(r'comments', CommentsViewSet)
aurora_router.register(r'posts', PostsViewSet)
aurora_router.register(r'posts images', PostImageViewSet)
