from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название локации', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Подробное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.ForeignKey('Place', on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='Картинка')
    position = models.PositiveIntegerField(
        'Позиция',
        default=0,
        blank=False,
        null=False
    )

    def __str__(self):
        return f'{self.position} {self.name.title}'

    class Meta:
        ordering = ['position']