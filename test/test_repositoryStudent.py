from unittest import TestCase
from domeniu.probleme import Problema
from domeniu.student import Student
from repository.problemeRepository import ProblemaRepository
from repository.studentRepository import StudentRepository

class TestStudentRepository(TestCase):
    def setUp(self) -> None:
        self.problemaRepository = ProblemaRepository()
        self.studentRepository = StudentRepository()

        problema = Problema("Lab1", "cheltuieli", "30.12")
        self.problemaRepository.adaugaProblema(problema)
        student = Student("1", "Bogdan", "315", "-", 0)
        self.studentRepository.adaugaStudent(student)
        student = Student("2", "Florin", "234", "-", 0)
        self.studentRepository.adaugaStudent(student)
        student = Student("3", "Coman", "515", "-", 0)
        self.studentRepository.adaugaStudent(student)
        student = Student("4", "Armando", "782", "-", 0)
        self.studentRepository.adaugaStudent(student)
        student = Student("5", "Dica", "132", "-", 0)
        self.studentRepository.adaugaStudent(student)
        student = Student("6", "Raul de Ghencea", "678", "-", 0)
        self.studentRepository.adaugaStudent(student)

    def test_GetById(self):
        self.setUp()
        student = self.studentRepository.getById("1")
        self.assertTrue(student.getStudentID() == "1")
        with self.assertRaises(ValueError):
            student = self.studentRepository.getById("50")
            raise ValueError

    def test_GetAll(self):
        studenti = self.studentRepository.getAll()
        self.assertTrue(studenti[0].getStudentID() == "1")
        self.assertTrue(studenti[1].getStudentID() == "2")
        self.assertTrue(studenti[2].getStudentID() == "3")
        self.assertTrue(studenti[3].getStudentID() == "4")
        self.assertTrue(studenti[4].getStudentID() == "5")
        self.assertTrue(studenti[5].getStudentID() == "6")

    def test_adaugaStudent(self):
        student = Student("7", "Bogdan", "315", "-", 0)
        student1 = Student("8", "Bogdan", "315", "-", 0)
        student2 = Student("9", "Bogdan", "315", "-", 0)
        student3 = Student("10", "Bogdan", "315", "-", 0)
        self.studentRepository.adaugaStudent(student)
        self.studentRepository.adaugaStudent(student1)
        self.studentRepository.adaugaStudent(student2)
        self.studentRepository.adaugaStudent(student3)
        studenti = self.studentRepository.getAll()
        self.assertTrue(len(studenti) == 10)
        with self.assertRaises(KeyError):
            self.studentRepository.adaugaStudent(student1)

    def test_modificaStudent(self):
        student = Student("1", "VVVV", 315,"Mate1",3.0)
        self.studentRepository.modificaStudent(student)
        studenti = self.studentRepository.getAll()
        print(len(studenti))
        self.assertTrue(len(studenti) == 6)
        self.assertTrue(studenti[0].getNume() == "VVVV")
        student = Student("11", "VVVV", 315, "MMM", 3.0)
        with self.assertRaises(KeyError):
            self.studentRepository.modificaStudent(student)

    def test_stergeStudent(self):
        self.studentRepository.stergeStudent("2")
        studenti = self.studentRepository.getAll()
        self.assertTrue(len(studenti) == 5)
        with self.assertRaises(KeyError):
            self.studentRepository.stergeStudent("2")

    def test_cautareStudent(self):
        student = self.studentRepository.getById("1")
        self.assertTrue(self.studentRepository.cautareStudent("1") == student)