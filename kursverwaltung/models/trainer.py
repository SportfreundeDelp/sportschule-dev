from django.db import models
from .person import Person
from .zertifizierung import Zertifizierung

class Trainer(Person):
    # zusätziche Daten zu Personendaten
    bemerkung = models.CharField(max_length=32767)
    zertifizierung = models.ManyToManyField(Zertifizierung)
