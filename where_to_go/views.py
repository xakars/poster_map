from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from places.models import Place


def serialize_place(place):
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [place.lng, place.lat]
        },
        'properties': {
            'title': place.name,
            'placeId': place.id,
            'detailsUrl': reverse('detail', args=[place.id])
        }
    }


def index(request):
    places = Place.objects.all()
    geo = {
        'type': 'FeatureCollection',
        'features': [serialize_place(place) for place in places]
    }

    context = {
        'places': geo
    }
    return render(request, 'index.html', context)


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_detail = {
        'title': place.name,
        'imgs': [img.img.url for img in place.imgs.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lng,
            'lng': place.lat
        }
    }
    return JsonResponse(place_detail, json_dumps_params={'ensure_ascii': False})
