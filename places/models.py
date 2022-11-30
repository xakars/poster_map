from django.db import models


class Place(models.Model):
    title = models.CharField("Название локации", max_length=200)
    description_short = models.CharField("Краткое описание", max_length=600, blank=True)
    description_long = models.TextField("Подробное описание", blank=True)
    lat = models.FloatField('Широта', blank=True)
    lon = models.FloatField('Долгота', blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        verbose_name='Фото локации',
        related_name='imgs'
    )
    img = models.ImageField()

    def __str__(self):
        return f'{self.id} {self.name.title}'
