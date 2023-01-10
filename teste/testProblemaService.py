from repository.FisierProblemerepository import FisierProblemerepository
from repository.FisierStudentrepository import FisierStudentrepository
from repository.problemeRepository import ProblemaRepository
from repository.studentRepository import StudentRepository
from service.ProblemeService import ProblemeService
from service.StudentService import StudentService

fisierS = FisierStudentrepository("TestStudent.txt")
fisierP = FisierProblemerepository("TestProbleme.txt","Teststudent.txt")
tip ="memorie"

class TesteServP:
    def __init__(self):
        ...

    def testAdaugaProblemaService(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        problemaService = ProblemeService(problemaRepository, studentRepository,fisierP,fisierS)
        problemaService.adaugaProblema("Lab1","Suma","Maine",tip)
        probleme =problemaService.getALLProbleme(tip)
        assert len(probleme) == 1
        assert probleme[0].GetNrProb() == "Lab1"
        try:
            problemaService.adaugaProblema("Lab1","Suma","Azi",tip)

        except KeyError:
            ...

    def testModificaProblemaService(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        problemaService = ProblemeService(problemaRepository, studentRepository,fisierP,fisierS)
        problemaService.adaugaProblema("Lab1", "Suma", "Maine",tip)

        problemaService.modificaProblema("Lab1","Produs", "Azi",tip)

        probleme = problemaService.getALLProbleme(tip)
        assert len(probleme) == 1
        assert probleme[0].GetDescriere() == "Produs"
        try:
            problemaService.modificaProblema("Lab22", "Suma", "Azi",tip)

        except KeyError:
            ...

    def testStergeProblemaService(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        problemaService = ProblemeService(problemaRepository, studentRepository,fisierP,fisierS)
        problemaService.adaugaProblema("Lab1", "Suma", "Maine",tip)
        studentService = StudentService(studentRepository, problemaRepository, fisierS, fisierP)
        studentService.adaugaStudent("1", "Vlad", 315, "Lab1", 9.0, tip)
        studentService.adaugaStudent("2", "Vlad", 315, "-", 0, tip)

        problemaService.stergeProblema("Lab1",tip)

        probleme = problemaService.getALLProbleme(tip)
        assert len(probleme) == 0

        try:
            problemaService.stergeProblema("Lab3",tip)

        except KeyError:
            ...

    def testCautareProblemaService(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        problemaService = ProblemeService(problemaRepository, studentRepository,fisierP,fisierS)
        problemaService.adaugaProblema("Lab1", "Suma", "Maine",tip)
        try:
            problemaService.cautareProblema("lab334",tip)

        except KeyError:
            ...
