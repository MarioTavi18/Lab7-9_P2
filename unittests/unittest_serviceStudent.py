from unittest import TestCase

from domeniu.probleme import Problema
from repository.FisierProblemerepository import FisierProblemerepository
from repository.FisierStudentrepository import FisierStudentrepository
from repository.problemeRepository import ProblemaRepository
from repository.studentRepository import StudentRepository
from service.ProblemeService import ProblemeService
from service.StudentService import StudentService

class TestStudentService(TestCase):
    def setUp(self) -> None:
            fisierS = FisierStudentrepository("unittests/studentU.txt")
            fisierP = FisierProblemerepository("unittests/problemeU.txt", "unittests/studentU.txt")
            self.problemaRepository = ProblemaRepository()
            self.studentRepository = StudentRepository()
            self.studentService = StudentService(self.studentRepository, self.problemaRepository, fisierS,fisierP)
            problema = Problema("Lab1", "cheltuieli", "30.12")
            self.problemaRepository.adaugaProblema(problema)

            self.studentService.adaugaStudent("1", "Bogdan", "315", "-", 0,"memorie")
            self.studentService.adaugaStudent("2", "Florin", "234", "-", 0,"memorie")
            self.studentService.adaugaStudent("3", "Coman", "515", "-", 0,"memorie")
            self.studentService.adaugaStudent("4", "Armando", "782", "-", 0,"memorie")
            self.studentService.adaugaStudent("5", "Dica", "132", "-", 0,"memorie")
            self.studentService.adaugaStudent("6", "Raul de Ghencea", "678", "-", 0,"memorie")


            self.studentService.Asignare("1", "Lab1","memorie")
            self.studentService.Asignare("2", "Lab1","memorie")
            self.studentService.Asignare("3", "Lab1","memorie")
            self.studentService.Asignare("4", "Lab1","memorie")
            self.studentService.Asignare("5", "Lab1","memorie")
            self.studentService.Asignare("6", "Lab1","memorie")

            self.studentService.Notare("1", 10,"memorie")
            self.studentService.Notare("2", 1,"memorie")
            self.studentService.Notare("3", 10,"memorie")
            self.studentService.Notare("4", 8,"memorie")
            self.studentService.Notare("5", 7,"memorie")
            self.studentService.Notare("6", 4,"memorie")

    def test_getAllstudenti(self):
            self.setUp()
            studenti = self.studentService.getALLStudenti("memorie")
            self.assertTrue(len(studenti) == 6)
            self.assertTrue(studenti[0].getNume() == "Bogdan")
            self.assertTrue(studenti[1].getNume() == "Florin")
            self.assertTrue(studenti[2].getNume() == "Coman")
            self.assertTrue(studenti[3].getNume() == "Armando")

    def test_cautareStudent(self):
            self.setUp()
            test = self.studentService.cautareStudent("3","memorie")
            self.assertTrue(test.getGrup() == "515")
            self.assertTrue(test.getNume() == "Coman")
            with self.assertRaises(KeyError):
                self.studentService.cautareStudent("9","memorie")

    def test_adaugaStudent(self):
            self.setUp()
            studenti = self.studentService.getALLStudenti("memorie")
            self.assertTrue(len(studenti) == 6)
            self.assertTrue(studenti[0].getNume() == "Bogdan")
            self.assertTrue(studenti[1].getNume() == "Florin")
            self.assertTrue(studenti[2].getNume() == "Coman")
            self.assertTrue(studenti[3].getNume() == "Armando")
            with self.assertRaises(ValueError):
                self.studentService.adaugaStudent("15", "Daniel", "612", "-", 0,"memorie")
                raise ValueError
            with self.assertRaises(ValueError):
                self.studentService.adaugaStudent("16", "Oscar", "431", "-", 0,"memorie")
                raise ValueError

    def test_modificastudent(self):
                self.setUp()
                self.studentService.modificaStudent("2", "Marin", "314", "-", 0, "memorie")
                studenti = self.studentService.getALLStudenti("memorie")
                self.assertTrue(studenti[1].getNume() == "Marin")
                self.assertTrue(studenti[1].getGrup() == "314")
                with self.assertRaises(ValueError):
                    self.studentService.modificaStudent("1", "Daniel", "612", "Lab1", 2,"memorie")
                    raise ValueError
                with self.assertRaises(ValueError):
                    self.studentService.modificaStudent("1", "Oscar", "431", "Lab1", 10,"memorie")
                    raise ValueError

    def test_stergestudent(self):
            self.setUp()
            studenti = self.studentService.getALLStudenti("memorie")
            self.assertTrue(len(studenti) == 6)
            self.studentService.stergeStudent("6","memorie")
            studenti = self.studentService.getALLStudenti("memorie")
            self.assertTrue(len(studenti) == 5)

    def test_Asignare(self):
            self.setUp()
            studenti = self.studentService.getALLStudenti("memorie")
            self.assertTrue(studenti[0].getLucrare() == "Lab1")
            self.assertTrue(studenti[1].getLucrare() == "Lab1")
            self.assertTrue(studenti[2].getLucrare() == "Lab1")
            with self.assertRaises(KeyError):
                self.studentService.Asignare("16", 1,"memorie")
            with self.assertRaises(KeyError):
                self.studentService.Asignare("4", 2,"memorie")

    def test_notarestudent(self):
            self.setUp()
            studenti = self.studentService.getALLStudenti("memorie")
            self.assertTrue(studenti[0].getNota() == 10)
            self.assertTrue(studenti[1].getNota() == 1)
            self.assertTrue(studenti[2].getNota() == 10)
            self.assertTrue(studenti[3].getNota() == 8)
            self.assertTrue(studenti[4].getNota() == 7)
            self.assertTrue(studenti[5].getNota() == 4)
            with self.assertRaises(KeyError):
                self.studentService.Notare("16", 1,"memorie")
            self.studentService.adaugaStudent("8", "Raul de Ghencea", "678", "-", 0,"memorie")
            with self.assertRaises(KeyError):
                self.studentService.Notare("8", 10,"memorie")


    def test_ordonarestudentnota(self):
            self.setUp()
            studenti = self.studentService.ordonareNota("memorie")
            self.assertTrue(studenti[0].getNota() == 1.0)
            self.assertTrue(studenti[1].getNota() == 4.0)
            self.assertTrue(studenti[2].getNota() == 7.0)
            self.assertTrue(studenti[3].getNota() == 8.0)
            self.assertTrue(studenti[4].getNota() == 10.0)
            self.assertTrue(studenti[5].getNota() == 10.0)
            self.studentService.stergeStudent("1","memorie")
            self.studentService.stergeStudent("2","memorie")
            self.studentService.stergeStudent("3","memorie")
            self.studentService.stergeStudent("4","memorie")
            self.studentService.stergeStudent("5","memorie")
            self.studentService.stergeStudent("6","memorie")
            with self.assertRaises(KeyError):
                self.studentService.ordonareNota("memorie")
                raise KeyError

    def test_ordonaresub5(self):
            self.setUp()
            studenti = self.studentService.Sub5("memorie")
            self.assertTrue(studenti[0].getNota() == 1)
            self.assertTrue(studenti[1].getNota() == 4)

            self.studentService.stergeStudent("1","memorie")
            self.studentService.stergeStudent("2","memorie")
            self.studentService.stergeStudent("3","memorie")
            self.studentService.stergeStudent("4","memorie")
            self.studentService.stergeStudent("5","memorie")
            self.studentService.stergeStudent("6","memorie")
            with self.assertRaises(ValueError):
                self.studentService.Sub5("memorie")
                raise ValueError


    def test_ordonareNumaiGrup(self):
        self.setUp()
        studenti = self.studentService.NumaiGrup("memorie")
        self.assertTrue(studenti[0].getGrup() == "782")
        self.assertTrue(studenti[1].getGrup() == "315")

        self.studentService.stergeStudent("1","memorie")
        self.studentService.stergeStudent("2","memorie")
        self.studentService.stergeStudent("3","memorie")
        self.studentService.stergeStudent("4","memorie")
        self.studentService.stergeStudent("5","memorie")
        self.studentService.stergeStudent("6","memorie")
        with self.assertRaises(ValueError):
            self.studentService.NumaiGrup("memorie")
            raise ValueError