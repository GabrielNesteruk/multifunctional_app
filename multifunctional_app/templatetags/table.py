from django.db.models.base import Model
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django import template
from django.db import models
# from project.apps.blog.models
from simulated_app.models import Client


register = template.Library()


def showTable(field_names, data, table_type):
    return {'field_names': field_names, 'data': data, 'table_type': table_type}


table_template = get_template('table_creator.html')
register.inclusion_tag(table_template)(showTable)
