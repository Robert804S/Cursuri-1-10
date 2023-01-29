#dict

dictionar1 = {0:'Luni', 1:'Marti'}
print(dictionar1)

# print(dictionar1.keys())
# print(dictionar1.values())

dictionar1.update({2:'Miercuri'})
print(dictionar1)

# dictionar1.pop(0) # scoatem key 0
# print(dictionar1)

dictionar1.popitem() # returneaza ultimul elem. (elimina din dictionar)
print(dictionar1)

if 0 in dictionar1.keys():
    print(f'exista si are valoarea {dictionar1.get(0)}')
else:
    print('nu este')

if 'Luni' in dictionar1.values():
    print('valoarea luni exista')
else:
    print('nu exista')