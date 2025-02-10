from rest_framework.routers import DefaultRouter

from core.aurora.views import CommentsViewSet, PostsViewSet, PostImageViewSet, ReactionsViewSet, RepliesViewSet, ReplieOfReplieViewSet

aurora_router = DefaultRouter()
aurora_router.register(r'comments', CommentsViewSet)
aurora_router.register(r'posts', PostsViewSet)
aurora_router.register(r'posts images', PostImageViewSet)
aurora_router.register(r'replies', RepliesViewSet)
aurora_router.register(r'reactions', ReactionsViewSet)
aurora_router.register(r'replies_of_replies', ReplieOfReplieViewSet)
