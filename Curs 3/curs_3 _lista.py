# avem o lista ce contine diferite tipuri de date

lista1 = ["Maria", 32, True, 12.5]
# print(type(lista1))
print(lista1)

print(len(lista1))

# afiseaza primul si ultimul element
print(lista1[0])
print(lista1[-1])

lista1.remove(lista1[0])
print(lista1)

lista1.pop(0)
print(lista1)

lista1 = lista1 + ["Ion"]
print(lista1)
lista1.append('Rex')
print(lista1)
lista1.extend([1,2,3])
print(lista1)

lista1.insert(2,"14") # adaugam pe indexul 2
print(lista1)

