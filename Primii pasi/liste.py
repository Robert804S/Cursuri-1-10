# listele in python pot sa cuprinda elemente diferite
# au dimensiune dinamica

fructe = ['Mar', 'Banana', 'Portocala', 3, True, 3]

# afisam o lista
print(fructe)

# accesam un element in functie de index
print(fructe[1])

# adaugam un element
fructe.append('Rosie')

# suprascriem un element
fructe[0] = 'Para'

# afisam lista
print(fructe)

# aflam dimensiunea listei
print(len(fructe))

# scoate si ne returneaza ultimul element
last = fructe.pop()
print(last)
print(fructe)

# de cate ori apare un element
print(fructe.count(3))

# extindem lista
fructe_exotice = ['Ananas', 'Kiwi']
fructe.extend(fructe_exotice)
print(fructe)