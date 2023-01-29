# 1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
# inputuri urmatoarele informatii:
# a. Varsta
# b. Insotit de mama
# c. Insotit de tata
# d. Pasaport
# e. Act permisiune mama
# f. Act permisiune tata
# Conditii de imbarcare:
# 1. Daca pers are varsta peste 18 ani si are pasaport
# 2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# 3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
# si are permisiune in scris de la celalat parinte
import random
# el2HgpCjfsad%E$RYg parola

varsta = 20
insotit_de_mama = bool(input('insotit de mama true sau false: '))
insotit_de_tata = bool(input('insotit de tata true sau false: '))
pasaport = bool(input('pasaport true sau false: '))
act_permisiune_mama = bool(input('act permisiune mama true sau false: '))
act_permisiune_tata = bool(input('act permisiune tata true sau false: '))
if varsta >= 18 and pasaport == True:
    print('Te poti imbarca')
elif varsta < 18 and pasaport == True and insotit_de_mama == True and insotit_de_tata == True:
    print('Te poti imbarca')
elif varsta < 18 and pasaport == True and insotit_de_mama == True and act_permisiune_tata == True:
    print('Te poti imbarca')
elif varsta < 18 and pasaport == True and insotit_de_tata == True and act_permisiune_mama == True:
    print('Te poti imbarca')
else:
    print('Nu te poti imbarca')

# 2. Joc de noroc
# - Cauta pe net si vezi cum se genereaza un numar random
# - Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
# Numarul salvat va fi generat random cu metoda gasita in online
# - Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
# - Verifica si afiseaza daca utilizatorul a ghicit numarul
# - Vor exista 3 optiuni care vor trebui tratate:
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# ● Ai ghicit. Felicitari? Ai ales x si zarul a fost y
# zar = [1, 2, 3, 4, 5, 6]
# dice_roll = random.choice(zar)
# nr_de_la_tastatura = int(input('Introdu un numar de la 1 la 6: '))
# if dice_roll > nr_de_la_tastatura:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {nr_de_la_tastatura} dar a fost {dice_roll}')
# elif dice_roll < nr_de_la_tastatura:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {nr_de_la_tastatura} dar a fost {dice_roll}')
# else:
#     print(f'Ai castigat. Ai ales {nr_de_la_tastatura} si a fost {dice_roll}')
