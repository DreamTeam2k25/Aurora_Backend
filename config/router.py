from rest_framework.routers import DefaultRouter

from core.aurora.router import aurora_router
from core.authentication.router import authentication_router
from core.uploader.router import uploader_router

router = DefaultRouter()
router.registry.extend(aurora_router.registry)
router.registry.extend(authentication_router.registry)
router.registry.extend(uploader_router.registry)

