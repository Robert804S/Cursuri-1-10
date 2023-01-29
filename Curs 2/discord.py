#Exercitiu 1 - Curs 2
# bancomat
# verificam username-ul si parola
# user-ul are 2 incercari de a-si introduce username-ul. la a doua incercare gresita se iese din program
# daca userul isi poate scoate o suma mai mica sau egala cu soldul curent
# daca introducem o suma prea mare poate sa aleaga daca sa reincerce sau nu
# la a doua incercare, daca user-ul introduce o suma prea mare, se iese din program

# expected_user_name = 'username'
# expected_password = 'password'
# sold = 5000
# username = input('Introduceti username: ')
# if username == expected_user_name:
#     print('Username corect')
# else:
#     print('Username incorect')
#     username = input('Introduceti username: ')
#     assert username == expected_user_name, 'Username gresit a doua oara'
# password = input('Introduceti parola: ')
# if len(password) == len(expected_password) and password == expected_password:
#     print('Parola corecta')
# else:
#     print('Parola gresita')
#     password = input('Introduceti parola: ')
#     assert password == expected_password, 'Parola gresita a doua oara'
# suma_extrasa = int(input('Introduceti suma: '))
# if suma_extrasa <= sold:
#     print('Tranzactie reusita')
# else:
#     print('Suma dorita depaseste soldul curent')
#     reincercare = input('Doriti sa reintroduceti suma? ')
#     if reincercare == 'Da':
#         suma_extrasa = int(input('Introduceti suma: '))
#         assert suma_extrasa <= sold, 'Suma dorita depaseste soldul curent'
#         print('Tranzactie acceptata')
#     elif reincercare == 'Nu':
#         print('Multumesc')

#Exercitiu 2 - Curs 2

import random

dice_number = [1,2,3,4,5,6]
dice_roll = random.choice(dice_number)
number = int(input('Introdu un numar de la 1 la 6: '))
if number < dice_roll:
    print(f'Ai pierdut, ai ales un numar mai mic. Ai ales {number}, dar a fost {dice_roll}')
elif number > dice_roll:
    print(f'Ai pierdut, ai ales un numar mai mare. Ai ales {number}, dar a fost {dice_roll}')
else:
    print(f'Ai ghicit! Ai ales {number} si a fost {dice_roll} ')

import math

# Exercitiul 1 - tema optionala
# x = input()
# assert len(x)%2 != 0, 'Lungimea stringului este para'
# caracter_mijloc = math.floor(len(x)/2)
# print(x[caracter_mijloc])