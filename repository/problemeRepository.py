class ProblemaRepository:
    def __init__(self):
        self.__probleme = {}

    def getAll(self):
        """
        returneaza lista de probleme
        :return: o lista de obiecte de tipul probleme
        """
        return list(self.__probleme.values())

    def getByNr(self, NrProb):
        """
        returneaza problema cu nr-ul dat
        :param NrProb: string
        :return: un obiect de tipul problema, daca exista unul cu nr-ul dat,altfel None
        """
        if NrProb in self.__probleme:
            return self.__probleme[NrProb]
        return None

    def adaugaProblema(self, problema):
        """
        adauga o problema in dictionar
        :param problema: obiect de tipul Problema
        :return:
        """
        if self.getByNr(problema.GetNrProb()) is not None:
            raise KeyError("Exista deja o problema cu nr-ul dat.")
        self.__probleme[problema.GetNrProb()] = problema

    def modificaProblema(self, problemaNou):
        """
        modifica o problema dupa nr
        :param problemaNou: obiect de tipul Problema
        :return:
        """
        if self.getByNr(problemaNou.GetNrProb())is None:
            raise KeyError("Nu exista o problema cu nr-ul dat!")
        self.__probleme[problemaNou.GetNrProb()] = problemaNou

    def stergeProblema(self,NrProb):
        """
        sterge o problema dupa nr
        :param NrProb: un obiect de tipul Problema
        :return:
        """
        if self.getByNr(NrProb) is None:
            raise KeyError("Nu exista o problema cu nr-ul dat!")
        self.__probleme.pop(NrProb)

    def cautareProblema(self, NrProb):
        """
        cauta o problema dupa nr
        :param NrProb: string
        :return:
        """
        return self.__probleme[NrProb]