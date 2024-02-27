from django.db import models

class CalculatedResult(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    result = models.FloatField()

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    matricule = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"