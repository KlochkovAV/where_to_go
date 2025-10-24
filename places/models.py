from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=256)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Полное описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(
        'Картинка'
    )
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name='images'
    )

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.place.title