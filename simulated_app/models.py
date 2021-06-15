from django.core.validators import ip_address_validator_map
from django.db import models
from django.utils.timezone import now

# Create your models here.


class Text(models.Model):
    font = models.CharField(max_length=25, choices=[('Times New Roman', 'Times New Roman'), (
        'Arial', 'Arial'), ('Courier New', 'Courier New'), ('Verdana', 'Verdana')], default='Times New Roman')
    align = models.CharField(max_length=25,
                             choices=[('text-start', 'Do lewej'), ('text-center', 'Środek'), ('text-end', 'Do prawej')], default='text-start')
    font_size = models.IntegerField(default=25)
    font_color = models.CharField(max_length=20, choices=[('red', 'Czerwony'), (
        'black', 'Czarny'), ('orange', 'Pomarańczowy'), ('green', 'Zielony')], default='black')
    content = models.TextField()
    date_created = models.DateTimeField(default=now, editable=False)
    data_type = models.CharField(max_length=5, default='text', editable=False)

    def __str__(self):
        return 'Tekst nr. ' + str(self.pk)

# dodawanie danych do bazy (model do bazy)


class Chart(models.Model):
    data_name = models.CharField(max_length=40, unique=True, error_messages={
                                 'unique': "Zarejstrowano taka nazwe"}, default="tekst")
    data_value = models.FloatField(max_length=10, default=0)
    date_created = models.DateTimeField(default=now, editable=False)


class Client(models.Model):
    name = models.CharField(max_length=25)
    surrname = models.CharField(max_length=25)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=25)


class Visibility(models.Model):
    model_name = models.CharField(max_length=15)
    data_type = models.CharField(max_length=20, default='table')
    date_created = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        if self.data_type == 'table':
            return str(self.model_name) + ' table nr.' + str(self.pk)
        else:
            return str(self.model_name) + ' nr.' + str(self.pk)
