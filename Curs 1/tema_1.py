# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# Variabila = spatiu din memorie ce contine date.

# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
# variabilă : - string - int - float - bool.

tip_carte = 'fictiune'
numar_pagini = 230
pret = 45.5
are_coperta = True

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(tip_carte))
print(type(numar_pagini))
print(type(pret))
print(type(are_coperta))

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
#aceeași variabilă (suprascriere): - Verifică tipul acesteia.
print(round(pret))
pret = 46
print(pret)
print(type(pret))

# 5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
print('Am cumparat o carte de genul ' + tip_carte)
print(f'Cartea are {numar_pagini} pagini')
print(f'Am platit pentru carte {pret} lei')
print(f'Este {are_coperta} ca are coperta')

# 6. Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.

numele = input('Intruduceti numele: ')
prenumele = input('Introduceti prenumele: ')
nr_litere_nume = len(numele)
nr_litere_prenume = len(prenumele)
print(f'Numele complet are {nr_litere_nume + nr_litere_prenume} caractere')

# 7. Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.

lungimea = int(input('lungimea ='))
latimea = int(input('latimea ='))
aria = lungimea * latimea
print(f'Aria dreptunghiului este {aria}')

# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - afișează de câte ori apare cuvântul 'the';

afirmatie = 'Coral is either the stupidest animal or the smartest rock'
afirmatie.count('the')
de_cate_ori_se_repeta_the: int = afirmatie.count('the')
print(f'Cuvantul the se repeta de {de_cate_ori_se_repeta_the} ori in propozitia de mai sus')

# 10. Același string. Folosiți un assert ca să verificați dacă acest string conține doar numere.

assert type(de_cate_ori_se_repeta_the) == int
print('totul e ok')