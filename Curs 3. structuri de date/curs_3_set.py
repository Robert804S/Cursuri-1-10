# set

new_set = set()         # declaram un set gol
# new_set2 = {1,2,3}
# atentie = {}    # se declara un dictionar

new_set.update([1,2,3,4,5,6,1])    # nu accepta duplicate
print(new_set)

new_set.add(7)  # adaugam element
print(new_set)

new_set.add(0)
print(new_set)

new_set2 = {'martie', 'aprilie', 1, 2}
print(new_set2)

new_set.update(new_set2)
print(new_set)

print('new set - new set 2' + str(new_set.difference(new_set2)))  # diference returneaza un al 3lea set

# intersectia a doua seturi
print(new_set.intersection(new_set))    # intersection returneaza un al 3lea set cu valori comune dintre cele doua seturi

if 3 in new_set:
    print('este')
else:
    print('nu este')