from unittest import TestCase

from domeniu.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("1", "Ana", "312", "-", 0)
        self.student1 = Student("3", "Vasile", "721", "-", 0)

    def test_getNota(self):
        self.setUp()
        self.assertTrue(self.student.getNota() == 0)

    def test_getLucrare(self):
        self.setUp()
        self.assertTrue(self.student.getLucrare() =="-")

    def test_getStudentID(self):
        self.setUp()
        self.assertTrue(self.student.getStudentID() == "1")

    def test_getNume(self):
        self.setUp()
        self.assertTrue(self.student.getNume() == "Ana")

    def test_getGrup(self):
        self.setUp()
        self.assertTrue(self.student.getGrup() == "312")

    def test_setStudentID(self):
        self.setUp()
        self.student1.setStudentID("2")
        self.assertTrue(self.student1.getStudentID() == "2")

    def test_setLucrare(self):
        self.setUp()
        self.student1.setLucrare("-")
        self.assertTrue(self.student1.getLucrare() == "-")

    def test_setNota(self):
        self.setUp()
        self.student1.setNota(0)
        self.assertTrue(self.student1.getNota() == 0)

    def test_setGrup(self):
        self.setUp()
        self.student1.setGrup("278")
        self.assertTrue(self.student1.getGrup() == "278")

    def test_setNume(self):
        self.setUp()
        self.student1.setNume("George")
        self.assertTrue(self.student1.getNume() == "George")
