from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the oracle index.")

def lookup(request, item_id):
    api_url = "http://prices.runescape.wiki/api/v1/osrs/timeseries/id=%s/timestamp=1h" % item_id
    header = {
        'User-Agent': 'Price Watcher Project - @Brian#6233'
    }
    res = requests.get(api_url, headers=header)
    return HttpResponse(res.json())

def lookupSearch(request):
    return HttpResponse("default lookup index")