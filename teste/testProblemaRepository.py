from domeniu.probleme import Problema

from repository.problemeRepository import ProblemaRepository
from repository.studentRepository import StudentRepository

class TesteReprP:
    def __init__(self):
        ...
    def testAdaugaProblemaRepository(self):
        problemaRepository = ProblemaRepository()
        problema = Problema("Lab1", "Scrie o suma", "12.02.2022")
        problemaRepository.adaugaProblema(problema)

        probleme=problemaRepository.getAll()
        assert len(probleme) == 1
        assert probleme[0].GetNrProb() == "Lab1"

        try:
            problemaRepository.adaugaProblema(problema)

        except KeyError:
            ...

    def testModificaProblemaRepository(self):
        problemaRepository = ProblemaRepository()
        problema = Problema("Lab1", "Scrie o suma", "12.02.2022")
        problemaNou1 = Problema("Lab1", "Scrie un produs", "13.03.2023")
        problemaNou2 = Problema("Lab3", "Scrie o suma", "12.02.2022")
        problemaRepository.adaugaProblema(problema)

        problemaRepository.modificaProblema(problemaNou1)
        probleme = problemaRepository.getAll()
        assert len(probleme) == 1
        assert probleme[0].GetDescriere() == "Scrie un produs"

        try:
            problemaRepository.modificaProblema(problemaNou2)

        except KeyError:
            ...


    def testStergeProblemaRepository(self):
        problemaRepository = ProblemaRepository()
        problema = Problema("Lab1", "Scrie o suma", "12.02.2022")
        problemaRepository.adaugaProblema(problema)

        problemaRepository.stergeProblema("Lab1")
        probleme = problemaRepository.getAll()
        assert len(probleme) == 0
        try:
            problemaRepository.stergeProblema("!")

        except KeyError:
            ...

    def testCautareProblemaRepository(self):
        problemaRepository = ProblemaRepository()
        studentRepository = StudentRepository()
        problema = Problema("Lab1", "Scrie o suma", "12.02.2022")
        problemaRepository.adaugaProblema(problema)
        try:
            problemaRepository.cautareProblema("Lab3")

        except KeyError:
            ...