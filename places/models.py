from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    name = models.CharField('Название локации', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Подробное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='imgs'
    )
    img = models.ImageField(verbose_name='Картинка')
    position = models.PositiveIntegerField(
        'Позиция',
        default=0
    )

    def __str__(self):
        return f'{self.position} {self.place.name}'

    class Meta:
        ordering = ['position']
