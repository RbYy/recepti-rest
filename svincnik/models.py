from django.db import models
from django.contrib.auth.models import User


KATEGORIJE = (
    (1, 'glavna'),
    (2, 'sladica'),
    (3, 'predjed')
)


class Jed(models.Model):
    ime = models.CharField(max_length=30)
    recept = models.TextField()
    poreklo = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name='jedi')
    kategorija = models.CharField(choices=KATEGORIJE,
                                  max_length=30)
    dodano = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ime


class Komentar(models.Model):
    vsebina = models.TextField()
    jed = models.ForeignKey(Jed, related_name='komentarji')
    user = models.ForeignKey(User, related_name='komentarji')
    objavljeno = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Komentarji"
        ordering = ['objavljeno']

    def __str__(self):
        return "{0} - {1} - {2}".format(self.objavljeno, self.vsebina, self.user.username)
