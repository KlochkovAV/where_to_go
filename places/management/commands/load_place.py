
import requests
from django.core.management import BaseCommand, CommandError
from django.core.files.base import ContentFile

from places.models import Place, Image


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            type=str
        )

    def handle(self, *args, **options):
        url = options['url']
        try:
            response = requests.get(url)
            data = response.json()
            place = Place.objects.create(
                title=data['title'],
                description_short=data['description_short'],
                description_long=data['description_long'],
                lng=data['coordinates']['lng'],
                lat=data['coordinates']['lat']
            )
            for img_url in data['imgs']:
                img_response = requests.get(img_url)
                image_obj = Image(place=place)
                image_obj.image.save(
                    img_url.split('/')[-1],
                    ContentFile(img_response.content),
                    save=True
                )
        except Exception as e:
            raise CommandError(f'ошибка {e}')
