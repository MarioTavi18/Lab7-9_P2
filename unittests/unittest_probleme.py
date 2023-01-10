from unittest import TestCase

from domeniu.probleme import Problema


class TestProbleme(TestCase):
    def setUp(self) -> None:
        self.problema = Problema("Lab1", "cheltuieli", "30.08")
        self.problema1 = Problema("Lab2", "patrate", "01.02")

    def test_getNrProb(self):
        self.setUp()
        self.assertTrue(self.problema.GetNrProb() == "Lab1")

    def test_getDescriere(self):
        self.setUp()
        self.assertTrue(self.problema.GetDescriere() == "cheltuieli")

    def test_getDeadline(self):
        self.setUp()
        self.assertTrue(self.problema.GetDeadline() == "30.08")

    def test_setNrProb(self):
        self.setUp()
        self.problema1.SetNrProb("Lab2")
        self.assertTrue(self.problema1.GetNrProb() == "Lab2")

    def test_setDescriere(self):
        self.setUp()
        self.problema1.SetDescriere("triunghiuri")
        self.assertTrue(self.problema1.GetDescriere() == "triunghiuri")

    def test_setDeadline(self):
        self.setUp()
        self.problema1.SetDeadline("13.04")
        self.assertTrue(self.problema1.GetDeadline() == "13.04")