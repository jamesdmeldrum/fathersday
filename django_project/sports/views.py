from django.shortcuts import render
from django.http import HttpResponse
from . import rugby_getter, cricket_getter

def home(request):
    return render(request, 'sports/homepage.html')

def rugby(request):
    rugby_dict = [rugby_getter.main()]
    context = {
        "rugby": rugby_dict
    }
    print(rugby_dict)
    return render(request, 'sports/rugby.html', context = context)

def cricket(request):
    cricket_dict = [cricket_getter.main()]
    context = {
        "cricket": cricket_dict
    }
    return render(request, 'sports/cricket.html', context = context)
