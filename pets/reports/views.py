__author__ = 'fredericomatos'

import requests
from django.conf import settings
from django.shortcuts import render_to_response


def report_pets_by_tags(request):
    url = 'https://api.instagram.com/v1/tags/bichosdeestimacao/media/recent'
    params = {'access_token': settings.ACCESS_TOKEN}
    content = requests.get(url, params=params).json()
    data = content['data']
    dogs_tag = ['doggy', 'dogs', 'cachorro', 'dog']
    cats_tag = ['cats', 'gatos', 'cat', 'gato']
    total_dogs = 0
    total_cats = 0

    for user in data:
        for tag in dogs_tag:
            if tag in user['tags']:
                total_dogs += 1
                break
        for tag in cats_tag:
            if tag in user['tags']:
                total_cats += 1
                break
    context = {}
    context['total_dogs'] = total_dogs
    context['total_cats'] = total_cats

    return render_to_response('report_pets_by_tags.html', context)