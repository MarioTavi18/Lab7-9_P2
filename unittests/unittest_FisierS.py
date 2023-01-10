from unittest import TestCase

from domeniu.probleme import Problema
from domeniu.student import Student
from repository.FisierProblemerepository import FisierProblemerepository
from repository.FisierStudentrepository import FisierStudentrepository


class TestStudentFisier(TestCase):
    def setUp(self) -> None:
        self.FisierS = FisierStudentrepository("C:\\Users\\mario\\Desktop\\Laborator\\Lab7-9 P2\\TestStudent.txt")
        self.FisierP = FisierProblemerepository("C:\\Users\\mario\\Desktop\\Laborator\\Lab7-9 P2\\TestProbleme.txt","C:\\Users\\mario\\Desktop\\Laborator\\Lab7-9 P2\\TestStudent.txt")

        problema = Problema("Lab1", "cheltuieli", "30.12")
        self.FisierP.adaugaProblema(problema)
        student = Student("1", "Bogdan", "315", "-", 0)
        self.FisierS.adaugaStudent(student)
        student = Student("2", "Florin", "234", "-", 0)
        self.FisierS.adaugaStudent(student)
        student = Student("3", "Coman", "515", "-", 0)
        self.FisierS.adaugaStudent(student)
        student = Student("4", "Armando", "782", "-", 0)
        self.FisierS.adaugaStudent(student)
        student = Student("5", "Dica", "132", "-", 0)
        self.FisierS.adaugaStudent(student)
        student = Student("6", "Raul de Ghencea", "678", "-", 0)
        self.FisierS.adaugaStudent(student)

    def test_adaugaStudent(self):
        self.setUp()
        student = Student("7", "Bogdan", "315", "-", 0)
        student1 = Student("8", "Bogdan", "315", "-", 0)
        student2 = Student("9", "Bogdan", "315", "-", 0)
        student3 = Student("10", "Bogdan", "315", "-", 0)
        self.FisierS.adaugaStudent(student)
        self.FisierS.adaugaStudent(student1)
        self.FisierS.adaugaStudent(student2)
        self.FisierS.adaugaStudent(student3)
        studenti = self.FisierS.getAll()
        self.assertTrue(len(studenti) == 10)
        with self.assertRaises(KeyError):
            self.FisierS.adaugaStudent(student1)
        with open('TestStudent.txt', 'r+') as f:
            f.truncate(0)


    def test_modificaStudent(self):
        student = Student("1", "VVVV", 315,"Mate1",3.0)
        self.FisierS.modificaStudent(student)
        studenti = self.FisierS.getAll()
        self.assertTrue(len(studenti) == 10)
        self.assertTrue(studenti[0].getNume() == "VVVV")
        student = Student("11", "VVVV", 315, "MMM", 3.0)
        with self.assertRaises(KeyError):
            self.FisierS.modificaStudent(student)
        with open('TestStudent.txt', 'r+') as f:
            f.truncate(0)


    def test_stergeStudent(self):
        self.FisierS.stergeStudent("2")
        studenti = self.FisierS.getAll()
        self.assertTrue(len(studenti) == 9)
        with self.assertRaises(KeyError):
            self.FisierS.stergeStudent("2")
        with open('TestStudent.txt', 'r+') as f:
            f.truncate(0)


    def test_cautareStudent(self):
        student = self.FisierS.getById("1")
        self.assertTrue(self.FisierS.cautareStudent("1") == student)
        with open('TestStudent.txt', 'r+') as f:
            f.truncate(0)
