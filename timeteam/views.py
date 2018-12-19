from django.shortcuts import render

from .models import Race,Coureur,Resultaat,Bepaling

class Plek:
    coureur = None
    resultaat = None
    score = None

# Create your views here.
def loting(request):
    races = Race.objects.all()
    context = {'races': races}
    return render(request, 'timeteam/loting.html',context)

def resultaten(request):
    races = Race.objects.all()
    for race in races:
        race.resultaten = Resultaat.objects.filter(race=race)
        race.plekken = []
        for coureur in race.deelnemers.all() :
            plek = Plek()
            plek.coureur = coureur
            try:
                resultaat = race.resultaten.filter(coureur=coureur).get()
            except resultaat.DoesNotExist as e:
                continue
            plek.resultaat = resultaat
            plek.score = resultaat.totaal()
            race.plekken += [plek]
        race.plekken = sorted(race.plekken, key=lambda plek:plek.score, reverse=True)

    context = {'races': races}
    return render(request, 'timeteam/resultaten.html',context)

def index(request):
    bepalingen = Bepaling.objects.all()
    context = {'bepalingen': bepalingen}
    return render(request, 'index.html', context)
