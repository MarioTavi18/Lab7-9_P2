from unittest import TestCase

from domeniu.probleme import Problema
from repository.FisierProblemerepository import FisierProblemerepository
from repository.FisierStudentrepository import FisierStudentrepository


class TestProblemaFisier(TestCase):
    def setUp(self) -> None:
        self.FisierS = FisierStudentrepository("TestStudent.txt")
        self.FisierP = FisierProblemerepository("TestProbleme.txt","TestStudent.txt")

        problema = Problema("Lab1", "cheltuieli1", "30.12")
        self.FisierP.adaugaProblema(problema)
        problema = Problema("Lab2", "cheltuieli2", "30.12")
        self.FisierP.adaugaProblema(problema)
        problema = Problema("Lab3", "cheltuieli3", "30.12")
        self.FisierP.adaugaProblema(problema)
        problema = Problema("Lab4", "cheltuieli4", "30.12")
        self.FisierP.adaugaProblema(problema)
        problema = Problema("Lab5", "cheltuieli5", "30.12")
        self.FisierP.adaugaProblema(problema)

    def test_adaugaProbleme(self):
        self.setUp()
        problema = Problema("Lab6", "cheltuieli1", "30.12")
        self.FisierP.adaugaProblema(problema)
        probleme = self.FisierP.getAll()
        self.assertTrue(len(probleme) == 6)
        with self.assertRaises(KeyError):
            self.FisierP.adaugaProblema(problema)
        with open('TestProbleme.txt', 'r+') as f:
            f.truncate(0)


    def test_modificaProblema(self):
        problema = Problema("Lab1", "cheltuieliNOI", "30.12")
        self.FisierP.modificaProblema(problema)
        probleme = self.FisierP.getAll()
        self.assertTrue(len(probleme) == 6)
        self.assertTrue(probleme[0].GetDescriere() == "cheltuieliNOI")
        problema = Problema("Lab1111", "cheltuieliNOI", "30.12")
        with self.assertRaises(KeyError):
            self.FisierP.modificaProblema(problema)
        with open('TestProbleme.txt', 'r+') as f:
            f.truncate(0)


    def test_stergeProblema(self):
        self.FisierP.stergeProblema("Lab2")
        probleme = self.FisierP.getAll()
        self.assertTrue(len(probleme) == 5)
        with self.assertRaises(KeyError):
            self.FisierP.stergeProblema("Lab2")
        with open('TestProbleme.txt', 'r+') as f:
            f.truncate(0)


    def test_cautareProblema(self):
        problema = self.FisierP.getByNr("Lab1")
        self.assertTrue(self.FisierP.cautareProblema("Lab1") == problema)
        with open('TestProbleme.txt', 'r+') as f:
            f.truncate(0)
