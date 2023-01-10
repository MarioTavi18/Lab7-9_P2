from teste.Unittest import TestRepository
import unittest
from teste.testFisierProblemerepository import FileReprP
from teste.testFisierStudentrepository import FileReprS

from teste.testProblema import TesteProblema
from teste.testProblemaRepository import TesteReprP
from teste.testProblemaService import TesteServP

from teste.testStudent import TesteStudent
from teste.testStudentRepository import TesteReprS
from teste.testStudentService import TesteServS


def testAll():
    testRepository = TestRepository()
    testRepository.DomainS()
    testRepository.DomainP()
    testRepository.ServiceS()
    testRepository.RepositoryS()
    testRepository.ServiceP()
    testRepository.RepositoryP()

    testRepository.FisierS()
    testRepository.FisierP()

    testS = TesteStudent()
    testP = TesteProblema()
    testS.testStudent()
    testP.testProblema()
    testS.testStudentSetteri()
    testP.testProblemaSetteri()

    testReprP = TesteReprP()
    testReprP.testAdaugaProblemaRepository()
    testReprP.testModificaProblemaRepository()
    testReprP.testStergeProblemaRepository()
    testReprP.testCautareProblemaRepository()

    testFileP = FileReprP()
    testFileP.testAdaugaP()
    testFileP.testModificaP()
    testFileP.testStergeP()
    testFileP.testCautareP()

    testReprS = TesteReprS()
    testReprS.testAdaugaStudentRepository()
    testReprS.testModificaStudentRepository()
    testReprS.testStergeStudentRepository()
    testReprS.testCautareStudentRepository()

    testFileS = FileReprS()
    testFileS.testAdaugaS()
    testFileS.testModificaS()
    testFileS.testStergeS()
    testFileS.testCautareS()

    testServP = TesteServP()
    testServP.testAdaugaProblemaService()
    testServP.testModificaProblemaService()
    testServP.testStergeProblemaService()
    testServP.testCautareProblemaService()

    testServS = TesteServS()
    testServS.testAdaugaStudentService()
    testServS.testModificaStudentService()
    testServS.testStergeStudentService()
    testServS.testCautareStudentService()
    testServS.testAsignareStudentService()
    testServS.testNotareStudentService()
    testServS.testOrdonareAlfStudentService()
    testServS.testOdonareNotaStudentService()
    testServS.testSub5StudentService()
