from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import NewmodViewSet

router = DefaultRouter()
router.register("newmod", NewmodViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
