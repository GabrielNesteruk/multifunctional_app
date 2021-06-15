from django.contrib import admin
from .models import Text, Chart, Client, Visibility

# Register your models here.

admin.site.register(Text)
admin.site.register(Chart)
admin.site.register(Client)
admin.site.register(Visibility)