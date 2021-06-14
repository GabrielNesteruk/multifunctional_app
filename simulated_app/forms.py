from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from decimal import Decimal


class TextForm(forms.Form):
    czcionka = forms.ChoiceField(choices=[('Times New Roman', 'Times New Roman'), (
        'Arial', 'Arial'), ('Courier New', 'Courier New'), ('Verdana', 'Verdana')])
    wysrodkowanie = forms.ChoiceField(
        choices=[('text-start', 'do lewej'), ('text-center', 'środek'), ('text-end', 'do prawej')])
    rozmiar = forms.IntegerField(initial=25)
    kolor = forms.ChoiceField(
        choices=[('black', 'Czarny'), ('red', 'Czerwony'), ('orange', 'Pomarańczowy'), ('green', 'Zielony')])
    tekst = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('czcionka', css_class="form-select m-2"),
            Field('wysrodkowanie', css_class="form-select m-2"),
            Field('rozmiar', css_class="form-select m-2"),
            Field('kolor', css_class="form-select m-2"),
            Field('tekst', css_class="form-control m-2"),
            Submit('submit', 'Dodaj', css_class="btn btn-success m-2")
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
            Field('model', css_class="form-select m-2"),
            Field('typ', css_class="form-select m-2"),
            Submit('submit', 'Dodaj', css_class="btn btn-success m-2")
        )
