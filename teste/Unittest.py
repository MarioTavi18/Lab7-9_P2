import unittest
from domeniu.student import Student
from teste.testFisierProblemerepository import FileReprP
from teste.testFisierStudentrepository import FileReprS
from teste.testProblema import TesteProblema
from teste.testProblemaRepository import TesteReprP
from teste.testProblemaService import TesteServP
from teste.testStudent import TesteStudent
from teste.testStudentRepository import TesteReprS
from teste.testStudentService import TesteServS


class TestRepository(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.__domS = TesteStudent()
        self.__domP = TesteProblema()
        self.__RepS = TesteReprS()
        self.__RepP = TesteReprP()
        self.__ServS = TesteServS()
        self.__ServP = TesteServP()
        self.__FileS = FileReprS()
        self.__FileP = FileReprP()

    def DomainS(self):
        testcase1 = unittest.FunctionTestCase(self.__domS.testStudent())
        testcase2 = unittest.FunctionTestCase(self.__domS.testStudentSetteri())

    def DomainP(self):
        testcase1 = unittest.FunctionTestCase(self.__domP.testProblema())
        testcase2 = unittest.FunctionTestCase(self.__domP.testProblemaSetteri())

    def ServiceS(self):
        testcase1 = unittest.FunctionTestCase(self.__ServS.testAdaugaStudentService())
        testcase2 = unittest.FunctionTestCase(self.__ServS.testModificaStudentService())
        testcase3 = unittest.FunctionTestCase(self.__ServS.testCautareStudentService())
        testcase4 = unittest.FunctionTestCase(self.__ServS.testAsignareStudentService())
        testcase5 = unittest.FunctionTestCase(self.__ServS.testNotareStudentService())
        testcase6 = unittest.FunctionTestCase(self.__ServS.testOrdonareAlfStudentService())
        testcase7 = unittest.FunctionTestCase(self.__ServS.testOdonareNotaStudentService())
        testcase8 = unittest.FunctionTestCase(self.__ServS.testSub5StudentService())
        testcase9 = unittest.FunctionTestCase(self.__ServS.testStergeStudentService())

    def RepositoryS(self):
        testcase1 = unittest.FunctionTestCase(self.__RepS.testAdaugaStudentRepository())
        testcase2 = unittest.FunctionTestCase(self.__RepS.testCautareStudentRepository())
        testcase3 = unittest.FunctionTestCase(self.__RepS.testModificaStudentRepository())
        testcase4 = unittest.FunctionTestCase(self.__RepS.testStergeStudentRepository())

    def ServiceP(self):
        testcase1 = unittest.FunctionTestCase(self.__ServP.testAdaugaProblemaService())
        testcase2 = unittest.FunctionTestCase(self.__ServP.testModificaProblemaService())
        testcase3 = unittest.FunctionTestCase(self.__ServP.testStergeProblemaService())
        testcase4 = unittest.FunctionTestCase(self.__ServP.testCautareProblemaService())

    def RepositoryP(self):
        testcase1 = unittest.FunctionTestCase(self.__RepP.testAdaugaProblemaRepository())
        testcase2 = unittest.FunctionTestCase(self.__RepP.testModificaProblemaRepository())
        testcase3 = unittest.FunctionTestCase(self.__RepP.testStergeProblemaRepository())
        testcase4 = unittest.FunctionTestCase(self.__RepP.testCautareProblemaRepository())

    def FisierS(self):
        testcase1 = unittest.FunctionTestCase(self.__FileS.testAdaugaS())
        testcase2 = unittest.FunctionTestCase(self.__FileS.testModificaS())
        testcase3 = unittest.FunctionTestCase(self.__FileS.testStergeS())
        testcase4 = unittest.FunctionTestCase(self.__FileS.testCautareS())

    def FisierP(self):
        testcase1 = unittest.FunctionTestCase(self.__FileP.testAdaugaP())
        testcase2 = unittest.FunctionTestCase(self.__FileP.testModificaP())
        testcase3 = unittest.FunctionTestCase(self.__FileP.testStergeP())
        testcase4 = unittest.FunctionTestCase(self.__FileP.testCautareP())
