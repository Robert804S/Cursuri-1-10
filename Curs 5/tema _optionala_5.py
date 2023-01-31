'''
1. Funcție care primește o lună din an și returnează câte zile are acea luna
'''

def days_in_month(month):
    if month in ('Aprilie', 'Iunie', 'Septembrie', 'Noiembrie'):
        return 30
    elif month in ('Februarie'):
        return 28
    elif month in ('Ianuarie', 'Martie', 'Mai', 'Iulie', 'August', 'Octombrie', 'Decembrie'):
        return 31
    else:
        return 'Luna invalida'

print(days_in_month('Iunie'))

'''
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)
● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)
'''

def calculator(x, y):
    suma = x + y
    diferenta = x - y
    inmultirea = x * y
    impartirea = x / y
    return suma, diferenta, inmultirea, impartirea

print(calculator(11, 2))

'''
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

'''
4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
'''

def maximum(a, b, c):            # varianta 1
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(maximum(8, 7, 8))

def maximum(a, b, c):            # varianta 2
    return max(a, b, c)

print(maximum(1, 2, 3))
print(maximum(3, 2, 1))
print(maximum(2, 2, 2))

'''
5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
'''

def suma(numar):
    total = 0
    for i in range(numar+1):
        total += i
    return total

print(suma(4))
