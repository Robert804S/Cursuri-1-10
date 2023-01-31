'''
2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
împreună).

ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
'''

from abc import abstractmethod

class FormaGeometrica:
    def __init__(self):
        self.PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descriere(self):
        print('Cel mai probabil am colturi')

# forma_geometrica1 = FormaGeometrica()
# forma_geometrica1.descriere()

'''
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
'''

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        super().__init__()
        self.latura = latura

# patrat1 = Patrat(4)
# print(patrat1.latura)
# print(patrat1.PI)

'''
ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)
'''

# la cele doua clase copil (patrat si cerc) difera modul de scriere pentru Getter, Setter si Deleter!!!

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        super().__init__()
        self._latura = latura

    # property
    def latura(self):
        return self._latura

    # latura.getter
    def get_latura(self):
        print(f'Getter: latura este {self._latura}')
        return self._latura

    # latura.setter
    def set_latura(self, latura):
        self._latura = latura
        print(f'Setter: latura este {self._latura}')

    # latura.deleter
    def delete_latura(self):
        self._latura = None
        print(f'Deleter: am sters valoarea laturii!')

    def aria(self):
        return self._latura * self._latura

patrat = Patrat(4)
patrat.descriere()
patrat.get_latura()
patrat.set_latura(6)
print(patrat.aria())
patrat.delete_latura()

print(50 * '*')


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        super().__init__()
        self._raza = raza

    @property
    def raza(self):
        return self._raza

    @raza.getter
    def raza(self):
        print(f'Getter: raza este {self._raza}')
        return self._raza

    @raza.setter
    def raza(self, noua_raza):
        print(f'Setter: raza este {noua_raza}')
        self._raza = noua_raza

    @raza.deleter
    def raza(self):
        print('Deleter: am sters valoarea razei!')
        self._raza = None

    def descriere(self):
        print('Eu nu am colturi')

    def aria(self):
        return self.PI * self._raza ** 2

cerc = Cerc(4)
cerc.descriere()
cerc.raza
cerc.raza = 5
print(cerc.aria())
del cerc.raza

'''
POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
'''

#  Obiectele au fost scrise sub fiecare clasa copil.
