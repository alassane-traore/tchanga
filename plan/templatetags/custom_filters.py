# custom_filters.py

from django import template
from django.template.defaultfilters import stringfilter
import time


register = template.Library()


@register.filter
def pmx(x):
    x=str(x)
    if "p.m." in x:
        
        am=x.split("p.m.")[0].split(":")[0]
        am1=int(am)+12
        x=x.replace(am,am1)
        x=x.split("p.m.")[0]
    return x





