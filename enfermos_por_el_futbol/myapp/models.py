from django.db import models


class Equipo(models.Model):
    bandera = models.ImageField(default="null")
    nombre = models.CharField(max_length=20)
    grupo = models.CharField(max_length=10)
    puntos = models.IntegerField(default=0)
    partidos_jugados = models.IntegerField(default=0)
    partidos_ganados = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)
    fuerza = models.IntegerField(default=0)
    resistencia = models.IntegerField(default=0)
    velocidad = models.IntegerField(default=0)
    precision = models.IntegerField(default=0)
