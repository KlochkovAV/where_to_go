import json
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.urls import reverse

from places.models import Place


def index_view(request):
    template = "index.html"
    objects = Place.objects.all()
    features = []
    for object in objects:
        url = reverse('places-detail', kwargs={'pk': object.id})
        place = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [object.lng, object.lat]
            },
            "properties": {
                "title": object.title,
                "placeId": object.id,
                "detailsUrl": url   
            }
        }
        features.append(place)
    data = {
        "type": "FeatureCollection",
        "features": features
    }
    context = {
        'places': mark_safe(json.dumps(data, ensure_ascii=False))
    }
    return render(request, template, context)
