from domeniu.student import Student
from repository.FisierStudentrepository import FisierStudentrepository

tip ="fisier"
class FileReprS:
    def __init__(self):
        ...

    def testAdaugaS(self):
        fisierS = FisierStudentrepository("TestStudent.txt")
        student = Student("1","Vlad",315,"-",0.0)
        fisierS.adauga(student)

        studenti = fisierS.getAll()
        assert len(studenti) == 1
        assert studenti[0].getStudentID() == "1"

        try:
            fisierS.adauga(student)

        except KeyError:
            ...
        with open('TestStudent.txt','r+') as f:
            f.truncate(0)

    def testModificaS(self):
        fisierS = FisierStudentrepository("TestStudent.txt")
        student = Student("1", "Vlad", 315,"Mate1",3.0)
        studentNou1 = Student("1", "Ana", 313,"Mate2",10.0)
        studentNou2 = Student("2", "Paul", 315,"Mate3",4.0)
        fisierS.adauga(student)
        fisierS.adauga(studentNou2)

        fisierS.modifica(studentNou1)
        studenti = fisierS.getAll()
        assert studenti[0].getNume() == "Ana"

        try:
            fisierS.modifica(studentNou2)
        except KeyError:
            raise KeyError
        with open('TestStudent.txt','r+') as f:
            f.truncate(0)

    def testStergeS(self):
        fisierS = FisierStudentrepository("TestStudent.txt")
        student = Student("1", "Vlad", 315,"Mate",3.0)
        fisierS.adauga(student)
        student = Student("2", "Vlad", 315, "Mate", 3.0)
        fisierS.adauga(student)

        fisierS.sterge("1")
        studenti = fisierS.getAll()
        assert len(studenti) == 1
        try:
            fisierS.sterge("!")

        except KeyError:
            ...
        with open('TestStudent.txt','r+') as f:
            f.truncate(0)

    def testCautareS(self):
        fisierS = FisierStudentrepository("TestStudent.txt")
        student = Student("1", "Vlad", 315, "Mate", 0)
        fisierS.adauga(student)
        student = Student("2", "Ana",333,"-",0)
        fisierS.adauga(student)
        studenti = fisierS.getAll()
        assert len(studenti) == 2
        try:
            fisierS.cautare("3")

        except KeyError:
            ...
        with open('TestStudent.txt','r+') as f:
            f.truncate(0)