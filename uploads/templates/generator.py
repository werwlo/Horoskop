import random


z1 = ['Czeka cię wspaniały tydzień!','W najbliższym czasie spotka cię coś wspaniałego.','Nadchodzą burzliwe dni - nie martw się jednak na zapas.','W twoim środowisku nastąpi zauważalna zmiana aury.','W najbliższych dniach zadbaj o swoje zdrowie i komfort psychiczny.']
z2 = ['Przed tobą wiele ważnych decyzji, które mogą zmienić twoją przyszłosć.','Czeka cię bardzo ważny wybór.','Twoje życie już niedługo może zmienić się na lepsze.','Najprawdopodobniej wydarzy się to, o czym myślisz już od dawna.','Nie bój się ryzyka - do odważnych świat należy!']
z3 = ['Uważaj koniecznie na swoje najbliższe otocznie.','Miej się na baczności, szczególnie w pracy lub szkole.','Pozwól sobie na odrobinę relaksu w nadchodzących tygodniach.','Wykorzystuj każdy dzień w pełni i ciesz się życiem.','Troszcz się o siebie i swoich bliskich i nie zapomnij doceniać tego, co masz.']
z4 = ['Osoby spod twojego znaku zodiaku mogą być wyjątkowo podatne na wpływ księżyca.','Osoby spod twojego znaku mogą mieć problemy ze snem.','Szukaj w sobie wewnętrznej siły i równowagi - tę zapewni układ planet w nadchodzących tygodniach.','Układ planet w kolejnych dniach pomoże ci odkryć w sobie nową energię.','Osoby o twoim znaku zodiaku mogą poczuć się przemęczone - zadbaj o siebie.']
z5 = 'Twoje szczęśliwe dni w kolejnym miesiącu to:'
print(random.choice(z1), end =" "),
print(random.choice(z2), end =" "),
print(random.choice(z3), end =" "),
print(random.choice(z4))
print(z5),
for i in range (3):
    print(random.randint(1,29))