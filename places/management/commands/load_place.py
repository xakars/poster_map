import requests
from django.core.management.base import BaseCommand
from places.models import Place, Image
from django.core.files.base import ContentFile


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()
        place_detail = response.json()
        try:
            place = Place.objects.get(title=place_detail['title'])
        except Place.DoesNotExist:
            place = Place(
                title=place_detail['title'],
                description_short = place_detail['description_short'],
                description_long = place_detail['description_long'],
                lng = place_detail['coordinates']['lng'],
                lat = place_detail['coordinates']['lat']
            )
            place.save()
            img_urls = place_detail['imgs']
            for index, url in enumerate(img_urls):
                img = Image(name=Place.objects.get(title=place_detail['title']))
                img_response = requests.get(url)
                response.raise_for_status()
                content = ContentFile(img_response.content)
                img.img.save(str(index), content, save=True)