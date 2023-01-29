# tuple

tupla = tuple()
tupla2 = ()
print(type(tupla))
print(type(tupla2))

tupla = (10,20,30,40)
print(tupla)
print(tupla.count(30))

#accesam ultimul elem
print(tupla.index(40))  # returneaza indexul valorii apelate
print(tupla[-1])

tupla_nested = (10,20,30,40, (1,2,3,4))
print(tupla_nested)

# accesam elem 3
print(tupla_nested[4][2])

if 40 in tupla_nested:
    print('40 este')
else:
    print('nu este')