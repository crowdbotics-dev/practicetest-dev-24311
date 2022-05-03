
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserdetailsViewSet
router = DefaultRouter()
router.register('userdetails', UserdetailsViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
