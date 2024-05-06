from django import template
from myapp.models import Equipo

register = template.Library()


@register.inclusion_tag("tables/group_a.html")
def table_group_a():
    equipos = Equipo.objects.all()
    return {"equipos": equipos}


@register.inclusion_tag("tables/group_b.html")
def table_group_b():
    equipos = Equipo.objects.all()
    return {"equipos": equipos}


@register.inclusion_tag("tables/group_c.html")
def table_group_c():
    equipos = Equipo.objects.all()
    return {"equipos": equipos}


@register.inclusion_tag("tables/group_d.html")
def table_group_d():
    equipos = Equipo.objects.all()
    return {"equipos": equipos}


@register.inclusion_tag("tables/group_e.html")
def table_group_e():
    equipos = Equipo.objects.all()
    return {"equipos": equipos}


@register.inclusion_tag("tables/group_f.html")
def table_group_f():
    equipos = Equipo.objects.all()
    return {"equipos": equipos}


@register.inclusion_tag("tables/group_g.html")
def table_group_g():
    equipos = Equipo.objects.all()
    return {"equipos": equipos}


@register.inclusion_tag("tables/group_h.html")
def table_group_h():
    equipos = Equipo.objects.all()
    return {"equipos": equipos}
