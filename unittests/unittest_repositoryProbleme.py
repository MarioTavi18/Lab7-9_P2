from unittest import TestCase

from domeniu.probleme import Problema
from repository.problemeRepository import ProblemaRepository
from repository.studentRepository import StudentRepository


class TestProblemeRepository(TestCase):
    def setUp(self) -> None:
        self.problemaRepository = ProblemaRepository()
        self.studentRepository = StudentRepository()

        problema = Problema("Lab1", "cheltuieli1", "30.12")
        self.problemaRepository.adaugaProblema(problema)
        problema = Problema("Lab2", "cheltuieli2", "30.12")
        self.problemaRepository.adaugaProblema(problema)
        problema = Problema("Lab3", "cheltuieli3", "30.12")
        self.problemaRepository.adaugaProblema(problema)
        problema = Problema("Lab4", "cheltuieli4", "30.12")
        self.problemaRepository.adaugaProblema(problema)
        problema = Problema("Lab5", "cheltuieli5", "30.12")
        self.problemaRepository.adaugaProblema(problema)

    def test_GetByNrProb(self):
        self.setUp()
        problema = self.problemaRepository.getByNr("Lab1")
        self.assertTrue(problema.GetNrProb() == "Lab1")
        with self.assertRaises(ValueError):
            problema = self.problemaRepository.getByNr("lab111")
            raise ValueError

    def test_GetAll(self):
        self.setUp()
        probleme = self.problemaRepository.getAll()
        self.assertTrue(probleme[0].GetNrProb() == "Lab1")
        self.assertTrue(probleme[1].GetNrProb() == "Lab2")
        self.assertTrue(probleme[2].GetNrProb() == "Lab3")
        self.assertTrue(probleme[3].GetNrProb() == "Lab4")
        self.assertTrue(probleme[4].GetNrProb() == "Lab5")

    def test_adaugaProblema(self):
        problema = Problema("Lab6", "cheltuieli1", "30.12")
        self.problemaRepository.adaugaProblema(problema)
        probleme = self.problemaRepository.getAll()
        self.assertTrue(len(probleme) == 6)
        with self.assertRaises(KeyError):
            self.problemaRepository.adaugaProblema(problema)

    def test_modificaProblema(self):
        problema = Problema("Lab1", "cheltuieliNOI", "30.12")
        self.problemaRepository.modificaProblema(problema)
        probleme = self.problemaRepository.getAll()
        self.assertTrue(len(probleme) == 6)
        self.assertTrue(probleme[0].GetDescriere() == "cheltuieliNOI")
        problema = Problema("Lab122", "cheltuieliNOI", "30.12")
        with self.assertRaises(KeyError):
            self.problemaRepository.adaugaProblema(problema)
            raise KeyError

    def test_stergeProblema(self):
        self.problemaRepository.stergeProblema("Lab2")
        probleme = self.problemaRepository.getAll()
        self.assertTrue(len(probleme) == 6)
        with self.assertRaises(KeyError):
            self.problemaRepository.stergeProblema("Lab2")
            raise KeyError

    def test_cautareProblema(self):
        problema = self.problemaRepository.getByNr("Lab1")
        self.assertTrue(self.problemaRepository.cautareProblema("Lab1") == problema)
