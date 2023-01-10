import unittest
from os import name

from repository.FisierProblemerepository import FisierProblemerepository
from repository.FisierStudentrepository import FisierStudentrepository
from repository.problemeRepository import ProblemaRepository
from repository.studentRepository import StudentRepository
from service.ProblemeService import ProblemeService
from service.StudentService import StudentService
from teste.testAll import testAll
from ui.consola import Consola
from unittests.unittestall import unittestall

#iteratie 1: clasele,adaugare,stergere,modificare,afisare
#iteratie 2: cautare dupa id, asignare laborator/notarea lui
#iteratie 3: statistici (lista de studenti si notelor lor ordonata alfabetic)
def main():
    with open('TestStudent.txt','r+') as f:
        f.truncate(0)
    with open('TestProbleme.txt','r+') as f:
        f.truncate(0)

    testAll()
    unittestall()

    fisierS = FisierStudentrepository("C:\\Users\\mario\\Desktop\\Laborator\\Lab7-9 P2\\student.txt")
    fisierP = FisierProblemerepository("probleme.txt","student.txt")
    problemaRepository = ProblemaRepository()
    studentRepository = StudentRepository()

    problemaService = ProblemeService (problemaRepository, studentRepository, fisierP, fisierS)
    studentService = StudentService(studentRepository,problemaRepository,fisierS, fisierP)

    consola = Consola(studentService, problemaService, fisierS, fisierP)
    consola.meniu()

main()