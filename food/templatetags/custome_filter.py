from pickle import PERSID

from django import template

register = template.Library()


@register.filter
def currency(value):
    return f"${value}"


@register.filter
def discount(value, percentage):
    return int(value) - (int(value) * (int(percentage) / 100))
