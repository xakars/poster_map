import requests
from django.core.management.base import BaseCommand
from places.models import Place, Image
from django.core.files.base import ContentFile


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        try:
            url = options['url']
            response = requests.get(url)
            response.raise_for_status()
            place_detail = response.json()

            place, created = Place.objects.get_or_create(
                title=place_detail['title'],
                lng=place_detail['coordinates']['lng'],
                lat=place_detail['coordinates']['lat'],
                defaults= {
                    'description_short': place_detail.get('description_short', ''),
                    'description_long': place_detail.get('description_long', '')
                }
            )
            if not created:
                place.imgs.all().delete()

            img_urls = place_detail.get('imgs', [])
            for index, url in enumerate(img_urls):
                img_response = requests.get(url)
                response.raise_for_status()
                content = ContentFile(img_response.content, name=f'{str(index)}.jpg')
                Image.objects.create(place=place, img=content, position=index)

        except KeyError as e:
               print(f'В json-е локации не найдено значение {e}')