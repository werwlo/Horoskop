from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd


def about(request):
    print('O astrologii')
    return render(request, 'about.html')

def contact(request):
    print('Kontakt')
    return render(request, 'contact.html')

def koziorozec(request):
    print('Koziorożec')
    return render(request, 'koziorozec.html')

def wodnik(request):
    print('Wodnik')
    return render(request, 'wodnik.html')

def ryby(request):
    print('Ryby')
    return render(request, 'ryby.html')

def baran(request):
    print('Baran')
    return render(request, 'baran.html')

def byk(request):
    print('Byk')
    return render(request, 'byk.html')

def bliznieta(request):
    print('Bliźnięta')
    return render(request, 'bliznieta.html')

def rak(request):
    print('Rak')
    return render(request, 'rak.html')

def lew(request):
    print('Lew')
    return render(request, 'lew.html')

def panna(request):
    print('Panna')
    return render(request, 'panna.html')

def waga(request):
    print('Waga')
    return render(request, 'waga.html')

def skorpion(request):
    print('Skorpion')
    return render(request, 'skorpion.html')

def strzelec(request):
    print('Strzelec')
    return render(request, 'strzelec.html')

def koziorozec(request):
    print('Koziorożec')
    return render(request, 'koziorozec.html')






def home(request):
    print('Data analysis')
    if request.method == 'POST':

        zodiac = request.POST.get('url')

        print(zodiac)

        return render(request, 'horoskopmain.html', {'zodiac': zodiac})


        # return render(request, 'data_analysis.html',
        #               {'result_present': True,
        #                'results': {'r_table': r_table.to_html(),
        #                            'p_table': p_table.to_html()},
        #                'df': df.to_html()})

    return render(request, 'home.html')
