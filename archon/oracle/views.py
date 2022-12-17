from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the oracle index.")

def lookup(request, item_id):
    api_url = "http://prices.runescape.wiki/api/v1/osrs/timeseries?id=52&timestep=1h"
    header = {
        'User-Agent': 'Price Watcher Project - @Brian#6233'
    }
    res = requests.get(api_url, headers=header)
    data = res.json()
    fields = dict()
    print(res.json())
    for object in data["data"]:

        fields[object['timestamp']] = object['avgHighPrice']
    context = {
            'fields': fields,
    }
    return render(request, 'oracle/index.html', context)

def lookupSearch(request):
    return HttpResponse("default lookup index")