'''
Flow control: if else
evalueaza conditii si bifurca codul
'''

#if
piesa_faina = True
print('pornim radio')
if piesa_faina == True:
    print('dau mai tare')
    print('incep si fredonez')
print('oprim radioul')

#if else
nr = 4
if nr % 2 ==0:
    print('nr par')
else:
    print('impar')

#if, else if, else
# luam date de la tastatura
# ora = int(input('Introduceti ora'))
# if ora < 0:
#     print('ora nu exista')
# elif ora <= 11:
#     print('Buna dimineata')
# elif ora <= 18:
#     print('Buna ziua')
# elif ora <= 21:
#     print('Buna seara')
# elif ora <= 24:
#     print('Noapte buna')
# else:
#     print('Ora nu exista')

viteza = int(input('Introduceti viteza'))
if viteza == 0:
    print("masina stationeaza")
elif viteza <= 50:
    print('masina este in localitate')
elif viteza <= 90:
    print('masina este in afara localitatii')
elif viteza <= 130:
    print('masina este pe autostrada')
else:
    print('masina circula cu o viteza prea mare')


