from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django import template


register = template.Library()


def showChart(id, type, qs_json, width, height):
    data = {
        'id': id,
        'type': type,
        'qs_json': qs_json,
        'width': width,
        'height': height,
    }
    return data


paragraph_template = get_template('chart.html')
register.inclusion_tag(paragraph_template)(showChart)
