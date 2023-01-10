from domeniu.student import Student

class TesteStudent:
    def __init__(self):
        ...


    def testStudent(self):
        student = Student("1","Vlad","315","Mate","3.0")

        assert student.getStudentID() == "1"
        assert student.getNume() == "Vlad"
        assert student.getGrup() == "315"
        assert student.getLucrare() == "Mate"
        assert student.getNota() == "3.0"

    def testStudentSetteri(self):
        student = Student("1", "Vlad", "315","Mate","3.0")

        student.setStudentID("1")
        assert student.getStudentID() == "1"

        student.setNume("Vlad")
        assert student.getNume() == "Vlad"

        student.setGrup("315")
        assert student.getGrup() == "315"

        student.setLucrare("Mate")
        assert student.getLucrare() == "Mate"

        student.setNota("3.0")
        assert student.getNota() == "3.0"