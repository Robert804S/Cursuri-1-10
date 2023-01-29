'''
structuri repetitive = modalitati prin care putem executa un cod in mod repetat pana cand
o anumita conditie nu mai este indeplinita
1 - while
2 - do while (nu este in phyton)
3 - for
4 - for each

Modalitati de control a structurilor repetitive
Break - opreste executarea structurii repetitive
Continue - face skip la o iteratie
'''

'''
while = structura repetitiva in care executam o serie de instructiuni atata timp cat conditia este adevarata.
    De regula elementul sau variabila de control al while se declara in afara acestuia sau inaintea acestuia
'''

# printeaza pe ecran toate numerele de la 1 la 10
# i = 1
# while i <= 10:
#     print(i)
#     i +=1

# Debugging - proces prin care analizam codul pentru a vedea cum circula datele
# de fiecare data cand vrem sa facem debugging putem pune brake point

# suma numerelor de la 1 la 500
# suma = 0
# i = 1
# while i <= 500:
#     suma += 1
#     i += 1
# print(suma)

# lista cu lunile anului - parcurgem fiecare luna
list1 = ['ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie', 'iulie']
index = 0
# while index < len(list1):
#     print(list1[index])
#     index += 1

# lista fara martie si mai
# while index < len(list1):
#     if list1[index] == 'martie' or list1[index] == 'mai':
#         index += 1
#         continue
#     print(list1[index])
#     index += 1

# parcurgem lista pana la aprilie
# while index < len(list1):
#     if list1[index] == 'aprilie':
#         break
#     print(list1[index])
#     index += 1

#  inlocuim luna mai cu luna noiembrie
# while index < len(list1):
#     if list1[index] == 'mai':
#         list1[index] = 'noiembrie'
#         break
#     index += 1
# print(list1)