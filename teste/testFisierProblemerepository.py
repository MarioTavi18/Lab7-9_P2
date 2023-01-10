from domeniu.probleme import Problema
from domeniu.student import Student
from repository.FisierProblemerepository import FisierProblemerepository
from repository.FisierStudentrepository import FisierStudentrepository

from repository.problemeRepository import ProblemaRepository
from repository.studentRepository import StudentRepository

class FileReprP:
    def __init__(self):
        ...

    def testAdaugaP(self):
        fisierS = FisierStudentrepository("TestStudent.txt")
        fisierP = FisierProblemerepository("TestProbleme.txt", "TestStudent.txt")
        problema = Problema("Lab1", "Scrie o suma", "12.02.2022")
        fisierP.adauga(problema)

        probleme=fisierP.getAll()
        assert len(probleme) == 1
        assert probleme[0].GetNrProb() == "Lab1"

        try:
            fisierP.adauga(problema)

        except KeyError:
            ...
        with open('TestProbleme.txt','r+') as f:
            f.truncate(0)

    def testModificaP(self):
        fisierP = FisierProblemerepository("TestProbleme.txt", "TestStudent.txt")
        problema = Problema("Lab1", "Scrie o suma", "12.02.2022")
        problemaNou1 = Problema("Lab1", "Scrie un produs", "13.03.2023")
        problemaNou2 = Problema("Lab3", "Scrie o suma", "12.02.2022")
        fisierP.adauga(problema)
        fisierP.adauga(problemaNou2)

        fisierP.modifica(problemaNou1)
        probleme = fisierP.getAll()
        assert len(probleme) == 2
        assert probleme[0].GetDescriere() == "Scrie un produs"

        try:
            fisierP.modifica(problemaNou2)

        except KeyError:
            ...
        with open('TestProbleme.txt','r+') as f:
            f.truncate(0)

    def testStergeP(self):
        fisierP = FisierProblemerepository("TestProbleme.txt", "TestStudent.txt")
        fisierS = FisierStudentrepository("TestStudent.txt")
        problema = Problema("Lab4", "Scrie o suma", "12.02.2022")
        fisierP.adauga(problema)
        problema = Problema("Lab5", "Scrie o suma", "12.02.2022")
        fisierP.adauga(problema)
        student = Student("12", "Vlad", 315, "Lab4", 3.0)
        fisierS.adauga(student)
        student = Student("13", "Vlad", 315, "Lab5", 3.0)
        fisierS.adauga(student)

        fisierP.sterge("Lab4")
        probleme = fisierP.getAll()
        assert len(probleme) == 1
        try:
            fisierP.sterge("!")
        except KeyError:
            ...
        with open('TestProbleme.txt','r+') as f:
            f.truncate(0)
        with open('TestStudent.txt','r+') as f:
            f.truncate(0)

    def testCautareP(self):
        fisierP = FisierProblemerepository("TestProbleme.txt", "TestStudent.txt")
        problema = Problema("Lab1", "Scrie o suma", "12.02.2022")
        fisierP.adauga(problema)
        try:
            fisierP.cautare("Lab3")

        except KeyError:
            ...
        with open('TestProbleme.txt','r+') as f:
            f.truncate(0)