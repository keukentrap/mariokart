from django.contrib import admin

from .models import Coureur,Race,Resultaat,Wedstrijdbaan,Bepaling

class ResultaatAdmin(admin.ModelAdmin):
    list_display = ['race', 'coureur', 'split1', 'split2','split3','split4','totaal']
    list_filter = ['coureur','race']

class WedstrijdbaanAdmin(admin.ModelAdmin):
    list_display = ['naam','locatie']

class RaceAdmin(admin.ModelAdmin):
    list_display = ['naam', 'wedstrijdbaan', 'promotie_code']

admin.site.register(Coureur)
admin.site.register(Wedstrijdbaan,WedstrijdbaanAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Resultaat,ResultaatAdmin)
admin.site.register(Bepaling)

# Register your models here.
