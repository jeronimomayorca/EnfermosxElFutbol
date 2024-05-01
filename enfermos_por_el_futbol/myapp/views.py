from django.shortcuts import render, HttpResponse
from myapp.models import Equipo


def index(request):
    return render(request, "index.html")


def table_group_a(request):
    return render(request, "group_a.html")


def tabla_de_posiciones(request):

    equipos = Equipo.objects.all()

    return render(request, "./tables/tabla_de_posiciones.html", {"equipos": equipos})


def llaves(request):
    return render(request, "llaves.html")


# saving the information in the db
def guardar_equipo(request):

    equipo = Equipo(
        bandera=None,
        nombre="Bolivia",
        grupo="A",
        puntos=0,
        partidos_jugados=0,
        partidos_ganados=0,
        partidos_empatados=0,
        partidos_perdidos=0,
        fuerza=10,
        resistencia=10,
        velocidad=10,
        precision=10,
    )

    equipo.save()

    return HttpResponse(f"Bienvenido al torneo, {equipo.nombre}!")
