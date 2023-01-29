# 1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
# If else = evalueaza conditii si bifurca codul

# 2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
# daca este numar intreg mai mare ca 0)
x = 70
y = 2
if x > 0:
    print('x este numar natural')
else:
    print('x NU este un numar natural')

# 3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
if x > 0:
    print('x este numar pozitiv')
elif x < 0:
    print('x este numar negativ')
else:
    print('x este numar neutru')

# 4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).
if x < -2:
    print('x NU se afla intre -2 si 13')
elif x > 13:
    print('x NU se afla intre -2 si 13')
else:
    print('numarul se afla in intervalul dat')

# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
# cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
# abs

x = 4
y = 8
if x - y < 5:
    print('Diferenta este mai mica decat 5.')
else:
    print('Diferenta nu este mai mica decat 5')

# 6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
x = 25
if x not in range(5,28):
    print('x NU se afla in intervalul dat')
else:
    print('x se afla in intervalul dat')

# 7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
# daca nu, afiseaza care din ele este mai mare
x = 6
y = 7
if x == y:
    print('x si y sunt egale')
elif x > y:
    print(f'{x} este mai mare decat {y}')
else:
    print(f'{y} este mai mare decat {x}')

# 8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
# triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
# oarecare (nicio latura nu e egala).
x = 2
y = 4
z = 6
if x == y == z:
    print('triunghiul este echilateral')
elif x == y or y == z or z == x:
    print('triunghiul este isoscel')
else:
    print('triunghiul este oarecare')

# 9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
# Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
# vocale_1 = ['A', 'E', 'I', 'O', 'U', 'Ă', 'Î']
# vocale_2 = ['a', 'e', 'i', 'o', 'u', 'ă', 'î']
# litera = input('Introduceti o litera: ')
# if litera in vocale_1:
#     print('Litera este vocala')
# elif litera in vocale_2:
#     print('Litera este vocala')
# else:
#     print('Litera este consoana')

# 10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
# urmeaza:
#    a. Peste 9 => A
#    b. Peste 8 => B
#    c. Peste 7 => C
#    d. Peste 6 => D
#    e. Peste 4 => E
#    f. 4 sau sub => F
nota = 10
if nota >= 9 and nota <= 10:
    print('nota este A')
elif nota >= 8 and nota < 9:
    print('nota este B')
elif nota >= 7 and nota < 8:
    print('nota este C')
elif nota >= 5 and nota < 7:
    print('nota este D')
elif nota >= 1 and nota <= 4:
    print('nota este F')
else:
    print('nota nu exista')
