from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import PlaceSerializer
from places.models import Place


class PlaceViewSet(ReadOnlyModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()