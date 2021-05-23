from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from decimal import Decimal


class TextForm(forms.Form):
    czcionka = forms.ChoiceField(choices=[('Times New Roman', 'Times New Roman'), (
        'Arial', 'Arial'), ('Courier New', 'Courier New'), ('Verdana', 'Verdana')])
    rozmiar = forms.IntegerField(initial=25)
    kolor = forms.ChoiceField(
        choices=[('red', 'Czerwony'), ('black', 'Czarny'), ('orange', 'Pomarańczowy'), ('green', 'Zielony')])
    tekst = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'czcionka',
            'rozmiar',
            'kolor',
            'tekst',
            Submit('submit', 'Dodaj', css_class="btn btn-success")
        )


class ChartForm(forms.Form):
    typ = forms.ChoiceField(
        choices=[('bar', 'Słupkowy'), ('line', 'Liniowy'), ('pie', 'Kołowy')])
    os_x = forms.CharField()
    os_y = forms.CharField()
    kolor = forms.ChoiceField(
        choices=[('red', 'Czerwony'), ('black', 'Czarny'), ('orange', 'Pomarańczowy'), ('green', 'Zielony')])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'typ',
            'os_x',
            'os_y',
            'kolor',
            Submit('submit', 'Dodaj', css_class="btn btn-success mt-2")
        )


class TableForm(forms.Form):
    model = forms.ChoiceField(choices=[('client', 'Klient'), (
        'product', 'Produkt')])
    typ = forms.ChoiceField(
        choices=[('table', 'podstawowy'), ('table table-dark', 'ciemny'), ('table table-striped', 'pasiasty'), ('table table-bordered', 'obramowany')])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'model',
            'typ',
            Submit('submit', 'Dodaj', css_class="btn btn-success mt-3")
        )
