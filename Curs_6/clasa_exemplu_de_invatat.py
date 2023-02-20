class Exemplu:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def afiseaza_nume(self):
        print(self.nume)

    def afiseaza_varsta(self):
        print(self.varsta)

# Crearea unui obiect de tip Exemplu
obiect_exemplu = Exemplu("John", 30)

# Apelarea metodelor
obiect_exemplu.afiseaza_nume() # "John"
obiect_exemplu.afiseaza_varsta() # 30

'''
Clasa "Exemplu" are doua atribute: "nume" si "varsta", si doua metode: "afiseaza_nume" si "afiseaza_varsta". 
In metoda constructor "init", se initializeaza aceste atribute cu valorile primite ca parametri. 
In acest exemplu, se creaza un obiect de tip "Exemplu" cu numele "John" si varsta 30, 
si se apeleaza metodele "afiseaza_nume" si "afiseaza_varsta" pentru a afisa aceste valori.
'''