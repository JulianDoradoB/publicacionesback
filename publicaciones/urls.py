from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PublicacionViewSet

router = DefaultRouter()
router.register(r'', PublicacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

