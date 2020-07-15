from django.shortcuts import render, HttpResponse, redirect
from .models import Show

# Create your views here.
def index(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    