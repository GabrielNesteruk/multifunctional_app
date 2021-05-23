from django.core.validators import ip_address_validator_map
from django.db import models

# Create your models here.


class Text(models.Model):
    font = models.CharField(max_length=25, choices=[('Times New Roman', 'Times New Roman'), (
        'Arial', 'Arial'), ('Courier New', 'Courier New'), ('Verdana', 'Verdana')], default='Times New Roman')
    font_size = models.IntegerField(default=25)
    font_color = models.CharField(max_length=20, choices=[('red', 'Czerwony'), (
        'black', 'Czarny'), ('orange', 'Pomarańczowy'), ('green', 'Zielony')], default='black')
    content = models.TextField()

    def __str__(self):
        return 'Tekst nr. ' + str(self.pk)


class Chart(models.Model):
    type = models.CharField(max_length=10, choices=[(
        'bar', 'Słupkowy'), ('line', 'Liniowy'), ('pie', 'Kołowy')], default='Liniowy')
    x_label = models.CharField(max_length=25, default='x')
    y_label = models.CharField(max_length=25, default='y')
    background_color = models.CharField(max_length=15, choices=[('red', 'Czerwony'), (
        'black', 'Czarny'), ('orange', 'Pomarańczowy'), ('green', 'Zielony'), ('transparent', 'Przezroczysty')], default='transparent')

    def __str__(self):
        return 'Wykres nr. ' + str(self.pk)


class Client(models.Model):
    name = models.CharField(max_length=25)
    surrname = models.CharField(max_length=25)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=25)


class Visibility(models.Model):
    model_name = models.CharField(max_length=15)
    table_type = models.CharField(max_length=20, default='table')
