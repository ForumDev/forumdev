from django import template

register = template.Library()

def widthcalc(value):
    return round(float(100/int(value)),5)

register.filter('widthcalc', widthcalc)