from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Coureur(models.Model):
    def number():
        no = Coureur.objects.count()
        if no == None:
            return 1
        else:
            return no + 1
    
    
    naam = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    rugnummer = models.IntegerField(unique=True,default=number)

    def __str__(self):
        return self.naam
    
    class Meta:
        ordering = ['rugnummer']

class Bepaling(models.Model):
    regel = models.TextField()

    def __str__(self):
        return regel

class Wedstrijdbaan(models.Model):
    naam = models.CharField(max_length=200)
    locatie = models.CharField(max_length=200)

    def __str__(self):
        return self.naam

class Race(models.Model):
    naam = models.CharField(max_length=200)
    wedstrijdbaan = models.ForeignKey(Wedstrijdbaan, on_delete=models.CASCADE, null=True, blank=True)
    promotie_code = models.CharField(blank=True,max_length=200)
    deelnemers = models.ManyToManyField(Coureur,blank=True)
    volgorde = models.IntegerField(default=10)

    def __str__(self):
        return self.naam

    class Meta:
        ordering = ['volgorde']

class Resultaat(models.Model):
    coureur = models.ForeignKey(Coureur, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    split1 = models.IntegerField(blank=True, null=True)
    split2 = models.IntegerField(blank=True, null=True)
    split3 = models.IntegerField(blank=True, null=True)
    split4 = models.IntegerField(blank=True, null=True)
	
    def totaal(self):
       if not self.split1:
           return -1
       if not self.split2:
           return self.split1
       if not self.split3:
           return self.split1 + self.split2
       if not self.split4:
           return self.split1 + self.split2 + self.split3
       return self.split1 + self.split2 + self.split3 + self.split4

@receiver(post_save, sender=Race)
def save_resultaten(sender, instance, **kwargs):
    for coureur in instance.deelnemers.all():
        Resultaat.objects.get_or_create(
            coureur=coureur,
            race=instance
        )
