from django.shortcuts import render, HttpResponse, redirect
from myapp.models import Equipo


def index(request):
    return render(request, "index.html")


def grupo_a(request):
    equipos = Equipo.objects.order_by("-puntos")
    return render(request, "./tables/group_a.html", {"equipos": equipos})


def tabla_de_posiciones(request):
    equipos = Equipo.objects.order_by("-puntos")
    return render(request, "./tables/tabla_de_posiciones.html", {"equipos": equipos})


def llaves(request):
    return render(request, "llaves.html")


def equipos_grupo_a(request):
    return


# saving the information in the db
def guardar_equipo(request):

    if request.method == "POST":

        nombre = request.POST.get("nombre", False)
        resistencia = request.POST.get("resistencia", False)
        fuerza = request.POST.get("fuerza", False)
        velocidad = request.POST.get("velocidad", False)
        precision = request.POST.get("precision", False)
        grupo = request.POST.get("grupo", False)

        equipo = Equipo(
            bandera=None,
            nombre=nombre,
            grupo=grupo,
            puntos=0,
            partidos_jugados=0,
            partidos_ganados=0,
            partidos_empatados=0,
            partidos_perdidos=0,
            fuerza=fuerza,
            resistencia=resistencia,
            velocidad=velocidad,
            precision=precision,
        )

        equipo.save()

        return redirect("tablas-de-posiciones")

    else:

        return HttpResponse(f"no puedes ingresar, {equipo.nombre}:(")


# delete a team
def borrar_equipo(request, name):
    equipo = Equipo.objects.get(pk=name)
    equipo.delete()
    return redirect("./tables/tabla_de_posiciones.html")
