from django import template

register = template.Library()


@register.inclusion_tag("../templates/navbar.html")
def navbar():
    pass


@register.inclusion_tag("tables/group_a.html")
def table_group_a():
    equipos = Equipo.objects.order_by("-puntos")
    return {"equipos": equipos}
