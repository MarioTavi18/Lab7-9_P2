from domeniu.probleme import Problema
from repository import FisierProblemerepository, FisierStudentrepository
from repository.problemeRepository import ProblemaRepository
from repository.studentRepository import StudentRepository


class ProblemeService:
    def __init__(self, problemeRepository: ProblemaRepository,studentRepository:StudentRepository, fisierP: FisierProblemerepository, fisierS: FisierStudentrepository):
        self.__problemaRepository = problemeRepository
        self.__studentRepository = studentRepository
        self.__fisierP = fisierP
        self.__fisierS = fisierS

    def getALLProbleme(self, tip):
        """
        returneaza lista de probleme
        :return: o lista de obiecte de tipul Problema
        """
        if tip == "memorie":
            return self.__problemaRepository.getAll()
        else:
            return self.__fisierP.getAll()

    def adaugaProblema (self, NrProb, Descriere, Deadline, tip):
        """
        adauga o problema
        :param NrProb: string
        :param Descriere: string
        :param Deadline: int
        :return:
        """
        problema = Problema(NrProb,Descriere,Deadline)
        if tip == "memorie":
            self.__problemaRepository.adaugaProblema(problema)
        else:
            self.__fisierP.adauga(problema)

    def modificaProblema(self, NrProb,DescriereNou,DeadlineNou, tip):
        """
        modifica o problema dupa nr
        :param NrProb: string
        :param DescriereNou: string
        :param DeadlineNou: int
        :return:
        """
        problemaNou = Problema (NrProb, DescriereNou, DeadlineNou)
        if tip == "memorie":
            self.__problemaRepository.modificaProblema(problemaNou)
        else:
            self.__fisierP.modifica(problemaNou)

    def stergeProblema(self, NrProb, tip):
        """
        sterge o problema dupa nr
        :param NrProb: string
        :return:
        """
        if tip == "memorie":
            studenti = self.__studentRepository.getAll()
            for student in studenti:
                if student.getLucrare() == NrProb:
                    student.setLucrare("-")
                    student.setNota(0.0)
            self.__problemaRepository.stergeProblema(NrProb)
        else:
            studenti = self.__fisierS.getAll()
            for student in studenti:
                if student.getLucrare() == NrProb:
                    student.setLucrare("-")
                    student.setNota(0.0)
            self.__fisierP.sterge(NrProb)

    def cautareProblema(self, NrProb, tip):
        """
        cauta o problema
        :param NrProb: string
        :return:
        """
        if tip == "memorie":
            if self.__problemaRepository.getByNr(NrProb) is None:
                raise KeyError("Nu exista nicio problema cu nr-ul dat!")
            problema = self.__problemaRepository.cautareProblema(NrProb)
            return problema
        else:
            self.__fisierP.cautare(NrProb)
