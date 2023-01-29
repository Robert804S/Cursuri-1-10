"""
Clasa CursProgramare
Atribute: companie, nume_curs, numar_locuri_maxime, studenti
Metode: inscriere_student, descriere_curs, get_locuri_disponibile
"""
from persoana import Persoana


class CursProgramare():
    def __init__(self, companie, nume_curs, nr_locuri_max):
        self.companie = companie
        self.nume_curs = nume_curs
        self.nr_locuri_max = nr_locuri_max
        self.studenti = []

    def inscriere_student(self, nume_student):
        if self.get_locuri_disponibile() > 0:
            self.studenti.append(nume_student)
        else:
            print('nu mai sunt locuri disponibile')

    def descriere_curs(self):
        print(f'{self.companie} - {self.nume_curs}')
        print(30 * '*')
        if len(self.studenti) > 0:
            print('Lista studenti: ')
            for student in self.studenti:
                print(student.nume, student.prenume)
        else:
            print('nu sunt studenti inscrisi')

    def get_locuri_disponibile(self):
        return self.nr_locuri_max - len(self.studenti)

student_1 = Persoana('Matei', 'Vlad', 33)
curs_python = CursProgramare('IT Factory', 'Introducere in Python', 10)
curs_python.descriere_curs()
curs_python.inscriere_student(student_1)
curs_python.descriere_curs()
student_2 = Persoana('Luiza', 'Diana', 29)
curs_python.descriere_curs()
curs_python.descriere_curs()