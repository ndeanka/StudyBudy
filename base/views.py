from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


# Create your views here.

# products = [
#     {'id': 1, 'language': 'Python'},
#     {'id': 2, 'language': 'JavaScript'},
#     {'id': 3, 'language': 'Java'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'home.html', context)


def room(request, pk):
    rooms = Room.objects.get(id=pk)
    context = {'rooms': rooms}
    return render(request, 'room.html', context)
