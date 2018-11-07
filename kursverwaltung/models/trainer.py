from django.db import models
from .person import Person
#from .zertifizierung import Zertifizierung

"""
    Trainer

    Abbildung von Trainer eines Kurses
"""
class Trainer(Person):

    class Meta:
        pass

    # zusätziche Daten zu Personendaten
    bemerkung = models.CharField(max_length=32767)
    #zertifizierung = models.ManyToManyField(Zertifizierung)
    geb_datum = models.DateField(verbose_name="Geburtstag")

    def __str__(self):
        return (self.vorname+" " +self.nachname )
