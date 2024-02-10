from django.db import models

class CalculatedResult(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    result = models.FloatField()