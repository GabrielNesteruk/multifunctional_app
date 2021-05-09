from django.shortcuts import render

# Create your views here.


def home(request):
    # context do testowania wyswietlania napisow
    #
    # context = {
    #     'text': "Tekst testujacy *pogrubienie* i **pochylenie** a na koncu ***skreslenie*** &nlTo powinno byc w nowej linii",
    #     'details': {
    #         'color': "red",
    #         'size': 30,
    #         'font': "Tahoma, sans-serif",
    #     }
    # }
    return render(request, 'pdf/base.html')
