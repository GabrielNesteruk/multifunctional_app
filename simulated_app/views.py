import django
from django.shortcuts import render
from .forms import TextForm, ChartForm, TableForm
from .models import Text, Visibility, Client
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

    tables_to_show = Visibility.objects.all()
    for table in tables_to_show:
        if table.model_name == 'client':
            field_names = [f.name for f in Client._meta.get_fields()]
            data = [[getattr(ins, name) for name in field_names]
                    for ins in Client.objects.prefetch_related().all()]
            tmp_data = {
                'field_names': field_names,
                'data': data,
                'type': table.data_type,
                'date_created': table.date_created,
            }
            all_objects.append(tmp_data)
    all_objects.sort(key=sortFunc)

    context = {
        'data': all_objects
    }
    return render(request, 'pdf/home.html', context)


def text(request):
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
    form = TextForm()
    return render(request, 'pdf/forms.html', {'form': form})


def chart(request):
    if request.method == 'POST':
        form = ChartForm(request.POST)
        if form.is_valid():
            chart_type = form.cleaned_data['typ']
    form = ChartForm()
    return render(request, 'pdf/chart.html', {'form': form})


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
