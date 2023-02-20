'''
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
'''

# class Cerc():
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descriere_cerc(self):
#         print(f'culoarea: {self.culoare}, raza: {self.raza}')
#
#     def aria(self):
#         aria = 3.14 * self.raza ** 2
#         return aria
#
#     def diametru(self):
#         diametru = 2 * self.raza
#         return diametru
#
#     def circumferinta(self):
#         circumferinta = 2 * 3.14 * self.raza
#         return circumferinta
#
# cerc_1 = Cerc(4, 'Albastru')
# cerc_2 = Cerc(6, 'Rosu')

# cerc_1.descriere_cerc()
# print(cerc_1.aria())
# print(cerc_1.diametru())
# print(cerc_1.circumferinta())
#
# print(50 * '*')

# cerc_2.descriere_cerc()
# print(cerc_2.aria())
# print(cerc_2.diametru())
# print(cerc_2.circumferinta())

'''
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
'''

# class Dreptunghi():
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descriere(self):
#         print(f'lungimea: {self.lungime}, latime: {self.latime}, culoare: {self.culoare}')
#
#     def aria(self):
#         aria = self.lungime * self.latime
#         return aria
#
#     def perimetrul(self):
#         perimetrul = (self.lungime + self.latime) * 2
#         return perimetrul
#
#     def schimba_culoarea(self, culoarea_noua):
#         self.culoare = culoarea_noua
#
# dreptunghi_1 = Dreptunghi(7, 3, 'verde')
# dreptunghi_2 = Dreptunghi(10, 5, 'galben')
#
# dreptunghi_1.descriere()
# print(dreptunghi_1.aria())
# print(dreptunghi_1.perimetrul())
# dreptunghi_1.schimba_culoarea('portocaliu')
# dreptunghi_1.descriere()
#
# print(50 * '*')
#
# dreptunghi_2.descriere()
# print(dreptunghi_2.aria())
# print(dreptunghi_2.perimetrul())
# dreptunghi_2.schimba_culoarea('roz')
# dreptunghi_2.descriere()

'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''

# class Angajat():
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descriere(self):
#         print(f'nume: {self.nume}, prenume: {self.prenume}, salariu: {self.salariu}')
#
#     def nume_complet(self):
#         return self.nume + ' ' + self.prenume
#
#     def salariu_lunar(self):
#         return self.salariu
#
#     def salariu_anual(self):
#         return self.salariu_lunar() * 12
#
#     def marire_salariu(self):
#         procent_marire_salariala = self.salariu_lunar() / 100 * (100 + int(input('Ce procentaj va avea cresterea salariala? - ')))
#         salariul_dupa_marirea_salariala = procent_marire_salariala
#         return salariul_dupa_marirea_salariala
#
# angajat_1 = Angajat('Sima', 'Doru', 4000)
# angajat_2 = Angajat('Restantia', 'Ovidiu', 5000)
#
# angajat_1.descriere()
# print(angajat_1.nume_complet())
# print(angajat_1.salariu_lunar())
# print(angajat_1.salariu_anual())
# print(angajat_1.marire_salariu())
#
# print(50 * '*')
#
# angajat_2.descriere()
# print(angajat_2.nume_complet())
# print(angajat_2.salariu_lunar())
# print(angajat_2.salariu_anual())
# print(angajat_2.marire_salariu())

'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
'''

class Cont():
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self):
        numar_incercari = 3
        while numar_incercari != 0:
            suma_retrasa = int(input('Introduceti suma pe care doriti sa o debitati: '))
            self.sold = 7000
            if suma_retrasa not in range(0, self.sold + 1):
                self.sold = self.sold - suma_retrasa
            if self.sold < 0:
                numar_incercari = numar_incercari - 1
                print(f'Suma pe care doresti sa o retragi este mai mare decat suma din cont, mai aveti {numar_incercari} incercari')
            if numar_incercari == 0:
                print('Nu mai puteti face retrageri, cardul este blocat')
                break
            if suma_retrasa in range(0, self.sold + 1):
                self.sold = self.sold - suma_retrasa
                print(f'Soldul in urma debitarii este {self.sold}')
                break

    def creditare_sold(self):
        self.sold = self.sold + int(input('Introduceti suma pe care doriti sa o depuneti in cont: '))
        print(f'Soldul in urma depunerii este {self.sold}')

persoana_1 = Cont(1234, 'Fogoros Florin', 7000)
persoana_2 = Cont(1213, 'Asaftei Mihai', 9000)

persoana_1.afisare_sold()
persoana_1.debitare_cont()
# persoana_1.creditare_sold()

print(50 * '*')
#
# persoana_2.afisare_sold()
# persoana_2.debitare_cont()
# persoana_2.creditare_sold()
