from rest_framework import serializers

from places.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description_short = serializers.CharField()
    description_long = serializers.CharField()
    imgs = serializers.SerializerMethodField()
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = (
            'title', 'imgs', 'description_short', 'description_long',
            'coordinates'
        )

    def get_coordinates(self, obj):
        coordinates = {
            'lng': obj.lng,
            'lat': obj.lat
        }
        return coordinates

    def get_imgs(self, obj):
        request = self.context.get('request')
        return [
            request.build_absolute_uri(
                img.image.url
            ) for img in obj.images.all()
        ]
