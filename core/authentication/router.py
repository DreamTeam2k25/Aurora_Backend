from rest_framework.routers import DefaultRouter

from core.authentication.views import StudentViewSet, UserViewSetList, GuildMemberViewSet

authentication_router = DefaultRouter()
authentication_router.register(r'students', StudentViewSet)
authentication_router.register(r'users', UserViewSetList)
authentication_router.register(r'guild_members', GuildMemberViewSet)
