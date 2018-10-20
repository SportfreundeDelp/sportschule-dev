from django.db import models
from .person import Person
from .zertifizierung import Zertifizierung

class Trainer(Person):
    # zusätziche Daten zu Personendaten
    bemerkung = CharField(max_length=32767)
    zertifizierung = models.ForeignKey(Zertifizierung, on_delete=models.SET_NULL)
