from domeniu.probleme import Problema
from domeniu.student import Student
from repository.problemeRepository import ProblemaRepository

class FisierProblemerepository(ProblemaRepository):
    def __init__(self, file_name, file_name2):
        super().__init__()
        self.__file_name = file_name
        self.__file_name2 = file_name2
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                lista = line.split(',')
                lista[2] = lista[2][:-1]
                lista[0] = lista[0].replace('Nr: ', '')
                lista[1] = lista[1].replace(' Descriere: ', '')
                lista[2] = lista[2].replace(' Deadline: ', '')
                problema = Problema(lista[0], lista[1], lista[2])
                # todo handle exception
                super().adaugaProblema(problema)

    def adauga(self, problema):
        super().adaugaProblema(problema)
        with open(self.__file_name,'a') as f:
            f.write(str(problema))
            f.write('\n')

    def modifica(self, problemaNou):
        """
        modifica o problema dupa nr
        :param problemaNou: obiect de tipul Problema
        :return:
        """
        super().modificaProblema(problemaNou)
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
        with open(self.__file_name, "w") as f:
            for line in lines:
                lista = line.split(',')
                lista[2] = lista[2][:-1]
                lista[0] = lista[0].replace('Nr: ', '')
                if lista[0] != problemaNou.GetNrProb():
                    f.write(line)
                else:
                    f.write(str(problemaNou)+'\n')

    def sterge(self, NrProb):
        """
        sterge un student dupa id
        :param NrProb: string
        :return:
        """
        super().stergeProblema(NrProb)
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
        with open(self.__file_name, "w") as f:
            for line in lines:
                lista = line.split(',')
                lista[2] = lista[2][:-1]
                lista[0] = lista[0].replace('Nr: ', '')
                if lista[0] != NrProb:
                    f.write(line)

        with open(self.__file_name2, "r") as f:
            lines = f.readlines()
        with open(self.__file_name2, "w") as f:
            for line in lines:
                lista = line.split(',')
                lista[4] = lista[4][:-1]
                lista[3] = lista[3].replace(' lucrare: ', '')
                if lista[3] != NrProb:
                    f.write(line)
                else:
                            lista[0] = lista[0].replace('id: ', '')
                            lista[1] = lista[1].replace(' nume: ', '')
                            lista[2] = int(lista[2].replace(' grup: ', ''))
                            lista[4] = float(lista[4].replace(' nota: ', ''))
                            student = Student(lista[0], lista[1], lista[2], "-", 0.0)
                            print("intrat")
                            f.write(str(student)+'\n')

    def cautare(self,NrProb):
        """
        cauta o problema dupa nr
        :param NrProb: string
        :return:
        """
        super().cautareProblema(NrProb)