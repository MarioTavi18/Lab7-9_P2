from repository.problemeRepository import ProblemaRepository
#from domeniu.student import Student
class StudentRepository:
    def __init__(self):
        self.__studenti = {}

    def getAll(self):
        """
        returneaza lista de studenti
        :return: o lista de obiecte de tipul studenti
        """
        # daca am scrie return self.__studenti, am returna un dictionar
        # iar layerele "de mai sus" au nevoie de o lista( ex. cand afisam studenti,
        # este mai citibil daca afisam o lista vs un dictionar)
        return list(self.__studenti.values())

    def getById(self, studentID):
        """
        returneaza studentul cu id-ul dat
        :param studentID: string
        :return: un obiect de tipul student, daca exista unul cu id-ul dat,altfel None
        """
        if studentID in self.__studenti:
            return self.__studenti[studentID]
        return None
        #return self.__studenti[studentID, None]

    def adaugaStudent(self, student):
        """
        adauga un student in dictionar
        :param student: obiect de tipul Student
        :return:
        """
        if self.getById(student.getStudentID()) is not None:
            raise KeyError("Exista deja un student cu ID-ul dat.")
        self.__studenti[student.getStudentID()] = student

    def modificaStudent(self, studentNou):
        """
        modifica un student dupa id
        :param studentNou: obiect de tipul Student
        :return:
        """
        if self.getById(studentNou.getStudentID()) is None:
            raise KeyError("Nu exista niciun student cu ID-ul dat!")
        self.__studenti[studentNou.getStudentID()] =studentNou

    def stergeStudent(self, studentID):
        """
        sterge un student dupa id
        :param studentID: string
        :return:
        """
        if self.getById(studentID) is None:
            raise KeyError("Nu exista niciun student cu ID-ul dat!")
        self.__studenti.pop(studentID)

    def cautareStudent(self, studentID):
        """
        cauta un student dupa id
        :param studentID: string
        :return:
        """
        return self.__studenti[studentID]
