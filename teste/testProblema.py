from domeniu.probleme import Problema

class TesteProblema:
    def __init__(self):
        ...

    def testProblema(self):
        problema = Problema("Lab1","Scrie o suma","12.02.2022")

        assert problema.GetNrProb() == "Lab1"
        assert problema.GetDescriere() == "Scrie o suma"
        assert problema.GetDeadline() == "12.02.2022"

    def testProblemaSetteri(self):
        problema = Problema("Lab1", "Scrie o suma", "12.02.2022")

        problema.SetNrProb("Lab2")
        assert problema.GetNrProb() == "Lab2"

        problema.SetDescriere("Scrie ceva")
        assert problema.GetDescriere() =="Scrie ceva"

        problema.SetDeadline("12.02.2012")
        assert problema.GetDeadline() == "12.02.2012"