class Problema:
    def __init__(self,NrProb,Descriere,Deadline):
        self.__NrProb = NrProb
        self.__Descriere = Descriere
        self.__Dealine = Deadline

    def GetNrProb(self):
        return self.__NrProb

    def GetDescriere(self):
        return self.__Descriere

    def GetDeadline(self):
        return self.__Dealine

    def SetNrProb(self, NrProb):
        self.__NrProb = NrProb

    def SetDescriere(self, Descriere):
        self.__Descriere = Descriere

    def SetDeadline(self, Deadline):
        self.__Dealine = Deadline

    def __str__(self):
        return f"Nr: {self.__NrProb}, Descriere: {self.__Descriere}, Deadline: {self.__Dealine}"