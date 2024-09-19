from django.db import models

class Entrepreneur(models.Model):
    nomEntrepreneure = models.CharField(max_length=100)
    prenomEntrepreneure = models.CharField(max_length=100)
    dateNaissanceEntrepreneure = models.DateField()
    secteurActivite = models.CharField(max_length=100)
    paysActivite = models.CharField(max_length=100)
    regionActivite = models.CharField(max_length=100)
    telephone = models.IntegerField()
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.prenomEntrepreneure} {self.nomEntrepreneure}"

