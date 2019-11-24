from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd
import random


def about(request):
    print('O astrologii')
    return render(request, 'about.html')

def authors(request):
    print('Autorzy')
    return render(request, 'authors.html')

def koziorozec(request):
    print('Koziorożec')
    return render(request, 'koziorozec.html',{'tekst':horoskop()})

def wodnik(request):
    print('Wodnik')
    return render(request, 'wodnik.html',{'tekst':horoskop()})

def ryby(request):
    print('Ryby')
    return render(request, 'ryby.html',{'tekst':horoskop()})

def baran(request):
    print('Baran')
    return render(request, 'baran.html',{'tekst':horoskop()})

def byk(request):
    print('Byk')
    return render(request, 'byk.html',{'tekst':horoskop()})

def bliznieta(request):
    print('Bliźnięta')
    return render(request, 'bliznieta.html',{'tekst':horoskop()})

def rak(request):
    print('Rak')
    return render(request, 'rak.html',{'tekst':horoskop()})

def lew(request):
    print('Lew')
    return render(request, 'lew.html',{'tekst':horoskop()})

def panna(request):
    print('Panna')
    return render(request, 'panna.html',{'tekst':horoskop()})

def waga(request):
    print('Waga')
    return render(request, 'waga.html',{'tekst':horoskop()})

def skorpion(request):
    print('Skorpion')
    return render(request, 'skorpion.html',{'tekst':horoskop()})

def strzelec(request):
    print('Strzelec')
    return render(request, 'strzelec.html',{'tekst':horoskop()})

def koziorozec(request):
    print('Koziorożec')
    return render(request, 'koziorozec.html',{'tekst':horoskop()})

def home(request):
    print('Horoskop')
    if request.method == 'POST':
        zodiac = request.POST.get('url')
        print(zodiac)
        return redirect(zodiac)
    return render(request, 'home.html')

def horoskop():
    print('Twój Horoskop')
    z1 = ['Czeka cię wspaniały tydzień! ','W najbliższym czasie spotka cię coś wspaniałego. ','Nadchodzą burzliwe dni - nie martw się jednak na zapas. ','W twoim środowisku nastąpi zauważalna zmiana aury. ','W najbliższych dniach zadbaj o swoje zdrowie i komfort psychiczny. ']
    z2 = ['Przed tobą wiele ważnych decyzji, które mogą zmienić twoją przyszłosć. ','Przed tobą bardzo ważny wybór. ','Twoje życie już niedługo może zmienić się na lepsze. ','Najprawdopodobniej wydarzy się to, o czym myślisz już od dawna. ','Nie bój się ryzyka - do odważnych świat należy! ']
    z3 = ['Uważaj koniecznie na swoje najbliższe otocznie. ','Miej się na baczności, szczególnie w pracy lub szkole. ','Pozwól sobie na odrobinę relaksu w nadchodzących tygodniach. ','Wykorzystuj każdy dzień w pełni i ciesz się życiem. ','Troszcz się o siebie i swoich bliskich i nie zapomnij doceniać tego, co masz. ']
    z4 = ['Osoby spod twojego znaku zodiaku mogą być wyjątkowo podatne na wpływ księżyca. ','Osoby spod twojego znaku mogą mieć problemy ze snem. ','Szukaj w sobie wewnętrznej siły i równowagi - tę zapewni układ planet w nadchodzących tygodniach. ','Układ planet w kolejnych dniach pomoże ci odkryć w sobie nową energię. ','Osoby o twoim znaku zodiaku mogą poczuć się przemęczone - zadbaj o siebie. ']
    z5 = 'Twój szczęśliwy dzień w kolejnym miesiącu to: '
    z6 = random.randint(1,29)
    return(random.choice(z1) + random.choice(z2) + random.choice(z3) + random.choice(z4) + (z5) + str(z6))
