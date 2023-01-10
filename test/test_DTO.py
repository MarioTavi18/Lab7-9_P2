from unittest import TestCase

from domeniu.DTO import StudentSub5, StudentNumaiGrup


class TestStudentSub5(TestCase):
    def setUp(self) -> None:
        self.studentN = StudentSub5("Ana",4)
        self.student1N = StudentSub5("Vasile",3)

    def test_getNota(self):
        self.setUp()
        self.assertTrue(self.studentN.getNota() == 4)
        self.assertTrue(self.student1N.getNota() == 3)

    def test_getNume(self):
        self.setUp()
        self.assertTrue(self.studentN.getNume() == "Ana")
        self.assertTrue(self.student1N.getNume() == "Vasile")

    def test_setNota(self):
        self.setUp()
        self.studentN.setNota("2")
        self.assertTrue(self.studentN.getNota() == "2")

    def test_setNume(self):
        self.setUp()
        self.student1N.setNume("George")
        self.assertTrue(self.student1N.getNume() == "George")

class TestStudentNumaiGrup(TestCase):
    def setUp(self) -> None:
        self.studentG = StudentNumaiGrup("Ana", "312")
        self.student1G = StudentNumaiGrup("Vasile", "721")

    def test_getNume(self):
        self.setUp()
        self.assertTrue(self.studentG.getNume() == "Ana")
        self.assertTrue(self.student1G.getNume() == "Vasile")

    def test_getGrup(self):
        self.setUp()
        self.assertTrue(self.studentG.getGrup() == "312")
        self.assertTrue(self.student1G.getGrup() == "721")

    def test_setNume(self):
        self.setUp()
        self.student1G.setNume("George")
        self.assertTrue(self.student1G.getNume() == "George")

    def test_setGrup(self):
        self.setUp()
        self.student1G.setGrup("278")
        self.assertTrue(self.student1G.getGrup() == "278")
