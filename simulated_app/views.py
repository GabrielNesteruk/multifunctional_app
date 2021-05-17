from django.shortcuts import render
from .forms import TextForm, ChartForm
# Create your views here.


def home(request):
    # context do testowania wyswietlania napisow
    #
    context = {
        'text': "Tekst testujacy *pogrubienie* i **pochylenie** a na koncu ***skreslenie*** &nlTo powinno byc w nowej linii",
        'details': {
            'color': "red",
            'size': 30,
            'font': "Tahoma, sans-serif",
        }
    }
    return render(request, 'pdf/base.html', context)


def text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            populated_text = form.cleaned_data['tekst']
    form = TextForm()
    return render(request, 'pdf/forms.html', {'form': form})


def chart(request):
    if request.method == 'POST':
        form = ChartForm(request.POST)
        if form.is_valid():
            chart_type = form.cleaned_data['typ']
    form = ChartForm()
    return render(request, 'pdf/chart.html', {'form': form})
