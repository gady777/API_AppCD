from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntrepreneurViewSet

router = DefaultRouter()
router.register(r'entrepreneurs', EntrepreneurViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
