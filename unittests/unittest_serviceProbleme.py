from unittest import TestCase

from repository.FisierProblemerepository import FisierProblemerepository
from repository.FisierStudentrepository import FisierStudentrepository
from repository.problemeRepository import ProblemaRepository
from repository.studentRepository import StudentRepository
from service.ProblemeService import ProblemeService



tip = "memorie"
class TestProblemeService(TestCase):
    def setUp(self) -> None:
        fisierS = FisierStudentrepository("student.txt")
        fisierP = FisierProblemerepository("probleme.txt", "student.txt")
        self.problemaRepository = ProblemaRepository()
        self.studentRepository = StudentRepository()
        self.problemaService = ProblemeService(self.problemaRepository, self.studentRepository, fisierP, fisierS)
        self.problemaService.adaugaProblema("Lab1", "Suma1", "Maine", tip)
        self.problemaService.adaugaProblema("Lab2", "Suma2", "Maine", tip)
        self.problemaService.adaugaProblema("Lab3", "Suma3", "Maine", tip)
        self.problemaService.adaugaProblema("Lab4", "Suma4", "Maine", tip)
        self.problemaService.adaugaProblema("Lab5", "Suma5", "Maine", tip)

    def test_getAllproblems(self):
        self.setUp()
        probleme = self.problemaService.getALLProbleme(tip)
        self.assertTrue(len(probleme) == 5)

    def test_cautareproblema(self):
        self.setUp()
        self.assertTrue(self.problemaService.cautareProblema("Lab1",tip).GetDescriere() == "Suma1")
        self.assertTrue(self.problemaService.cautareProblema("Lab2",tip).GetDescriere() == "Suma2")
        with self.assertRaises(KeyError):
            self.problemaService.cautareProblema("Lab55",tip)

    def testAdaugaProblemaService(self):
        self.setUp()
        self.problemaService.adaugaProblema("Lab6", "Suma", "Maine", tip)
        probleme = self.problemaService.getALLProbleme(tip)
        self.assertTrue(len(probleme) == 6)
        with self.assertRaises(KeyError):
            self.problemaService.adaugaProblema("Lab1", "Suma", "Maine",tip)


    def testModificaProblemaService(self):
        self.problemaService.modificaProblema("Lab1", "SumaNoua", "Maine", tip)
        probleme = self.problemaService.getALLProbleme(tip)
        self.assertTrue(probleme[0].GetDescriere() == "SumaNoua")
        self.assertTrue(len(probleme) == 6)
        with self.assertRaises(KeyError):
            self.problemaService.modificaProblema("Lab111", "Suma", "Maine", tip)


    def testStergeProblemaService(self):
        self.problemaService.stergeProblema("Lab5", tip)
        probleme = self.problemaService.getALLProbleme(tip)
        self.assertTrue(len(probleme) == 5)
        with self.assertRaises(KeyError):
            self.problemaService.stergeProblema("Lab111", tip)