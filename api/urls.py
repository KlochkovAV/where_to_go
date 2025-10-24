from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PlaceViewSet

router = SimpleRouter()
router.register('places', PlaceViewSet, basename='places')

urlpatterns = [
    path('', include(router.urls)),

]
