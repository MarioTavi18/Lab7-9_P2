from unittests.unittest_DTO import TestStudentSub5, TestStudentNumaiGrup
from unittests.unittest_FisierP import TestProblemaFisier
from unittests.unittest_FisierS import TestStudentFisier
from unittests.unittest_probleme import TestProbleme
from unittests.unittest_repositoryProbleme import TestProblemeRepository
from unittests.unittest_repositoryStudent import TestStudentRepository
from unittests.unittest_serviceProbleme import TestProblemeService
from unittests.unittest_serviceStudent import TestStudentService
from unittests.unittest_student import TestStudent


def unittestall():
    testS =TestStudent()
    testS.test_getStudentID()
    testS.test_setStudentID()
    testS.test_getGrup()
    testS.test_setGrup()
    testS.test_getNume()
    testS.test_setNume()
    testS.test_getLucrare()
    testS.test_setLucrare()
    testS.test_getNota()
    testS.test_setNota()

    testP = TestProbleme()
    testP.test_getNrProb()
    testP.test_setNrProb()
    testP.test_getDeadline()
    testP.test_setDeadline()
    testP.test_getDescriere()
    testP.test_setDescriere()

    Sub5 = TestStudentSub5()
    Sub5.test_getNume()
    Sub5.test_setNume()
    Sub5.test_getNota()
    Sub5.test_setNota()

    NumaiGrup = TestStudentNumaiGrup()
    NumaiGrup.test_getNume()
    NumaiGrup.test_setNume()
    NumaiGrup.test_getGrup()
    NumaiGrup.test_setGrup()

    testServP =TestProblemeService()
    testServP.test_getAllproblems()
    testServP.testAdaugaProblemaService()
    testServP.testModificaProblemaService()
    testServP.testStergeProblemaService()
    testServP.test_cautareproblema()

    testServS = TestStudentService()
    testServS.test_adaugaStudent()
    testServS.test_modificastudent()
    testServS.test_stergestudent()
    testServS.test_getAllstudenti()
    testServS.test_cautareStudent()
    testServS.test_notarestudent()
    testServS.test_Asignare()
    testServS.test_ordonarestudentnota()
    testServS.test_ordonaresub5()
    testServS.test_ordonareNumaiGrup()

    testRepP = TestProblemeRepository()
    testRepP.test_GetAll()
    testRepP.test_GetByNrProb()
    testRepP.test_adaugaProblema()
    testRepP.test_modificaProblema()
    testRepP.test_stergeProblema()
    testRepP.test_cautareProblema()

    testRepS = TestStudentRepository()
    testRepS.test_GetById()
    testRepS.test_GetAll()
    testRepS.test_adaugaStudent()
    testRepS.test_modificaStudent()
    testRepS.test_stergeStudent()
    testRepS.test_cautareStudent()

    testFileP =TestProblemaFisier()
    testFileP.test_adaugaProbleme()
    testFileP.test_modificaProblema()
    testFileP.test_stergeProblema()
    testFileP.test_cautareProblema()

    testFileS = TestStudentFisier()
    testFileS.test_adaugaStudent()
    testFileS.test_modificaStudent()
    testFileS.test_stergeStudent()
    testFileS.test_cautareStudent()




