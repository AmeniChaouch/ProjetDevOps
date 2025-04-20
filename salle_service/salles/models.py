from django.db import models
# models.py
class Salle(models.Model):
    nom = models.CharField(max_length=100)
    capacité = models.IntegerField()

    def __str__(self):
        return self.nom


class Disponibilite(models.Model):
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.salle.nom} - {self.date_debut} to {self.date_fin}'
