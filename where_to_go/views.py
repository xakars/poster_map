from django.shortcuts import render
from places.models import Place


def serialize_place(place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
        },
        "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": place.detailsUrl
        }
    }



def index(request):
    places = Place.objects.all()
    geo = {
        "type": "FeatureCollection",
        "features": [serialize_place(place) for place in places]
    }

    context = {
        "places": geo
    }
    return render(request, 'index.html', context)