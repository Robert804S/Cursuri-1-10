# definirea unei functii simple (fara parametrii si return)

def hello_world ():
    print('Hello World!')
#
# hello_world()  # fara paranteze functia nu va fi executata
# # daca o functie nu este apelata codul din interiorul ei nu va fi executat
#
# x = hello_world() # codul din functie va fi executat iar x va lua valoare de NONE (functia nu returneaza nimic)
# print(x)

# def say_hi_name (name): # name este un parametru
#     print(f'Hi, my name is {name}')
#
# say_hi_name('Cosmin') # Cosmin este un argument al parametrului name
#
# lista_nume = ['Iuliana', 'Cosmin', 'Andrei']
# say_hi_name(lista_nume)
#
# for nume in lista_nume:
#     say_hi_name(nume)

# definim o functie care sa ne zica daca un numar este par sau impar

def is_even (numar):
    numar = int(input('Introduceti numar: '))
    if numar % 2 == 0:
        return True
    else:
        return False
#
# if is_even(10) == True:
#     print('este par')

# functie ce returneaza suma elementelor din lista

def suma_numere (lista_numere):
    suma = 0
    for numar in lista_numere:
        suma += numar
    return suma

# lista_1 = [1, 2, 3, 4]
# print(suma_numere(lista_1))

# o functie ce ne returneaza valoarea maxima din lista

# def nr_maxim (lista):
#     maxim = 0
#     for numar in lista:
#         if numar > maxim:
#             maxim = numar
#     return maxim
# print(nr_maxim(lista_1))

def numar_maxim2 (*numere):
    maxim = 0
    for numar in numere:
        if numar > maxim:
            maxim = numar
    return maxim, "numar maxim"
# m = numar_maxim2(1, 2, 3, 4, 5)
# # print(numar_maxim2(1, 2, 3, 4, 5, 20, 30))
# print(m)
#
# m,string = numar_maxim2(1, 2, 3, 4, 5)
# # print(numar_maxim2(1, 2, 3, 4, 5, 20, 30))
# print(m)
# print(string)

# variabila globala = variabila definita in afara functiei care poate fi folosita in interiorul oricarei functii
var_globala = 30
# print(str(var_globala),'din afara functiei')

def dummy():
    # var_globala = 60
    # print(str(var_globala), 'din interiorul functiei') # valoarea variabilei globale ramane nemodificata in afara functiei
    # pentru a modifica valoarea variabilei globale in interiorul unei functii folosim Key Word-ul global
    global var_globala
    print(var_globala)
# dummy()
# print(var_globala)

def say_my_age(age = 10):
    print(age)
    # return 'sunt aici'
say_my_age()
say_my_age(30)

'''
def - key word care anunta inceputul unei functii
say_my_age - numele functiei, dat de catre user, poate sa fie orice nume. In general numele functiei trebuie sa fie sugestiv pentru actiunea pe care o face
() - reprezentant al zonei in care putem sa specificam parametrii (parametrii sunt optionali)
: - reprezinta inceputul corpului functiei
corpul functiei (asemanator structurilor if, while, for)
'''