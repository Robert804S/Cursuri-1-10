'''
1.Funcție care să calculeze și să returneze suma a două numere
'''

def suma_numerelor(a, b):
    return (f'Suma celor doua numere este: {a + b}')

print(suma_numerelor(5, 5))
'''
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
'''

def par_sau_impar(a):
    if a % 2 == 0:
        return True
    else:
        return False

print(par_sau_impar(4))

'''
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
'''

def numar_total_caractere(nume, prenume, nume_mijlociu):
    nume = len(nume)
    prenume = len(prenume)
    nume_mijlociu = len(nume_mijlociu)
    print(f'Suma tuturor caracterelor este: {nume + prenume + nume_mijlociu}')

numar_total_caractere('Stanescu', 'Robert', 'NuAm')

'''
4. Funcție care returnează aria dreptunghiului
'''

def aria_dreptunghiului(a, b):
    return (f'Aria dreptunghiului este: {a * b}')

print(aria_dreptunghiului(5, 4))

'''
5. Funcție care returnează aria cercului
'''

def aria_cercului(raza):
    aria = 3.14 * raza ** 2
    print(f'Aria cercului este: {aria}')

aria_cercului(4)

'''
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.
'''

def caracter_in_string(a, b):
    if a in b:
        return True
    else:
        return False

print(caracter_in_string('t', 'acasa'))

'''
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
'''

def string_litere_mari_si_mici(string):
    lower_case = 0
    upper_case = 0
    for char in string:
        if char.islower():
            lower_case = lower_case + 1
        elif char.isupper():
            upper_case = upper_case + 1
    print(f'Numarul de caractere lower case este: {lower_case}')
    print(f'Numarul de caractere upper case este: {upper_case}')

string_litere_mari_si_mici('SaluT')

'''
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
'''

def lista_numere(lista):
    lista_numere_pozitive = []
    for numar in lista:
        if numar > 0:
            lista_numere_pozitive.append(numar)
    return print(lista_numere_pozitive)

lista_numere([-1, 0, 1, 2, -4, 7])

'''
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
'''

def comparatie_numere(a, b):
    if a > b:
        print(f'Primul numar {a} este mai mare decat al doilea numar {b}')
    elif b > a:
        print(f'Al doilea numar {b} este mai mare decat primul numar {a}')
    else:
        print('Numerele sunt egale')

comparatie_numere(9, 9)

'''
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
'''

def add_number_to_set(number, number_set):
    if number in number_set:
        print(f'Nu am adaugat numărul {number} în set. Acesta există deja')
        return False
    else:
        number_set.add(number)
        print(f'Am adaugat numărul {number} în set')
        return True

print(add_number_to_set(8, {6, 5, 4}))
