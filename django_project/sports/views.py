from django.shortcuts import render
from django.http import HttpResponse
from . import rugby_getter, cricket_getter, supercars_getter, cricket_top_stories_getter, rugby_top_stories_getter, supercars_top_stories_getter, sailing_getter, sailing_news, indy_getter
def home(request):
    return render(request, 'sports/homepage.html')

def rugby(request):
    rugby_dict = [rugby_getter.main()]
    story_dict = [rugby_top_stories_getter.main()]
    context = {
        "rugby": rugby_dict,
        "story": story_dict
    }
    return render(request, 'sports/rugby.html', context = context)

def cricket(request):
    cricket_dict = [cricket_getter.main()]
    story_dict = [cricket_top_stories_getter.main()]
    context = {
        "cricket": cricket_dict,
        "story": story_dict
    }
    return render(request, 'sports/cricket.html', context = context)

def supercars(request):
    cars_dict = [supercars_getter.main()]
    story_dict = [supercars_top_stories_getter.main()]
    context = {
        "cars": cars_dict,
        "story": story_dict
    }
    return render(request, 'sports/supercars.html', context)

def sailing(request):
    sailing_dict = [sailing_getter.main()]
    story_dict = [sailing_news.main()]
    context = {
        "sailing": sailing_dict,
        "story": story_dict


    }
    return render(request, 'sports/sailing.html', context)

def indycar(request):
    indy_dict = [indy_getter.main()]
    context = {
        "cars": indy_dict
    }
    return render(request, 'sports/indycars.html', context)

def watchJSON(request):
    fileobject = open("./watchjson.json", 'r').readlines()[0]
    return HttpResponse(fileobject, content_type='application/json')
