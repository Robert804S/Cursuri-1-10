"""
Clasa Masina
Atribute: marca, culoare, motor_pornit, viteza
Metode: start, stop, accelereaza, incetineste, vopseste
"""

class Masina():
    def __init__(self, marca, culoare):
        self.marca = marca
        self.culoare = culoare
        self.motor_pornit = False
        self.viteza = 0

    def prezentare_masina(self):
        print(self.marca, self.culoare, self.motor_pornit, self.viteza)

    def start(self):
        self.motor_pornit = True

    def stop(self):
        self.viteza = 0
        self.motor_pornit = False

    def accelereaza(self, accelereaza_cu):
        if self.motor_pornit == True:
            self.viteza += accelereaza_cu
            print(f'Masina a ajuns la {self.viteza} km/h')
        else:
            print('nu se poate accelera, motorul este oprit')

    def incetineste(self, incetineste_cu):
        if self.motor_pornit == True and self.viteza > 0:
            self.viteza -= incetineste_cu
            print(f'Masina a ajuns la {self.viteza} km/h')
        else:
            print('nu se poate')

    def vopseste(self, culoare):
        self.culoare = culoare


masina_test = Masina('Volvo', 'Albastru')
masina_test.prezentare_masina()
masina_test.accelereaza(30)
masina_test.start()
masina_test.accelereaza(30)
masina_test.accelereaza(70)
# masina_test.stop()
print(masina_test.viteza)
masina_test.incetineste(70)
masina_test.incetineste(30)
masina_test.vopseste('rosu')
print(masina_test.culoare)