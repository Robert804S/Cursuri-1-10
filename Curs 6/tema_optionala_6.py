'''
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
'''
import datetime


# class Factura():
#     def __init__(self, numar, nume_produs, cantitate, pret_bucata):
#         self.serie = 12345
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_bucata = pret_bucata
#
#     def schimba_cantitatea(self):
#         self.cantitate = int(input('Introduceti noua cantitate: '))
#
#     def schimba_pretul(self):
#         self.pret_bucata = int(input('Introduceti noul pret: '))
#
#     def schimba_nume_produs(self):
#         self.nume_produs = input('Introduceti noul nume de produs: ')
#
#     def genereaza_factura(self):
#         from datetime import date
#         print(f'Factura seria: {self.serie}, numarul: {self.numar}')
#         data = date.today()
#         print(data)
#         total = self.cantitate * self.pret_bucata
#         print('Nume Produs | Cantitate | Pret Bucata | Total|')
#         print(f'{self.nume_produs} | {self.cantitate} | {self.pret_bucata} | {total} |')
#
# telefon = Factura(1, 'Telefon', 3, 200)
#
# telefon.genereaza_factura()
#
# print(50 * '*')
#
# telefon.schimba_cantitatea()
# telefon.schimba_pretul()
# telefon.schimba_nume_produs()
# telefon.genereaza_factura()

'''
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
'''

# class Masina():
#     def __init__(self, model, viteza_maxima):
#         self.marca = 'Dacia'
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#         self.viteza_actuala = 0
#         self.culoare = 'Gri'
#         self.culori_disponibile = {'Roz', 'Alb', 'Negru', 'Galben', 'Rosu'}
#         self.inmatriculata = False
#
#     def descriere(self):
#         print(f'{self.marca} | {self.model} | {self.viteza_maxima} | {self.viteza_actuala} | {self.culoare} | {self.inmatriculata}')
#
#     def inmatriculare(self):
#         self.inmatriculata = True
#
#     def vopseste(self):
#         while self.culoare not in self.culori_disponibile:
#             self.culoare = input('Introduceti culoarea dorita: ')
#             if self.culoare in self.culori_disponibile:
#                 self.culoare = self.culoare
#                 print(f'Culoarea masinii este acum {self.culoare}')
#             else:
#                 print('Culoarea dorita nu se afla in lista de culori disponibile!')
#
#
#     def accelereaza(self):
#         while self.viteza_actuala <= 0:
#             cu_cat_acceleram = int(input('Introduceti cu cati Km/H sa acceleram masina: '))
#             self.viteza_actuala = 0
#             self.viteza_actuala = self.viteza_actuala + cu_cat_acceleram
#             if self.viteza_actuala < 0:
#                 print('Eroare, viteza nu poate sa fie negativa!')
#         if self.viteza_actuala > self.viteza_maxima:
#             self.viteza_actuala = self.viteza_maxima
#         print(f'Viteza actuala este: {self.viteza_actuala} Km/H')
#
#     def franeaza(self):
#         self.viteza_actuala = 0
#         print(f'Masina s-a oprit si are viteza: {self.viteza_actuala} Km/H')
#
# masina_1 = Masina('Logan', 175)
# masina_1.descriere()
# masina_1.inmatriculare()
# masina_1.vopseste()
# masina_1.accelereaza()
# masina_1.franeaza()
#
# print(50 * '*')

'''
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:
● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
'''

class ToDoList():
    def __init__(self):
        self.todo = {}

    def adauga_task(self):
        nume_task = input('Introduceti noul task: ')
        descriere_task = input('Introduceti descrierea task-ului: ')
        self.todo.update({nume_task: descriere_task})

    def finalizeaza_task(self):
        self.todo.pop(input('Intriduceti numele task-ului ce a fost finalizat: '))

    def afiseaza_to_do_list(self):
        print(self.todo.keys())

    def afiseaza_detalii_suplimentare(self):
        nume_task = input('Introduceti numele task-ului caruia doriti sa-i vedeti descrierea: ')
        if nume_task in self.todo.keys():
            print(self.todo[nume_task])
        if nume_task not in self.todo.keys():
            raspuns = input('Task-ul nu se afla in todo list, doriti sa il adaugati? da sau nu: ')
            if raspuns == 'da':
                nume_task = input('Introduceti noul task: ')
                descriere_task = input('Introduceti descrierea task-ului: ')
                self.todo.update({nume_task: descriere_task})
            else:
                print('La revedere!')

activitate_1 = ToDoList()
activitate_1.adauga_task()
activitate_1.finalizeaza_task()
activitate_1.adauga_task()
activitate_1.afiseaza_to_do_list()
activitate_1.afiseaza_detalii_suplimentare()

print(50 * '*')

activitate_1.afiseaza_to_do_list()