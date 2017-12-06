from django.shortcuts import render
from django.http import JsonResponse
from .models import Event
from django.db.models import QuerySet

# Create your views here.
def index(request):

    num = Event.objects.all().count()

    if num == 0:
        return JsonResponse({'Information': 'No Events'})

    events = Event.objects.all()

    response = dict()

    for event in events:
        eventdata = dict()
        eventdata['type'] = event.eventType
        eventdata['Created at'] = event.eventCreationTime

        response[event.id] = eventdata

    return JsonResponse(response)

def event(request, eventid):
    return JsonResponse({'Info': 'blank'})