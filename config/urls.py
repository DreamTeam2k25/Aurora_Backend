from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from core.authentication.utils import UpdateMemberDataView

from core.authentication.views import CustomTokenObtainPairView, StudentViewSet, UserViewSetList

from core.uploader.views import ImageViewSet

from core.aurora.views import PostsViewSet, PostImageViewSet

router = DefaultRouter()

router.register(r'students', StudentViewSet)
router.register(r'users', UserViewSetList)
router.register(r'images', ImageViewSet)
router.register(r'posts', PostsViewSet)
router.register(r'post-images', PostImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/students/<int:student_id>/<int:office_id>/', UpdateMemberDataView.as_view(), name='update_member_guild_data'),
    path('', lambda request: redirect('api/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
