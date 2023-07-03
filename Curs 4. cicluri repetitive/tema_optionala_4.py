'''
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''
from random import random

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

# for numar in alte_numere:
#     if numar % 2 == 0:
#         numere_pare.append(numar)
#     else:
#         numere_impare.append(numar)
#     if numar > 0:
#         numere_pozitive.append(numar)
#     else:
#         numere_negative.append(numar)
# print(f"Numere pare: {numere_pare}")
# print(f"Numere impare: {numere_impare}")
# print(f"Numere pozitive: {numere_pozitive}")
# print(f"Numere negative: {numere_negative}")

'''
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

# while True:
#     ordonata = True
#     for i in range(len(alte_numere) - 1):
#         if alte_numere[i] > alte_numere[i + 1]:
#             alte_numere[i], alte_numere[i + 1] = alte_numere[i + 1], alte_numere[i]
#             ordonata = False
#     if ordonata:
#         break
# print(alte_numere)

'''
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
'''
import random

# numar_secret = random.randint(1, 30)
# numar_ghicit = None
#
# while numar_ghicit != numar_secret:
#     numar_ghicit = int(input("Alegeți un număr între 1 și 30: "))
#     if numar_ghicit > numar_secret:
#         print("Numărul secret este mai mic.")
#     elif numar_ghicit < numar_secret:
#         print("Numărul secret este mai mare.")
#     else:
#         print("Felicitări! Ai ghicit!")

'''
4. Alege un număr de la tastatură
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
'''

# numar_piramida = int(input('Introduceti numarul: '))
# for i in range(1, numar_piramida +1):
#     for j in range(1, i + 1):
#         print(i, end="")
#     print()

# nr_introdus = int(input('Introduceti un numar de la 1 la 9: '))
# nr_initial = 1
# while nr_initial <= nr_introdus:
#     print(str(nr_initial)*nr_initial)
#     nr_initial += 1

'''
5.tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# for lista in tastatura_telefon:
#     for cifra in lista:
#         print(f"Cifra curentă este {cifra}")

for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Numarul curent este {tastatura_telefon[i][j]}')