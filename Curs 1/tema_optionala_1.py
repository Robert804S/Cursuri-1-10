# 1- citește de la tastatură un string de dimensiune impară; - afișează caracterul din mijloc.

cuvant_impar = input('cuvant de dimensiune impara: ')
lungime = len(cuvant_impar)
middle_char = lungime // 2
print('Caracterul din mijloc este: ' + cuvant_impar[middle_char])

# 2. Folosind assert, verifică dacă un string este palindrom.

cuvant_palindrom = input('cuvant palindrom de dimensiune impara: ')
assert cuvant_palindrom == cuvant_palindrom[::-1]
print('totul e ok')

# 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.

text = input('introduceti cuvant: ')
x,y = text.split(' ')
print(x)
print(y)

# 4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.

string1 = input('string de la tastatura: ')
metoda_slice = slice(0, 1)
string2 = string1[metoda_slice]
print(string2)
string_modificat = string1[0]+string1[1:len(string1)-1].replace('a','A'.upper())+string1[len(string1)-1]
print(string_modificat)

# 5 - citește un user de la tastatură;
# - citește o parolă; - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.

user = input('introduceti user: ')
parola = input('introduceti parola: ')
lungime_parola = len(parola)
parola_secreta = '*' * len(parola)
print(f'parola pentru user {user} este {parola_secreta} si are {lungime_parola} caractere')
