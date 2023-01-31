"""
Incapsulare = posbilitatea de a PROTEJA atrbutele/metodele unei clase, folosind meodificatorii de vizibilitate

- private (privat, adica atributul/metoda poate fi accesata doar din interiorul clasei in care a fost definit)
          -- se defineste cu underscore in fata (variabila sau metoda(): )
- protected (protejat, atributul/metoda poate fi accesata din calasa in care a fost defnita,
            dar si din clasele copil ale acesteia, INSA NU din exterior)

Atunci cand avem un atribut ascuns putem folosi metode speciale pentru a interactiona cu el:
Numite getter, setter si delter
getter -> pe a-l vedea/ a avea acces la atribut
setter -> pentru a-i schimba valoarea
deleter -> pentru a sterge valoarea

Conventie: aceste metode trebuie denumite cu set,delete si get_ + numele variabilei
"""

class Car:

    variabila_privata = "privat"
    _variabila_protected = "protected"

    def __init__(self,var_protected):
        self._variabila_protected = var_protected
    #getter
    def get_variabila_privata(self):
        return self.variabila_privata
    #setter
    def set_variabila_privata(self,var):
       self.variabila_privata = var

    #deleter
    def delete_variabila_privata(self):
        self.variabila_privata = None


masina = Car('Update Protected')
# print(masina._variabila_protected)   # convetie ca aceasta variabila sa nu fie accesata.

# print(masina.__variabila_privata)   #-> eroare, variabilele private nu avem acces

print(masina.get_variabila_privata())
masina.set_variabila_privata("Update Private")

print(masina.get_variabila_privata())
masina.delete_variabila_privata()

print(masina.get_variabila_privata())

# "------------------------------------------------------------------"
# Getter, setter, delete intr-un mod pythonic

class CarPy:

    def __init__(self,color):
        self.color = color
        self.nr_roti = 0
    @property
    def color(self):
        return self.color

    @property
    def nr_roti(self):
        return self.nr_roti

    @color.getter
    def color(self):
        print(f"Getter: Culoare {self.color}")
        return self.color

    @color.setter
    def color(self, color):
        print(f"setter: Setam culoarea in {color}")
        self.color = color

    @color.deleter
    def color(self):
        self.color =None


car_py = CarPy("negru")
car_py.color
car_py.color = "Albastru"
car_py.color
del car_py.color
car_py.color