from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CustomTextViewSet, DevstringViewSet, HomePageViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("homepage", HomePageViewSet)
router.register("customtext", CustomTextViewSet)
router.register("devstring", DevstringViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
