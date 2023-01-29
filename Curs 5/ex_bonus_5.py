'''
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
'''

def numere_comune(list1, list2):
    # Convertim listele in seturi
    set1 = set(list1)
    set2 = set(list2)
    # Returnam intersectia dintre cele 2 seturi
    return set1.intersection(set2)

print(numere_comune([1, 1, 2, 3], [2, 2, 3, 4]))

'''
2.. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
'''

def pret_final(pret_intreg):
    reducere = 100 - int(input('Introduceti procentajul aferent reducerii de pret: '))
    pret_redus = pret_intreg / 100 * reducere
    while reducere < 0:
        print('suma invalida')
        break
    else:
        return pret_redus

print(pret_final(100))

'''
3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)
'''

import datetime

def afiseaza_data_ora_curenta():
    data_ora_curenta = datetime.datetime.now()
    print(data_ora_curenta.strftime("%d/%m/%Y %H:%M:%S"))

afiseaza_data_ora_curenta()

'''
4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
'''

import datetime

def zile_pana_la_craciun():
    data_curenta = datetime.datetime.now()
    data_craciun = datetime.datetime(2023, 12, 25)
    zile_ramase = (data_craciun - data_curenta).days
    print(f'Mai sunt {zile_ramase} zile pana la Craciun')

zile_pana_la_craciun()