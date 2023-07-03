# for este o structura repetitiva carea este utilizata atunci cand vrem sa parcurgem o structura de date
# cu scopul de a prelucra datele din acea structura de date
# poate fi folosit sa executam un set de instructiuni de un numar de ori (range)

# structura for
# inceputul structurii 'for'
# variabila de iteratir
# inceputul range-ului de parcurs (default este 0)
# sfarsitul range-ului de parcurs (obliatoriu) - capatul superior nu este luat in considerare
# pasul range-ului care default este 1

# parcurgem numerele de la 0 la 10 si printam separat numerele pare si impare
# for i in range(0,11):
#     if i %2 == 0:
#         print(f'{i} este par')
#     else:
#         print(f'{i} este impar')

# nested list (embedded list) (lista imbricata) (matrice)
# matrice = [
#     [1, "test1"],
#     [2, "test2", 3],
#     [5,6,7]
# ]
# for i in range(len(matrice)):
#     for j in range(len(matrice[i])):
#         print(f'valoarea de pe pozitia [{i}] [{j}] este {matrice[i][j]}')

luni = ['ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie', 'iulie']
# for i in range(len(luni)):
#     print(luni[i])

# for luna in luni: # for each
#     print(luna)

lista_culori_disponibile = ["rosu", "galben", "albastru", "fuchsia", "magenta", "roz", "violet", "maro", "negru",
                            "orange", "verde", "indigo"]
liste_culori_de_exclus = ["rosu", "galben", "roz"]

# lista_culori_neexcluse = []
# for culoare in lista_culori_disponibile:
#     if culoare in liste_culori_de_exclus:
#         continue
#     lista_culori_neexcluse.append(culoare)
# print(lista_culori_neexcluse)

# sortam o lista (algoritmi de sortare)
lista_nesortata = [1, 5, 10, 2, 50, 11, 20, 12]
# lista_nesortata.sort() # suprascrie lista initiala, nu returneaza nimic
# print(lista_nesortata)

for i in range(len(lista_nesortata)-1):
    for j in range(len(lista_nesortata)-1):
        if lista_nesortata[j] > lista_nesortata[j+1]:
            lista_nesortata[j], lista_nesortata[j+1] = lista_nesortata[j+1], lista_nesortata[j]
print(lista_nesortata)