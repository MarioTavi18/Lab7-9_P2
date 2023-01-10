from repository.FisierProblemerepository import FisierProblemerepository
from repository.FisierStudentrepository import FisierStudentrepository
from repository.problemeRepository import ProblemaRepository
from repository.studentRepository import StudentRepository
from service.ProblemeService import ProblemeService
from service.StudentService import StudentService

fisierS = FisierStudentrepository("TestStudent.txt")
fisierP = FisierProblemerepository("TestProbleme.txt","TestStudent.txt")
tip ="memorie"

class TesteServS:
    def __init__(self):
        ...

    def testAdaugaStudentService(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        studentService = StudentService(studentRepository,problemaRepository,fisierS,fisierP)
        studentService.adaugaStudent("1","Vlad",315,"-",0,tip)
        studenti= studentService.getALLStudenti(tip)
        assert len(studenti) == 1
        assert studenti[0].getStudentID() == "1"
        assert studenti[0].getGrup() == 315
        try:
            studentService.adaugaStudent("1","Vlad",316,"-",0,tip)

        except KeyError:
            assert True
        try:
            studentService.adaugaStudent("3", "Vlad", 316, "Lab1", 0, tip)

        except KeyError:
            assert True
        try:
            studentService.adaugaStudent("3", "Vlad", 316, "-", 9.0, tip)

        except KeyError:
            assert True


    def testModificaStudentService(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        studentService = StudentService(studentRepository,problemaRepository,fisierS,fisierP)
        studentService.adaugaStudent("1", "Vlad", 315,"-",0, tip)
        studentService.modificaStudent("1","Ana",315,"-",0.0,tip)
        studenti = studentService.getALLStudenti(tip)
        assert len(studenti) == 1
        assert studenti[0].getNume() == "Ana"

        try:
            studentService.modificaStudent("33", "Vlad", 316,"Mate1",3.0,tip)

        except KeyError:
            ...

    def testStergeStudentService(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        studentService = StudentService(studentRepository,problemaRepository,fisierS,fisierP)
        studentService.adaugaStudent("1", "Vlad", 315,"-",0,tip)
        studentService.stergeStudent("1",tip)
        studenti = studentService.getALLStudenti(tip)
        assert len(studenti) == 0

        try:
            studentService.stergeStudent("2222", tip)

        except KeyError:
            ...

    def testCautareStudentService(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        studentService = StudentService(studentRepository, problemaRepository,fisierS,fisierP)
        studentService.adaugaStudent("1", "Vlad", 315, "-", 0,tip)
        try:
            studentService.cautareStudent("33",tip)

        except KeyError:
            ...

    def testAsignareStudentService(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        problemaService = ProblemeService(problemaRepository,studentRepository,fisierS,fisierP)
        studentService = StudentService(studentRepository, problemaRepository,fisierS,fisierP)

        problemaService.adaugaProblema("Lab1", "Suma", "Maine",tip)
        studentService.adaugaStudent("1", "Vlad", 315, "-", 0,tip)
        studentService.Asignare("1","Lab1", tip)
        studenti =studentRepository.getAll()
        assert len(studenti) == 1
        assert studenti[0].getLucrare() == "Lab1"


    def testNotareStudentService(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        problemaService = ProblemeService(problemaRepository, studentRepository,fisierS,fisierP)
        studentService = StudentService(studentRepository, problemaRepository,fisierS,fisierP)

        problemaService.adaugaProblema("Lab1", "Suma", "Maine",tip)
        studentService.adaugaStudent("1", "Vlad", 315, "Lab1", 0,tip)
        studentService.Notare("1","9.80",tip)
        studenti = studentRepository.getAll()
        assert len(studenti) == 1
        assert studenti[0].getNota() == "9.80"

    def testOrdonareAlfStudentService(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        problemaService = ProblemeService(problemaRepository, studentRepository,fisierS,fisierP)
        studentService = StudentService(studentRepository, problemaRepository,fisierS,fisierP)

        problemaService.adaugaProblema("Lab1", "Suma", "Maine",tip)
        studentService.adaugaStudent("1", "Vlad", 315, "Lab1", 8,tip)
        studentService.adaugaStudent("2", "Vlad", 315, "-", 0,tip)
        studentService.adaugaStudent("3", "Ana", 315, "-", 0,tip)

        studenti = studentService.ordonareAlf(tip)
        assert len(studenti) == 3
        assert studenti[0].getStudentID() == "3"
        assert studenti[1].getStudentID() == "2"
        assert studenti[2].getStudentID() == "1"

    def testOdonareNotaStudentService(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        problemaService = ProblemeService(problemaRepository, studentRepository,fisierS,fisierP)
        studentService = StudentService(studentRepository, problemaRepository,fisierS,fisierP)

        problemaService.adaugaProblema("Lab1", "Suma", "Maine",tip)
        studentService.adaugaStudent("1", "Vlad", 315, "Lab1", 8,tip)
        studentService.adaugaStudent("2", "Vlad", 315, "Lab1", 3,tip)
        studentService.adaugaStudent("3", "Ana", 315, "-", 0,tip)

        studenti = studentService.ordonareNota(tip)
        assert len(studenti) == 3
        assert studenti[0].getStudentID() == "3"
        assert studenti[1].getStudentID() == "2"
        assert studenti[2].getStudentID() == "1"

    def testSub5StudentService(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        problemaService = ProblemeService(problemaRepository, studentRepository,fisierS,fisierP)
        studentService = StudentService(studentRepository, problemaRepository,fisierS,fisierP)

        problemaService.adaugaProblema("Lab1", "Suma", "Maine",tip)
        studentService.adaugaStudent("1", "Vlad", 315, "Lab1", 8,tip)
        studentService.adaugaStudent("2", "Vlad", 315, "Lab1", 3,tip)
        studentService.adaugaStudent("3", "Ana", 315, "Lab1", 0,tip)

        studenti = studentService.Sub5(tip)
        assert len(studenti) == 2

        assert studenti[0].getNume() == "Ana"
        assert studenti[1].getNume() == "Vlad"



