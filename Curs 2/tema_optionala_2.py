# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = 10000
if x in range(1000, 10000):
    print('x are 4 cifre')
else:
    print('x NU are are 4 cifre')

# 2. Verifica daca x are exact 6 cifre
x = 100000
if x in range(100000, 1000000):
    print('x are exact 6 cifre')
else:
    print('x NU are exact 6 cifre')

# 3. Verifica daca x este numar par sau impar
x = 9
if x %2 == 0:
    print('x este numar par')
else:
    print('x este numar impar')

# 4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre
# ele
x = 2
y = 4
z = 4
if x > y and x > z:
    print(f'x = {x}, este mai mare')
elif y > x and y > z:
    print(f'y = {y}, este mai mare')
else:
    print(f'z = {z}, este mai mare')

# 5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
# triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
# 180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
# lungimea celei de-a treia laturi)
x = 60
y = 60
z = 60
if x + y + z == 180:
    print('triunghiul este valid')
else:
    print('triunghiul NU este valid')

# 6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
# la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
# ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
# smarte'
str = 'Coral is either the stupidest animal or the smartest rock'
xyz = int(input('Introduceti numar: '))
nr = str[0:-xyz]
print(f'{nr}')

# 7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
# din primele 5 caractere + ultimele 5
string_nou = str[0:5] + str[-5:len(str)]
print(string_nou)

# 8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
# indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
# (hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
# afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
# animal or the smartest '
str = 'Coral is either the stupidest animal or the smartest rock'
print(str.find('rock'))
print(str[slice(str.find('rock'))])

# 9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
# va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
# e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
# functie pentru a face string-ul case insensitive)
cuvant = input('Introduceti cuvant: ')
a = cuvant[0:1]
z = cuvant[-1:len(cuvant)]
print(f'{a} {z}')
assert a.lower() == z.lower()
print('Totul e ok')

# 10. Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)
str = '0123456789'
print(str[0:len(str)-1:2])
print(str[1:len(str):2])