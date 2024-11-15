from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet

router = DefaultRouter()
router.register(r'listings', ListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]