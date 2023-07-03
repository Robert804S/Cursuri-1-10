'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''

lista_masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# for masina in range(len(lista_masini)):
#     print(f'Masina mea preferata este {lista_masini[masina]}')
#     masina = masina + 1
#
# for masina in lista_masini:
#     print(f'Masina mea preferata este {masina}')
#
# i = 0
# while i < len(lista_masini):
#     print(f'Masina mea preferata este {lista_masini[i]}')
#     i += 1

'''
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrise cu majuscule,
exceptând primul și ultimul.
În else
- Printează lista.
'''

# for masina in range(len(lista_masini)):
#   for masina in range(1,len(lista_masini)-1):
#     lista_masini[masina] = lista_masini[masina].upper()
# else:
#   print(lista_masini)

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''

# for masina in lista_masini:
#     print(f'Am gasit masina {masina}')
#     if masina == "Mercedes":
#         print('Am gasit masina aleasa de DVS')
#         break
# print(f'Am gasit masina {masina}, mai cautam?')

'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
'''

# masini_scumpe = []
# for masina in lista_masini:
#     if masina == "Trabant" or masina == "Lastun":
#         continue
#     masini_scumpe.append(masina)
# for masina_scumpa in masini_scumpe:
#     print(f'S-ar putea sa va placa masina {masina_scumpa}')

'''
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
'''

# masini_vechi = []
#
# for masina in lista_masini:
#     if masina == 'Lastun':
#         masini_vechi.append('Lastun')
#         lista_masini[lista_masini.index('Lastun')] = 'Tesla'
#     if masina == 'Trabant':
#         masini_vechi.append('Trabant')
#         lista_masini[lista_masini.index('Trabant')] = 'Tesla'
# print(f'Masini vechi = {masini_vechi}')
# print(f'Masini noi = {lista_masini}')

'''
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
'''

pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}

# buget = 15000
#
# for masina, pret in pret_masini.items():
#   if pret <= buget:
#     print(f"Pentru un buget de sub {buget} euro puteți alege mașina {masina} la pretul de {pret} euro")

'''
7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

# contor = 0
# for numar in numere:
#   if numar == 3:
#     contor += 1
# print(f"Numărul 3 apare de {contor} ori în listă.")

'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

# suma = 0
# for numar in numere:
#   suma = suma + numar
#
# print(f"Suma elementelor din listă este: {suma}.")

'''
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

# maxim = 0
# for numar in numere:
#   if numar > maxim:
#     maxim = numar
# print(f"Cel mai mare număr din listă este: {maxim}.")

'''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

# for i, numar in enumerate(numere):
#   if numar > 0:
#     numere[i] = -numar
# print(f"Noua listă este: {numere}.")

# for i in numere:     # Varianta 2
#     if numere[i] > 0:
#         numere[i] = -numere[i]
# print(numere)
