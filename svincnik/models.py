from django.db import models
from django.contrib.auth.models import User


VRSTE_JEDI = (
    ('glavna', 'glavna'),
    ('sladica', 'sladica'),
    ('predjed', 'predjed')
)


class Jed(models.Model):
    ime = models.CharField(max_length=30)
    recept = models.TextField()
    poreklo = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name='jedi')
    vrsta = models.CharField(choices=VRSTE_JEDI, max_length=30)

