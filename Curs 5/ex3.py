3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1: 2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''
def functie_dict():
    dictionar = {}
    lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
    for i in range(0, 10):
        contor = 0
        for j in range(0, len(lista)):
            if i == lista[j]:
                contor += 1
                dictionar.update({i: contor})

            else:
                dictionar.update({i: contor})

    return dictionar