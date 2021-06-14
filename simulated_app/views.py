import django
from django.shortcuts import render
from .forms import TextForm, TableForm
from .models import Chart, Text, Visibility, Client
from django.core import serializers
# Create your views here.


def sortFunc(e):
    return e['date_created']


def home(request):
    all_objects = []
    texts_to_show = Text.objects.all()
    for text in texts_to_show:
        tmp_data = {
            'font': text.font,
            'align': text.align,
            'font_size': text.font_size,
            'font_color': text.font_color,
            'content': text.content,
            'date_created': text.date_created,
            'type': text.data_type,
        }
        all_objects.append(tmp_data)

    visibility_objects_to_show = Visibility.objects.all()
    for item in visibility_objects_to_show:
        if item.model_name == 'client':
            field_names = [f.name for f in Client._meta.get_fields()]
            data = [[getattr(ins, name) for name in field_names]
                    for ins in Client.objects.prefetch_related().all()]
            tmp_data = {
                'field_names': field_names,
                'data': data,
                'type': item.data_type,
                'date_created': item.date_created,
                'category': 'table',
            }
        elif item.model_name == 'chart':
            chart_list = Chart.objects.all()
            data = serializers.serialize('json', chart_list)
            tmp_data = {
                'category': 'chart',
                'id': item.id,
                'type': item.data_type,
                'data': data,
                'date_created': item.date_created,
            }
        all_objects.append(tmp_data)

    all_objects.sort(key=sortFunc)

    context = {
        'data': all_objects
    }
    return render(request, 'pdf/home.html', context)


def text(request):
    successful_operation = False
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['tekst']
            color = form.cleaned_data['kolor']
            size = form.cleaned_data['rozmiar']
            font = form.cleaned_data['czcionka']
            align = form.cleaned_data['wysrodkowanie']
            new_text = Text(content=content, align=align, font_color=color,
                            font_size=size, font=font)
            new_text.save()
            successful_operation = True
    form = TextForm()
    return render(request, 'pdf/forms.html', {'form': form, 'added': successful_operation})


def chart(request):
    if request.method == 'POST':
        if 'add_to_database' in request.POST:
            nazwa = request.POST["nazwa_danych"]
            procenty = request.POST["procent_danych"]
            wykres = Chart(data_name=nazwa, data_value=procenty)
            wykres.save()
        elif 'add_chart' in request.POST:
            chart_type = request.POST["types"]
            new_chart = Visibility(model_name="chart", data_type=chart_type)
            new_chart.save()

    chart_list = Chart.objects.all()

    return render(request, 'pdf/chart.html',
                  {'chart_list': chart_list})


def table(request):
    successful_operation = False
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            model = form.cleaned_data['model']
            table_type = form.cleaned_data['typ']
            new_table = Visibility(model_name=model, data_type=table_type)
            new_table.save()
            successful_operation = True
    form = TableForm()
    return render(request, 'pdf/table.html', {'form': form, 'added': successful_operation})
