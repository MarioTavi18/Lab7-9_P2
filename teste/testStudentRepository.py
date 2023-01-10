from domeniu.probleme import Problema
from domeniu.student import Student
from repository.studentRepository import StudentRepository
from repository.problemeRepository import ProblemaRepository

class TesteReprS:
    def __init__(self):
        ...

    def testAdaugaStudentRepository(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        student = Student("1","Vlad",315,"-",0.0)

        studentRepository.adaugaStudent(student)

        studenti = studentRepository.getAll()
        assert len(studenti) == 1
        assert studenti[0].getStudentID() == "1"

        try:
            studentRepository.adaugaStudent((student))

        except KeyError:
            ...

    def testModificaStudentRepository(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        student = Student("1", "Vlad", 315,"Mate1",3.0)
        studentNou1 = Student("1", "Ana", 313,"Mate2",10.0)
        studentNou2 = Student("2", "Paul", 315,"Mate3",4.0)
        studentRepository.adaugaStudent(student)

        studentRepository.modificaStudent(studentNou1)
        studenti = studentRepository.getAll()
        assert studenti[0].getNume() == "Ana"

        try:
            studentRepository.modificaStudent(studentNou2)

        except KeyError:
            ...

    def testStergeStudentRepository(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        student = Student("1", "Vlad", 315,"Mate",3.0)
        studentRepository.adaugaStudent(student)

        studentRepository.stergeStudent("1")
        studenti = studentRepository.getAll()
        assert len(studenti) == 0
        try:
            studentRepository.stergeStudent("!")

        except KeyError:
            ...

    def testCautareStudentRepository(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        student = Student("1", "Vlad", 315, "Mate", 0)
        studentRepository.adaugaStudent(student)
        student = Student("2", "Ana",333,"-",0)
        studentRepository.adaugaStudent(student)
        studenti = studentRepository.getAll()
        assert len(studenti) == 2
        try:
            studentRepository.cautareStudent("3")

        except KeyError:
            ...



