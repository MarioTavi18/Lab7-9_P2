from domeniu.student import Student
from repository.studentRepository import StudentRepository


class FisierStudentrepository(StudentRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                lista = line.split(',')
                lista[4] = lista[4][:-1]
                lista[0] = lista[0].replace('id: ', '')
                lista[1] = lista[1].replace(' nume: ', '')
                lista[2] = int(lista[2].replace(' grup: ', ''))
                lista[3] = lista[3].replace(' lucrare: ', '')
                lista[4] = float(lista[4].replace(' nota: ', ''))
                student = Student(lista[0], lista[1], lista[2], lista[3], lista[4])
                # todo handle exception
                super().adaugaStudent(student)

    def adauga(self, student):
        """with open('probleme.txt',"r+") as f:
            for x in f:
                lista= x.split(',')
                lista[4] = lista[4][:-1]
                lista[0] = lista[0].replace('id: ','')
                lista[1] = lista[1].replace(' nume: ', '')
                lista[2] = int(lista[2].replace(' grup: ', ''))
                lista[3] = lista[3].replace(' lucrare: ', '')
                lista[4] = float(lista[4].replace(' nota: ', ''))
                student = Student(lista[0],lista[1],lista[2],lista[3],lista[4])
                self.__Fstudenti[student.getStudentID()] = student
        """
        super().adaugaStudent(student)
        #if self.getById(student.getStudentID()) is not None:
            #raise KeyError("Exista deja un student cu ID-ul dat.")
        with open(self.__file_name,'a') as f:
            f.write(str(student))
            f.write('\n')
        #self.__studenti[student.getStudentID()] = student

    def modifica(self, studentNou):
        """
        modifica un student dupa id
        :param studentNou: obiect de tipul Student
        :return:
        """
        super().modificaStudent(studentNou)
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
        with open(self.__file_name, "w") as f:
            for line in lines:
                lista = line.split(',')
                lista[4] = lista[4][:-1]
                lista[0] = lista[0].replace('id: ', '')
                if lista[0] != studentNou.getStudentID():
                    f.write(line)
                else:
                    f.write(str(studentNou)+'\n')

    def sterge(self, studentID):
        """
        sterge un student dupa id
        :param studentID: string
        :return:
        """
        super().stergeStudent(studentID)
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
        with open(self.__file_name, "w") as f:
            for line in lines:
                lista = line.split(',')
                lista[4] = lista[4][:-1]
                lista[0] = lista[0].replace('id: ', '')
                if lista[0] != studentID:
                    f.write(line)

    def cautare(self, studentID):
        """
        cauta un student dupa ID
        :param studentID: string
        :return:
        """
        super().cautareStudent(studentID)

